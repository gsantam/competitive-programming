"""
Test suite for EventBookingSystem

Run with: pytest test_booking.py -v
Run specific phase: pytest test_booking.py -v -k "phase1"
"""

import pytest
from booking import EventBookingSystem


# ============================================================================
# PHASE 1: Basic Event Management
# ============================================================================

class TestPhase1BasicEventManagement:
    """Phase 1: Basic create, book, cancel, get_bookings operations."""

    def test_phase1_create_event(self):
        """Can create an event."""
        system = EventBookingSystem()
        assert system.create_event("meeting", 100, 200, 5) is True

    def test_phase1_create_duplicate_event_fails(self):
        """Cannot create event with existing id."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        assert system.create_event("e1", 300, 400, 10) is False

    def test_phase1_book_user(self):
        """Can book a user for an event."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        assert system.book("e1", "alice") is True

    def test_phase1_book_nonexistent_event(self):
        """Booking nonexistent event returns False."""
        system = EventBookingSystem()
        assert system.book("fake", "alice") is False

    def test_phase1_book_duplicate_user(self):
        """Cannot book same user twice for same event."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.book("e1", "alice")
        assert system.book("e1", "alice") is False

    def test_phase1_book_at_capacity(self):
        """Cannot book when event is at capacity."""
        system = EventBookingSystem()
        system.create_event("small", 100, 200, 2)
        system.book("small", "user1")
        system.book("small", "user2")
        assert system.book("small", "user3") is False

    def test_phase1_get_bookings(self):
        """get_bookings returns list of booked users."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.book("e1", "alice")
        system.book("e1", "bob")
        bookings = system.get_bookings("e1")
        assert sorted(bookings) == ["alice", "bob"]

    def test_phase1_get_bookings_nonexistent(self):
        """get_bookings returns None for nonexistent event."""
        system = EventBookingSystem()
        assert system.get_bookings("fake") is None

    def test_phase1_get_bookings_empty(self):
        """get_bookings returns empty list for event with no bookings."""
        system = EventBookingSystem()
        system.create_event("empty", 100, 200, 5)
        assert system.get_bookings("empty") == []

    def test_phase1_cancel_booking(self):
        """Can cancel a booking."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.book("e1", "alice")
        assert system.cancel("e1", "alice") is True
        assert system.get_bookings("e1") == []

    def test_phase1_cancel_nonexistent_event(self):
        """Cancel on nonexistent event returns False."""
        system = EventBookingSystem()
        assert system.cancel("fake", "alice") is False

    def test_phase1_cancel_user_not_booked(self):
        """Cancel for user not booked returns False."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        assert system.cancel("e1", "alice") is False

    def test_phase1_cancel_frees_capacity(self):
        """Cancelling frees up capacity for new bookings."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "alice")
        assert system.book("e1", "bob") is False  # At capacity
        system.cancel("e1", "alice")
        assert system.book("e1", "bob") is True  # Now has space

    def test_phase1_multiple_events(self):
        """Multiple events are independent."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 2)
        system.create_event("e2", 100, 200, 2)
        system.book("e1", "alice")
        system.book("e2", "alice")
        system.book("e2", "bob")

        assert sorted(system.get_bookings("e1")) == ["alice"]
        assert sorted(system.get_bookings("e2")) == ["alice", "bob"]


# ============================================================================
# PHASE 2: Time Conflict Detection
# ============================================================================

