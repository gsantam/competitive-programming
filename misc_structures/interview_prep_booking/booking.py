"""
Event Booking System

Implement the EventBookingSystem class according to the requirements in README.md.
Progress through each phase, ensuring all tests pass before moving on.

Phase 1: Basic event creation and booking
Phase 2: Time conflict detection
Phase 3: Recurring events
Phase 4: Waitlist with priority-based promotion
"""


class EventBookingSystem:
    """
    An event booking system with conflict detection and waitlist support.

    Phase 1 - Basic Operations:
        - create_event(event_id: str, start: int, end: int, capacity: int) -> bool
        - book(event_id: str, user_id: str) -> bool
        - cancel(event_id: str, user_id: str) -> bool
        - get_bookings(event_id: str) -> list[str] | None

    Phase 2 - Conflict Detection:
        - book() now checks for time conflicts across events
        - get_user_schedule(user_id: str) -> list[tuple[int, int, str]]
        - find_conflicts(start: int, end: int, user_id: str) -> list[str]

    Phase 3 - Recurring Events:
        - create_recurring_event(event_id: str, start: int, end: int, capacity: int, interval: int, count: int) -> bool
        - get_occurrences(event_id: str) -> list[tuple[int, int]] | None
        - book_occurrence(event_id: str, occurrence_index: int, user_id: str) -> bool
        - cancel_occurrence(event_id: str, occurrence_index: int, user_id: str) -> bool

    Phase 4 - Waitlist:
        - join_waitlist(event_id: str, user_id: str, priority: int) -> bool
        - leave_waitlist(event_id: str, user_id: str) -> bool
        - get_waitlist(event_id: str) -> list[tuple[str, int]] | None
        - cancel() now auto-promotes from waitlist
    """

    def __init__(self):
        self.events = {}
        self.users = {}
        self.n_ocurrences = {}

    # ==================== PHASE 1 ====================

    def create_event(self, event_id: str, start: int, end: int, capacity: int) -> bool:
        """
        Create an event with given time range and capacity.
        Returns False if event_id already exists.
        """
        if event_id in self.events:
            return False
        self.events[event_id] = {"start": start, "end": end,
                                 "capacity": capacity, "users": set()}

        return True

    def book(self, event_id: str, user_id: str) -> bool:
        """
        Book a user for an event.
        Returns False if event doesn't exist, user already booked, or at capacity.
        In Phase 2+: Also returns False if user has time conflict.
        """
        if event_id not in self.events:
            return False
        if len(self.events[event_id]["users"]) >= self.events[event_id]["capacity"]:
            return False
        if user_id in self.events[event_id]["users"]:
            return False
        if user_id not in self.users:
            self.users[user_id] = {"events": set()}

        event_start = self.events[event_id]["start"]
        event_end = self.events[event_id]["end"]

        user_already_starts_ends = self.get_user_schedule(user_id)

        for user_already_start, user_already_end, _ in user_already_starts_ends:
            if event_end > user_already_start and event_start < user_already_end:
                return False

        self.users[user_id]["events"].add(event_id)
        self.events[event_id]["users"].add(user_id)
        return True

    def cancel(self, event_id: str, user_id: str) -> bool:
        """
        Cancel a user's booking.
        Returns False if event doesn't exist or user wasn't booked.
        In Phase 4: Auto-promotes highest priority user from waitlist.
        """
        if event_id not in self.events:
            return False
        if user_id not in self.events[event_id]["users"]:
            return False
        self.events[event_id]["users"].remove(user_id)
        self.users[user_id]["events"].remove(event_id)
        return True

    def get_bookings(self, event_id: str) -> list[str] | None:
        """
        Return list of user_ids booked for event.
        Returns None if event doesn't exist.
        """
        if event_id not in self.events:
            return None
        return list(self.events[event_id]["users"])

    # ==================== PHASE 2 ====================

    def get_user_schedule(self, user_id: str) -> list[tuple[int, int, str]]:
        """
        Return list of (start, end, event_id) tuples for all events
        the user is booked for, sorted by start time.
        """
        if user_id not in self.users:
            return []
        user_already_starts_ends = [(self.events[event_id]["start"], self.events[event_id]["end"], event_id)
                                    for event_id in self.users[user_id]["events"]]
        user_already_starts_ends = sorted(user_already_starts_ends)
        return user_already_starts_ends

    def find_conflicts(self, start: int, end: int, user_id: str) -> list[str]:
        """
        Return list of event_ids where user is booked that overlap
        with the given time range.
        """
        user_already_starts_ends = self.get_user_schedule(user_id)
        conflicts = []

        for user_already_start, user_already_end, event_id in user_already_starts_ends:
            if end > user_already_start and start < user_already_end:
                conflicts.append(event_id)
        return conflicts

    # ==================== PHASE 3 ====================

    def create_recurring_event(
        self, event_id: str, start: int, end: int,
        capacity: int, interval: int, count: int
    ) -> bool:
        """
        Create a recurring event that repeats count times with interval between starts.
        Returns False if event_id already exists.
        """
        if event_id in self.events:
            return False
        for i in range(count):
            if i == 0:
                self.create_event(event_id, start, end, capacity)
            else:
                self.create_event(event_id+"_"+str(i), start + interval *
                                  i, end+interval*i, capacity)
        self.n_ocurrences[event_id] = count
        return True

    def format_event_name(self, event_id, occurrance_index):
        if occurrance_index == 0:
            return event_id
        else:
            return event_id+"_"+str(occurrance_index)

    def get_occurrences(self, event_id: str) -> list[tuple[int, int]] | None:
        """
        Return list of (start, end) tuples for all occurrences.
        Returns None if event doesn't exist.
        For non-recurring events, returns single occurrence.
        """
        if event_id not in self.events:
            return None
        if event_id in self.n_ocurrences:
            n_ocurrences = self.n_ocurrences[event_id]
        else:
            n_ocurrences = 1
        all_ocurrences = []
        for i in range(n_ocurrences):
            event = self.events[self.format_event_name(event_id, i)]

            all_ocurrences.append((event["start"], event["end"]))
        return all_ocurrences

    def book_occurrence(self, event_id: str, occurrence_index: int, user_id: str) -> bool:
        """
        Book user for a specific occurrence of a recurring event.
        Returns False if event doesn't exist, invalid index, user already booked
        for this occurrence, occurrence at capacity, or time conflict.
        """
        return self.book(self.format_event_name(event_id, occurrence_index), user_id)

    def cancel_occurrence(self, event_id: str, occurrence_index: int, user_id: str) -> bool:
        """
        Cancel booking for specific occurrence.
        Returns False if event doesn't exist, invalid index, or user wasn't booked.
        """
        return self.cancel(self.format_event_name(
            event_id, occurrence_index), user_id)

    # ==================== PHASE 4 ====================

    def join_waitlist(self, event_id: str, user_id: str, priority: int) -> bool:
        """
        Add user to waitlist with priority (lower number = higher priority).
        Returns False if event doesn't exist, user already booked,
        already on waitlist, or has time conflict.
        """
        # TODO: Implement this
        raise NotImplementedError("Phase 4: Implement join_waitlist()")

    def leave_waitlist(self, event_id: str, user_id: str) -> bool:
        """
        Remove user from waitlist.
        Returns False if event doesn't exist or user not on waitlist.
        """
        # TODO: Implement this
        raise NotImplementedError("Phase 4: Implement leave_waitlist()")

    def get_waitlist(self, event_id: str) -> list[tuple[str, int]] | None:
        """
        Return waitlist as [(user_id, priority)] sorted by priority (ascending).
        Users with same priority are ordered by insertion time (FIFO).
        Returns None if event doesn't exist.
        """
        # TODO: Implement this
        raise NotImplementedError("Phase 4: Implement get_waitlist()")
