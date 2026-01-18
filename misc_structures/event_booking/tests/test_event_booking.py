"""
Tests for Event Booking System - Coding Interview Practice

Run specific levels with:
    pytest tests/ -v -k "level1"
    pytest tests/ -v -k "level2"
    pytest tests/ -v -k "level3"
    pytest tests/ -v -k "level4"
"""

import pytest
from event_booking import EventBookingSystem


@pytest.fixture
def system():
    """Create a fresh EventBookingSystem for each test."""
    return EventBookingSystem()


# ==================== LEVEL 1: Basic Operations ====================


class TestLevel1BasicOperations:
    """Level 1: Basic CRUD operations for events and attendees."""

    def test_level1_create_event_success(self, system):
        """Can create a new event."""
        assert system.create_event("evt1", "Tech Conference") is True

    def test_level1_create_event_duplicate(self, system):
        """Cannot create duplicate events."""
        system.create_event("evt1", "Tech Conference")
        assert system.create_event("evt1", "Another Event") is False

    def test_level1_create_multiple_events(self, system):
        """Can create multiple different events."""
        assert system.create_event("evt1", "Conference") is True
        assert system.create_event("evt2", "Workshop") is True
        assert system.create_event("evt3", "Meetup") is True

    def test_level1_add_attendee_success(self, system):
        """Can add attendee to existing event."""
        system.create_event("evt1", "Conference")
        assert system.add_attendee("evt1", "user1", "Alice") is True

    def test_level1_add_attendee_nonexistent_event(self, system):
        """Cannot add attendee to non-existent event."""
        assert system.add_attendee("evt1", "user1", "Alice") is False

    def test_level1_add_attendee_update_name(self, system):
        """Adding same attendee again updates their name."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "user1", "Alice")
        assert system.add_attendee("evt1", "user1", "Alice Smith") is True
        assert system.get_attendee("evt1", "user1") == "Alice Smith"

    def test_level1_add_multiple_attendees(self, system):
        """Can add multiple attendees to an event."""
        system.create_event("evt1", "Conference")
        assert system.add_attendee("evt1", "user1", "Alice") is True
        assert system.add_attendee("evt1", "user2", "Bob") is True
        assert system.add_attendee("evt1", "user3", "Charlie") is True

    def test_level1_get_attendee_success(self, system):
        """Can get attendee name."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "user1", "Alice")
        assert system.get_attendee("evt1", "user1") == "Alice"

    def test_level1_get_attendee_nonexistent_event(self, system):
        """Get attendee returns None for non-existent event."""
        assert system.get_attendee("evt1", "user1") is None

    def test_level1_get_attendee_nonexistent_user(self, system):
        """Get attendee returns None for non-existent user."""
        system.create_event("evt1", "Conference")
        assert system.get_attendee("evt1", "user1") is None

    def test_level1_remove_attendee_success(self, system):
        """Can remove attendee."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "user1", "Alice")
        assert system.remove_attendee("evt1", "user1") is True
        assert system.get_attendee("evt1", "user1") is None

    def test_level1_remove_attendee_nonexistent_event(self, system):
        """Remove returns False for non-existent event."""
        assert system.remove_attendee("evt1", "user1") is False

    def test_level1_remove_attendee_nonexistent_user(self, system):
        """Remove returns False for non-existent user."""
        system.create_event("evt1", "Conference")
        assert system.remove_attendee("evt1", "user1") is False

    def test_level1_remove_and_readd_attendee(self, system):
        """Can re-add attendee after removal."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "user1", "Alice")
        system.remove_attendee("evt1", "user1")
        assert system.add_attendee("evt1", "user1", "Alice New") is True
        assert system.get_attendee("evt1", "user1") == "Alice New"


# ==================== LEVEL 2: Query Operations ====================