class TestPhase2ConflictDetection:
    """Phase 2: Time conflict detection and schedule queries."""

    def test_phase2_no_conflict_different_times(self):
        """User can book non-overlapping events."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.create_event("e2", 300, 400, 5)
        system.book("e1", "alice")
        assert system.book("e2", "alice") is True

    def test_phase2_conflict_overlapping_events(self):
        """User cannot book overlapping events."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.create_event("e2", 150, 250, 5)
        system.book("e1", "alice")
        assert system.book("e2", "alice") is False

    def test_phase2_conflict_one_inside_other(self):
        """Conflict when one event is entirely inside another."""
        system = EventBookingSystem()
        system.create_event("outer", 100, 400, 5)
        system.create_event("inner", 200, 300, 5)
        system.book("outer", "alice")
        assert system.book("inner", "alice") is False

    def test_phase2_no_conflict_adjacent_events(self):
        """Adjacent events (end = start) don't conflict."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.create_event("e2", 200, 300, 5)  # Starts when e1 ends
        system.book("e1", "alice")
        assert system.book("e2", "alice") is True

    def test_phase2_conflict_only_affects_same_user(self):
        """Different users can book overlapping events."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.create_event("e2", 150, 250, 5)
        system.book("e1", "alice")
        assert system.book("e2", "bob") is True  # Different user, OK

    def test_phase2_get_user_schedule_empty(self):
        """get_user_schedule returns empty list for user with no bookings."""
        system = EventBookingSystem()
        assert system.get_user_schedule("nobody") == []

    def test_phase2_get_user_schedule_sorted(self):
        """get_user_schedule returns bookings sorted by start time."""
        system = EventBookingSystem()
        system.create_event("late", 500, 600, 5)
        system.create_event("early", 100, 200, 5)
        system.create_event("mid", 300, 400, 5)
        system.book("late", "alice")
        system.book("early", "alice")
        system.book("mid", "alice")

        schedule = system.get_user_schedule("alice")
        assert schedule == [
            (100, 200, "early"),
            (300, 400, "mid"),
            (500, 600, "late")
        ]

    def test_phase2_find_conflicts_none(self):
        """find_conflicts returns empty list when no conflicts."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.book("e1", "alice")
        assert system.find_conflicts(300, 400, "alice") == []

    def test_phase2_find_conflicts_single(self):
        """find_conflicts finds a single conflicting event."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.book("e1", "alice")
        conflicts = system.find_conflicts(150, 250, "alice")
        assert conflicts == ["e1"]

    def test_phase2_find_conflicts_multiple(self):
        """find_conflicts finds multiple conflicting events."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.create_event("e2", 300, 400, 5)
        system.create_event("e3", 500, 600, 5)
        system.book("e1", "alice")
        system.book("e2", "alice")
        system.book("e3", "alice")

        # Query overlaps with e1 and e2, but not e3
        conflicts = system.find_conflicts(150, 350, "alice")
        assert sorted(conflicts) == ["e1", "e2"]

    def test_phase2_cancel_removes_conflict(self):
        """After cancelling, user can book previously conflicting event."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.create_event("e2", 150, 250, 5)
        system.book("e1", "alice")
        assert system.book("e2", "alice") is False  # Conflict
        system.cancel("e1", "alice")
        assert system.book("e2", "alice") is True  # No more conflict


# ============================================================================
# PHASE 3: Recurring Events
# ============================================================================