class TestLevel2QueryOperations:
    """Level 2: Search and listing capabilities."""

    def test_level2_list_attendees_empty_event(self, system):
        """List attendees returns empty list for event with no attendees."""
        system.create_event("evt1", "Conference")
        assert system.list_attendees("evt1") == []

    def test_level2_list_attendees_nonexistent_event(self, system):
        """List attendees returns empty list for non-existent event."""
        assert system.list_attendees("evt1") == []

    def test_level2_list_attendees_single(self, system):
        """List attendees with one attendee."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "user1", "Alice")
        assert system.list_attendees("evt1") == ["user1(Alice)"]

    def test_level2_list_attendees_multiple_sorted(self, system):
        """List attendees returns sorted by user_id."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "charlie", "Charlie Brown")
        system.add_attendee("evt1", "alice", "Alice Smith")
        system.add_attendee("evt1", "bob", "Bob Jones")
        assert system.list_attendees("evt1") == [
            "alice(Alice Smith)",
            "bob(Bob Jones)",
            "charlie(Charlie Brown)",
        ]

    def test_level2_list_attendees_format(self, system):
        """List attendees uses correct format."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "u1", "Name With Spaces")
        result = system.list_attendees("evt1")
        assert result == ["u1(Name With Spaces)"]

    def test_level2_list_by_prefix_empty(self, system):
        """List by prefix returns empty when no matches."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "alice", "Alice")
        assert system.list_attendees_by_prefix("evt1", "b") == []

    def test_level2_list_by_prefix_single_match(self, system):
        """List by prefix with single match."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "alice", "Alice")
        system.add_attendee("evt1", "bob", "Bob")
        assert system.list_attendees_by_prefix("evt1", "a") == ["alice(Alice)"]

    def test_level2_list_by_prefix_multiple_matches(self, system):
        """List by prefix with multiple matches, sorted."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "alex", "Alex")
        system.add_attendee("evt1", "alice", "Alice")
        system.add_attendee("evt1", "bob", "Bob")
        system.add_attendee("evt1", "amy", "Amy")
        result = system.list_attendees_by_prefix("evt1", "a")
        assert result == ["alex(Alex)", "alice(Alice)", "amy(Amy)"]

    def test_level2_list_by_prefix_exact_match(self, system):
        """List by prefix where prefix equals user_id."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "alice", "Alice")
        assert system.list_attendees_by_prefix(
            "evt1", "alice") == ["alice(Alice)"]

    def test_level2_list_by_prefix_nonexistent_event(self, system):
        """List by prefix returns empty for non-existent event."""
        assert system.list_attendees_by_prefix("evt1", "a") == []

    def test_level2_count_events_zero(self, system):
        """Count events returns 0 for user not in any events."""
        system.create_event("evt1", "Conference")
        assert system.count_events_for_user("user1") == 0

    def test_level2_count_events_single(self, system):
        """Count events for user in one event."""
        system.create_event("evt1", "Conference")
        system.add_attendee("evt1", "user1", "Alice")
        assert system.count_events_for_user("user1") == 1

    def test_level2_count_events_multiple(self, system):
        """Count events for user in multiple events."""
        system.create_event("evt1", "Conference")
        system.create_event("evt2", "Workshop")
        system.create_event("evt3", "Meetup")
        system.add_attendee("evt1", "user1", "Alice")
        system.add_attendee("evt2", "user1", "Alice")
        system.add_attendee("evt3", "user1", "Alice")
        assert system.count_events_for_user("user1") == 3

    def test_level2_count_events_after_removal(self, system):
        """Count events decreases after removal."""
        system.create_event("evt1", "Conference")
        system.create_event("evt2", "Workshop")
        system.add_attendee("evt1", "user1", "Alice")
        system.add_attendee("evt2", "user1", "Alice")
        assert system.count_events_for_user("user1") == 2
        system.remove_attendee("evt1", "user1")
        assert system.count_events_for_user("user1") == 1


# ==================== LEVEL 3: Time-Based Operations ====================


class TestLevel3TimeBasedOperations:
    """Level 3: Timestamp support and TTL for registrations."""

    def test_level3_add_attendee_at_basic(self, system):
        """Add attendee at timestamp works."""
        system.create_event("evt1", "Conference")
        assert system.add_attendee_at("evt1", "user1", "Alice", 100) is True
        assert system.get_attendee_at("evt1", "user1", 100) == "Alice"

    def test_level3_add_attendee_at_not_visible_before(self, system):
        """Attendee added at timestamp not visible before that time."""
        system.create_event("evt1", "Conference")
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        assert system.get_attendee_at("evt1", "user1", 99) is None
        assert system.get_attendee_at("evt1", "user1", 100) == "Alice"

    def test_level3_add_attendee_at_nonexistent_event(self, system):
        """Add attendee at returns False for non-existent event."""
        assert system.add_attendee_at("evt1", "user1", "Alice", 100) is False

    def test_level3_add_attendee_with_ttl_basic(self, system):
        """Attendee with TTL expires correctly."""
        system.create_event("evt1", "Conference")
        system.add_attendee_with_ttl("evt1", "user1", "Alice", 100, 50)
        # Valid during [100, 150)
        assert system.get_attendee_at("evt1", "user1", 99) is None
        assert system.get_attendee_at("evt1", "user1", 100) == "Alice"
        assert system.get_attendee_at("evt1", "user1", 149) == "Alice"
        assert system.get_attendee_at("evt1", "user1", 150) is None

    def test_level3_add_attendee_with_ttl_nonexistent_event(self, system):
        """Add attendee with TTL returns False for non-existent event."""
        assert system.add_attendee_with_ttl(
            "evt1", "user1", "Alice", 100, 50) is False

    def test_level3_remove_attendee_at(self, system):
        """Remove at timestamp works."""
        system.create_event("evt1", "Conference")
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        assert system.remove_attendee_at("evt1", "user1", 150) is True
        # Still visible before removal
        assert system.get_attendee_at("evt1", "user1", 149) == "Alice"
        # Not visible at or after removal
        assert system.get_attendee_at("evt1", "user1", 150) is None

    def test_level3_remove_attendee_at_nonexistent(self, system):
        """Remove at returns False when attendee doesn't exist at that time."""
        system.create_event("evt1", "Conference")
        assert system.remove_attendee_at("evt1", "user1", 100) is False

    def test_level3_get_attendee_at_multiple_updates(self, system):
        """Multiple updates to same attendee at different times."""
        system.create_event("evt1", "Conference")
        system.add_attendee_at("evt1", "user1", "Alice V1", 100)
        system.add_attendee_at("evt1", "user1", "Alice V2", 200)
        assert system.get_attendee_at("evt1", "user1", 99) is None
        assert system.get_attendee_at("evt1", "user1", 100) == "Alice V1"
        assert system.get_attendee_at("evt1", "user1", 199) == "Alice V1"
        assert system.get_attendee_at("evt1", "user1", 200) == "Alice V2"

    def test_level3_list_attendees_at(self, system):
        """List attendees at specific timestamp."""
        system.create_event("evt1", "Conference")
        system.add_attendee_at("evt1", "alice", "Alice", 100)
        system.add_attendee_at("evt1", "bob", "Bob", 150)
        assert system.list_attendees_at("evt1", 99) == []
        assert system.list_attendees_at("evt1", 100) == ["alice(Alice)"]
        assert system.list_attendees_at("evt1", 150) == [
            "alice(Alice)", "bob(Bob)"]

    def test_level3_list_attendees_at_with_ttl(self, system):
        """List attendees respects TTL expiration."""
        system.create_event("evt1", "Conference")
        system.add_attendee_with_ttl("evt1", "alice", "Alice", 100, 50)
        system.add_attendee_at("evt1", "bob", "Bob", 120)
        # At 100: only alice
        assert system.list_attendees_at("evt1", 100) == ["alice(Alice)"]
        # At 130: both
        assert system.list_attendees_at("evt1", 130) == [
            "alice(Alice)", "bob(Bob)"]
        # At 150: alice expired, only bob
        assert system.list_attendees_at("evt1", 150) == ["bob(Bob)"]

    def test_level3_list_attendees_at_with_removal(self, system):
        """List attendees respects removal timestamps."""
        system.create_event("evt1", "Conference")
        system.add_attendee_at("evt1", "alice", "Alice", 100)
        system.add_attendee_at("evt1", "bob", "Bob", 100)
        system.remove_attendee_at("evt1", "alice", 150)
        assert system.list_attendees_at("evt1", 149) == [
            "alice(Alice)", "bob(Bob)"]
        assert system.list_attendees_at("evt1", 150) == ["bob(Bob)"]

    def test_level3_list_by_prefix_at(self, system):
        """List by prefix at specific timestamp."""
        system.create_event("evt1", "Conference")
        system.add_attendee_at("evt1", "alice", "Alice", 100)
        system.add_attendee_at("evt1", "amy", "Amy", 100)
        system.add_attendee_at("evt1", "bob", "Bob", 100)
        system.add_attendee_at("evt1", "adam", "Adam", 150)
        result = system.list_attendees_by_prefix_at("evt1", "a", 100)
        assert result == ["alice(Alice)", "amy(Amy)"]
        result = system.list_attendees_by_prefix_at("evt1", "a", 150)
        assert result == ["adam(Adam)", "alice(Alice)", "amy(Amy)"]

    def test_level3_complex_timeline(self, system):
        """Complex scenario with multiple operations over time."""
        system.create_event("evt1", "Conference")
        # Alice joins at 100 with TTL 100 (valid until 200)
        system.add_attendee_with_ttl("evt1", "alice", "Alice", 100, 100)
        # Bob joins at 120 permanently
        system.add_attendee_at("evt1", "bob", "Bob", 120)
        # Charlie joins at 150 with TTL 30 (valid until 180)
        system.add_attendee_with_ttl("evt1", "charlie", "Charlie", 150, 30)
        # Bob leaves at 160
        system.remove_attendee_at("evt1", "bob", 160)

        # Check various timestamps
        assert system.list_attendees_at("evt1", 99) == []
        assert system.list_attendees_at("evt1", 100) == ["alice(Alice)"]
        assert system.list_attendees_at("evt1", 120) == [
            "alice(Alice)", "bob(Bob)"]
        assert system.list_attendees_at("evt1", 150) == [
            "alice(Alice)",
            "bob(Bob)",
            "charlie(Charlie)",
        ]
        assert system.list_attendees_at("evt1", 160) == [
            "alice(Alice)",
            "charlie(Charlie)",
        ]
        assert system.list_attendees_at("evt1", 180) == ["alice(Alice)"]
        assert system.list_attendees_at("evt1", 200) == []


# ==================== LEVEL 4: Capacity & Waitlist ====================


class TestLevel4CapacityAndWaitlist:
    """Level 4: Capacity limits and waitlist management."""

    def test_level4_set_capacity_basic(self, system):
        """Can set capacity for an event."""
        system.create_event("evt1", "Conference")
        assert system.set_capacity("evt1", 10, 100) is True
        assert system.get_capacity("evt1", 100) == 10

    def test_level4_set_capacity_nonexistent_event(self, system):
        """Set capacity returns False for non-existent event."""
        assert system.set_capacity("evt1", 10, 100) is False

    def test_level4_get_capacity_before_set(self, system):
        """Get capacity returns None before capacity is set."""
        system.create_event("evt1", "Conference")
        assert system.get_capacity("evt1", 100) is None

    def test_level4_get_capacity_at_different_times(self, system):
        """Capacity takes effect at set timestamp."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 10, 100)
        assert system.get_capacity("evt1", 99) is None
        assert system.get_capacity("evt1", 100) == 10
        assert system.get_capacity("evt1", 200) == 10

    def test_level4_capacity_update(self, system):
        """Can update capacity over time."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 10, 100)
        system.set_capacity("evt1", 20, 150)
        assert system.get_capacity("evt1", 100) == 10
        assert system.get_capacity("evt1", 149) == 10
        assert system.get_capacity("evt1", 150) == 20

    def test_level4_waitlist_when_full(self, system):
        """User goes to waitlist when event is full."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 2, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        system.add_attendee_at("evt1", "user2", "Bob", 100)
        # Event is now full, next person goes to waitlist
        system.add_attendee_at("evt1", "user3", "Charlie", 100)
        assert system.get_attendee_at("evt1", "user3", 100) is None
        assert system.get_waitlist_position("evt1", "user3", 100) == 1

    def test_level4_waitlist_position(self, system):
        """Waitlist maintains FIFO order."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 1, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)  # Gets in
        system.add_attendee_at("evt1", "user2", "Bob", 101)  # Waitlist #1
        system.add_attendee_at("evt1", "user3", "Charlie", 102)  # Waitlist #2
        system.add_attendee_at("evt1", "user4", "David", 103)  # Waitlist #3

        assert system.get_waitlist_position("evt1", "user2", 105) == 1
        assert system.get_waitlist_position("evt1", "user3", 105) == 2
        assert system.get_waitlist_position("evt1", "user4", 105) == 3

    def test_level4_waitlist_not_on_waitlist(self, system):
        """Get waitlist position returns None for user not on waitlist."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 2, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        assert system.get_waitlist_position("evt1", "user1", 100) is None

    def test_level4_get_waitlist(self, system):
        """Get full waitlist in order."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 1, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        system.add_attendee_at("evt1", "charlie", "Charlie", 101)
        system.add_attendee_at("evt1", "bob", "Bob", 102)
        waitlist = system.get_waitlist("evt1", 105)
        # FIFO order, not alphabetical
        assert waitlist == ["charlie(Charlie)", "bob(Bob)"]

    def test_level4_auto_promote_on_remove(self, system):
        """First waitlist person promoted when attendee leaves."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 1, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        system.add_attendee_at("evt1", "user2", "Bob", 101)  # Waitlist
        system.add_attendee_at("evt1", "user3", "Charlie", 102)  # Waitlist

        # Before removal
        assert system.get_attendee_at("evt1", "user1", 149) == "Alice"
        assert system.get_waitlist_position("evt1", "user2", 149) == 1

        # Remove user1
        system.remove_attendee_at("evt1", "user1", 150)

        # After removal: user2 promoted, user3 moves up
        assert system.get_attendee_at("evt1", "user1", 150) is None
        assert system.get_attendee_at("evt1", "user2", 150) == "Bob"
        assert system.get_waitlist_position("evt1", "user2", 150) is None
        assert system.get_waitlist_position("evt1", "user3", 150) == 1

    def test_level4_auto_promote_on_ttl_expiry(self, system):
        """Waitlist person promoted when attendee's TTL expires."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 1, 100)
        system.add_attendee_with_ttl("evt1", "user1", "Alice", 100, 50)
        system.add_attendee_at("evt1", "user2", "Bob", 101)  # Waitlist

        # Before expiry
        assert system.get_attendee_at("evt1", "user1", 149) == "Alice"
        assert system.get_waitlist_position("evt1", "user2", 149) == 1

        # At expiry: user1 gone, user2 promoted
        assert system.get_attendee_at("evt1", "user1", 150) is None
        assert system.get_attendee_at("evt1", "user2", 150) == "Bob"

    def test_level4_no_promote_when_empty_waitlist(self, system):
        """No error when spot opens but waitlist is empty."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 2, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        system.remove_attendee_at("evt1", "user1", 150)
        # Should not error, just have empty event
        assert system.list_attendees_at("evt1", 150) == []

    def test_level4_capacity_increase_promotes_multiple(self, system):
        """Increasing capacity promotes multiple from waitlist."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 1, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        system.add_attendee_at("evt1", "user2", "Bob", 101)
        system.add_attendee_at("evt1", "user3", "Charlie", 102)
        system.add_attendee_at("evt1", "user4", "David", 103)

        # Increase capacity from 1 to 3
        system.set_capacity("evt1", 3, 150)

        # user2 and user3 should be promoted
        assert system.get_attendee_at("evt1", "user2", 150) == "Bob"
        assert system.get_attendee_at("evt1", "user3", 150) == "Charlie"
        assert system.get_waitlist_position("evt1", "user4", 150) == 1

    def test_level4_complex_capacity_scenario(self, system):
        """Complex scenario with capacity, waitlist, TTL."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 2, 100)

        # Two attendees fill the event
        system.add_attendee_with_ttl(
            "evt1", "alice", "Alice", 100, 100)  # Expires at 200
        system.add_attendee_at("evt1", "bob", "Bob", 100)

        # Two more go to waitlist
        system.add_attendee_at("evt1", "charlie", "Charlie", 110)
        system.add_attendee_at("evt1", "david", "David", 120)

        # At 150: alice and bob in, charlie and david waitlisted
        assert len(system.list_attendees_at("evt1", 150)) == 2
        assert system.get_waitlist("evt1", 150) == [
            "charlie(Charlie)", "david(David)"]

        # At 200: alice expires, charlie promoted
        assert system.get_attendee_at("evt1", "alice", 200) is None
        assert system.get_attendee_at("evt1", "charlie", 200) == "Charlie"
        assert system.get_waitlist("evt1", 200) == ["david(David)"]

    def test_level4_waitlist_empty(self, system):
        """Get waitlist returns empty list when no waitlist."""
        system.create_event("evt1", "Conference")
        system.set_capacity("evt1", 10, 100)
        system.add_attendee_at("evt1", "user1", "Alice", 100)
        assert system.get_waitlist("evt1", 100) == []

    def test_level4_waitlist_nonexistent_event(self, system):
        """Get waitlist returns empty for non-existent event."""
        assert system.get_waitlist("evt1", 100) == []

    def test_level4_no_capacity_no_waitlist(self, system):
        """Without capacity set, no waitlist is used."""
        system.create_event("evt1", "Conference")
        # No capacity set, unlimited attendees
        for i in range(100):
            system.add_attendee_at("evt1", f"user{i}", f"User {i}", 100)
        assert len(system.list_attendees_at("evt1", 100)) == 100
        assert system.get_waitlist("evt1", 100) == []