class TestPhase3RecurringEvents:
    """Phase 3: Recurring event support."""

    def test_phase3_create_recurring_event(self):
        """Can create a recurring event."""
        system = EventBookingSystem()
        assert system.create_recurring_event(
            "weekly", 100, 150, 5, 1000, 3) is True

    def test_phase3_create_recurring_duplicate_fails(self):
        """Cannot create recurring event with existing id."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        assert system.create_recurring_event(
            "e1", 100, 150, 5, 1000, 3) is False

    def test_phase3_get_occurrences(self):
        """get_occurrences returns all occurrence time ranges."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 5, 1000, 3)
        occurrences = system.get_occurrences("r1")
        assert occurrences == [(100, 150), (1100, 1150), (2100, 2150)]

    def test_phase3_get_occurrences_nonexistent(self):
        """get_occurrences returns None for nonexistent event."""
        system = EventBookingSystem()
        assert system.get_occurrences("fake") is None

    def test_phase3_get_occurrences_regular_event(self):
        """get_occurrences works for non-recurring events too."""
        system = EventBookingSystem()
        system.create_event("single", 100, 200, 5)
        assert system.get_occurrences("single") == [(100, 200)]

    def test_phase3_book_occurrence(self):
        """Can book specific occurrence of recurring event."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 5, 1000, 3)
        assert system.book_occurrence("r1", 0, "alice") is True
        assert system.book_occurrence("r1", 2, "alice") is True

    def test_phase3_book_occurrence_invalid_index(self):
        """book_occurrence fails for invalid occurrence index."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 5, 1000, 3)
        assert system.book_occurrence("r1", 5, "alice") is False
        assert system.book_occurrence("r1", -1, "alice") is False

    def test_phase3_book_occurrence_duplicate(self):
        """Cannot book same user for same occurrence twice."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 5, 1000, 3)
        system.book_occurrence("r1", 0, "alice")
        assert system.book_occurrence("r1", 0, "alice") is False

    def test_phase3_occurrences_have_independent_capacity(self):
        """Each occurrence has its own capacity."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 1, 1000, 2)
        system.book_occurrence("r1", 0, "alice")
        assert system.book_occurrence("r1", 0, "bob") is False  # First full
        assert system.book_occurrence(
            "r1", 1, "bob") is True   # Second available

    def test_phase3_cancel_occurrence(self):
        """Can cancel specific occurrence booking."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 5, 1000, 3)
        system.book_occurrence("r1", 0, "alice")
        assert system.cancel_occurrence("r1", 0, "alice") is True
        # Can book again after cancel
        assert system.book_occurrence("r1", 0, "bob") is True

    def test_phase3_conflict_across_occurrences(self):
        """Conflict detection works across recurring event occurrences."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 200, 5, 1000, 3)
        # Occurrences: [100,200), [1100,1200), [2100,2200)
        system.book_occurrence("r1", 1, "alice")  # Book [1100,1200)

        system.create_event("conflict", 1150, 1250, 5)
        # Conflicts with occurrence 1
        assert system.book("conflict", "alice") is False

    def test_phase3_no_conflict_between_different_occurrences(self):
        """User can book multiple non-overlapping occurrences."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 200, 5, 1000, 3)
        assert system.book_occurrence("r1", 0, "alice") is True
        assert system.book_occurrence("r1", 1, "alice") is True
        assert system.book_occurrence("r1", 2, "alice") is True

    def test_phase3_user_schedule_includes_occurrences(self):
        """get_user_schedule includes recurring event occurrences."""
        system = EventBookingSystem()
        system.create_recurring_event("r1", 100, 150, 5, 1000, 3)
        system.book_occurrence("r1", 0, "alice")
        system.book_occurrence("r1", 2, "alice")

        schedule = system.get_user_schedule("alice")
        # Note: might include occurrence info - accept reasonable formats
        assert len(schedule) == 2
        assert schedule[0][0] == 100  # First occurrence start
        assert schedule[1][0] == 2100  # Third occurrence start


# ============================================================================
# PHASE 4: Waitlist with Priority
# ============================================================================

class TestPhase4Waitlist:
    """Phase 4: Waitlist with priority-based auto-promotion."""

    def test_phase4_join_waitlist(self):
        """Can join waitlist for full event."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "alice")
        assert system.join_waitlist("e1", "bob", 1) is True

    def test_phase4_join_waitlist_nonexistent_event(self):
        """Cannot join waitlist for nonexistent event."""
        system = EventBookingSystem()
        assert system.join_waitlist("fake", "alice", 1) is False

    def test_phase4_join_waitlist_already_booked(self):
        """Cannot join waitlist if already booked."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 5)
        system.book("e1", "alice")
        assert system.join_waitlist("e1", "alice", 1) is False

    def test_phase4_join_waitlist_already_on_waitlist(self):
        """Cannot join waitlist twice."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "alice")
        system.join_waitlist("e1", "bob", 1)
        assert system.join_waitlist("e1", "bob", 2) is False

    def test_phase4_get_waitlist(self):
        """get_waitlist returns sorted list by priority."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "alice")
        system.join_waitlist("e1", "bob", 5)
        system.join_waitlist("e1", "charlie", 1)
        system.join_waitlist("e1", "dave", 3)

        waitlist = system.get_waitlist("e1")
        assert waitlist == [("charlie", 1), ("dave", 3), ("bob", 5)]

    def test_phase4_get_waitlist_fifo_same_priority(self):
        """Same priority users are ordered by insertion time."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "first")
        system.join_waitlist("e1", "second", 1)
        system.join_waitlist("e1", "third", 1)
        system.join_waitlist("e1", "fourth", 1)

        waitlist = system.get_waitlist("e1")
        assert waitlist == [("second", 1), ("third", 1), ("fourth", 1)]

    def test_phase4_get_waitlist_nonexistent(self):
        """get_waitlist returns None for nonexistent event."""
        system = EventBookingSystem()
        assert system.get_waitlist("fake") is None

    def test_phase4_leave_waitlist(self):
        """Can leave waitlist."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "alice")
        system.join_waitlist("e1", "bob", 1)
        assert system.leave_waitlist("e1", "bob") is True
        assert system.get_waitlist("e1") == []

    def test_phase4_leave_waitlist_not_on_list(self):
        """leave_waitlist returns False if not on waitlist."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        assert system.leave_waitlist("e1", "alice") is False

    def test_phase4_auto_promote_on_cancel(self):
        """Cancelling promotes highest priority from waitlist."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "alice")
        system.join_waitlist("e1", "bob", 5)
        system.join_waitlist("e1", "charlie", 1)  # Higher priority

        system.cancel("e1", "alice")

        bookings = system.get_bookings("e1")
        assert bookings == ["charlie"]

        waitlist = system.get_waitlist("e1")
        assert waitlist == [("bob", 5)]

    def test_phase4_auto_promote_respects_fifo(self):
        """Auto-promote uses FIFO for same priority."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.book("e1", "original")
        system.join_waitlist("e1", "first", 1)
        system.join_waitlist("e1", "second", 1)

        system.cancel("e1", "original")

        assert system.get_bookings("e1") == ["first"]
        assert system.get_waitlist("e1") == [("second", 1)]

    def test_phase4_skip_conflicting_waitlist_user(self):
        """Auto-promote skips users who now have conflicts."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.create_event("e2", 150, 250, 5)

        system.book("e1", "alice")
        system.join_waitlist("e1", "bob", 0)  # Highest priority
        system.join_waitlist("e1", "charlie", 1)

        # Bob gets a conflicting booking
        system.book("e2", "bob")

        # When alice cancels, bob should be skipped
        system.cancel("e1", "alice")

        bookings = system.get_bookings("e1")
        assert bookings == ["charlie"]

    def test_phase4_waitlist_with_conflicts(self):
        """Cannot join waitlist if would have time conflict."""
        system = EventBookingSystem()
        system.create_event("e1", 100, 200, 1)
        system.create_event("e2", 150, 250, 5)

        system.book("e1", "alice")  # e1 full
        system.book("e2", "bob")    # bob has [150,250) booked

        # Bob shouldn't be able to join e1's waitlist due to conflict
        assert system.join_waitlist("e1", "bob", 1) is False

    def test_phase4_complex_scenario(self):
        """Complex scenario with multiple operations."""
        system = EventBookingSystem()
        system.create_event("talk", 100, 200, 2)

        # Fill the event
        system.book("talk", "alice")
        system.book("talk", "bob")

        # Build waitlist
        system.join_waitlist("talk", "charlie", 3)
        system.join_waitlist("talk", "dave", 1)
        system.join_waitlist("talk", "eve", 2)

        # First cancellation promotes dave (priority 1)
        system.cancel("talk", "alice")
        assert "dave" in system.get_bookings("talk")

        # Second cancellation promotes eve (priority 2)
        system.cancel("talk", "bob")
        assert sorted(system.get_bookings("talk")) == ["dave", "eve"]

        # Only charlie left on waitlist
        assert system.get_waitlist("talk") == [("charlie", 3)]
