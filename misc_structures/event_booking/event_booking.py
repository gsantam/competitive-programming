"""
Event Booking System - Coding Interview Practice

Implement the methods below according to the specifications in README.md.
Progress through the 4 levels, implementing each set of methods.

Run tests with: pytest tests/ -v -k "levelX" (where X is 1-4)
"""


class EventBookingSystem:
    def __init__(self):
        self.events = {}
        self.internal_time = 10**5

    # ==================== LEVEL 1: Basic Operations ====================

    def create_event(self, event_id: str, name: str) -> bool:
        if event_id in self.events:
            return False
        self.events[event_id] = {"name": name,
                                 "attendants": {}, "capacities": []}
        return True

    def add_attendee(self, event_id: str, user_id: str, name: str) -> bool:
        self.internal_time += 1
        return self.add_attendee_at(event_id, user_id, name, self.internal_time)

    def get_attendee(self, event_id: str, user_id: str) -> str | None:
        self.internal_time += 1
        return self.get_attendee_at(event_id, user_id, self.internal_time)

    def remove_attendee(self, event_id: str, user_id: str) -> bool:
        self.internal_time += 1
        return self.remove_attendee_at(event_id, user_id, self.internal_time)

    # ==================== LEVEL 2: Query Operations ====================

    def list_attendees(self, event_id: str) -> list[str]:
        """
        Returns list of attendees formatted as ["user_id(name)", ...].
        Sorted lexicographically by user_id. Empty list if event doesn't exist.
        """
        self.internal_time += 1
        return self.list_attendees_at(event_id, self.internal_time)

    def list_attendees_by_prefix(self, event_id: str, prefix: str) -> list[str]:
        """
        Same as list_attendees but only includes user_ids starting with prefix.
        """
        self.internal_time += 1
        return self.list_attendees_by_prefix_at(event_id, prefix, self.internal_time)

    def count_events_for_user(self, user_id: str) -> int:
        """
        Returns the number of events the user is registered for.
        """
        self.internal_time += 1
        return self.count_events_for_user_at(user_id, self.internal_time)

    def count_events_for_user_at(self, user_id: str, timestamp: int):
        n_events = 0
        for event_id in self.events:
            exists, _ = self.exists_at_timestamp(event_id, user_id, timestamp)
            if exists:
                n_events += 1
        return n_events

    # ==================== LEVEL 3: Time-Based Operations ====================

    def add_attendee_at(
        self, event_id: str, user_id: str, name: str, timestamp: int, ttl: int = None
    ) -> bool:
        """
        Adds an attendee at a specific timestamp.
        Returns True if event exists, False otherwise.
        """
        if event_id not in self.events:
            return False
        if user_id not in self.events[event_id]["attendants"]:
            self.events[event_id]["attendants"][user_id] = []
        self.events[event_id]["attendants"][user_id].append(
            [timestamp, name, ttl, "add"])
        return True

    def add_attendee_with_ttl(
        self, event_id: str, user_id: str, name: str, timestamp: int, ttl: int
    ) -> bool:
        """
        Adds an attendee with a time-to-live. Registration valid during [timestamp, timestamp + ttl).
        Returns True if event exists, False otherwise.
        """
        return self.add_attendee_at(event_id, user_id, name, timestamp, ttl)

    def get_attendee_sorted_log(self, event_id, user_id):
        if event_id in self.events and user_id in self.events[event_id]["attendants"]:
            logs = self.events[event_id]["attendants"][user_id]
            logs = sorted(logs)
            return logs
        return None

    def exists_at_timestamp(self, event_id: str, user_id: str, at_timestamp):
        sorted_logs = self.get_attendee_sorted_log(event_id, user_id)
        if sorted_logs is None:
            return False, None
        if len(sorted_logs) == 0:
            return False, None
        for i in range(len(sorted_logs)):
            if at_timestamp >= sorted_logs[i][0] and (i == len(sorted_logs)-1 or at_timestamp < sorted_logs[i+1][0]):
                if sorted_logs[i][3] == "rem":
                    return False, None
                if sorted_logs[i][2] is None or (sorted_logs[i][0] + sorted_logs[i][2] > at_timestamp):
                    return True, sorted_logs[i]
        return False, None

    def exists_at_timestamp_as_not_in_waitlist(self, event_id: str, user_id: str, at_timestamp):
        exists, log = self.exists_at_timestamp(event_id, user_id, at_timestamp)
        list_position = self.get_waitlist_position(
            event_id, user_id, at_timestamp)
        if exists and list_position is None:
            return True, log
        return False, None

    def remove_attendee_at(
        self, event_id: str, user_id: str, timestamp: int
    ) -> bool:
        exists, log = self.exists_at_timestamp(event_id, user_id, timestamp)
        if exists:
            self.events[event_id]["attendants"][user_id].append(
                [timestamp, log[1], None, "rem"])
            return True
        return False

    def get_attendee_at(
        self, event_id: str, user_id: str, timestamp: int
    ) -> str | None:
        exists, log = self.exists_at_timestamp_as_not_in_waitlist(
            event_id, user_id, timestamp)
        if exists:
            return log[1]

        return None

    def list_attendees_at(self, event_id: str, timestamp: int) -> list[str]:
        """
        Lists attendees at a specific timestamp.
        Formatted and sorted same as list_attendees.
        """
        return self.list_attendees_by_prefix_at(event_id, "", timestamp)

    def list_attendees_by_prefix_at(
        self, event_id: str, prefix: str, timestamp: int
    ) -> list[str]:
        """
        Lists attendees with prefix at a specific timestamp.
        """
        if event_id in self.events:
            attendants_data = self.events[event_id]["attendants"]
            user_id = [user_id for user_id in attendants_data.keys()
                       if user_id.startswith(prefix)]
            user_id_sorted = sorted(user_id)
            attendees_formated = []
            for user_id in user_id_sorted:
                exists, log = self.exists_at_timestamp_as_not_in_waitlist(
                    event_id, user_id, timestamp)
                if exists:
                    attendees_formated.append(
                        f"{user_id}({log[1]})"
                    )
            return attendees_formated

        return []

    # ==================== LEVEL 4: Capacity & Waitlist ====================

    def set_capacity(self, event_id: str, capacity: int, timestamp: int) -> bool:
        if event_id not in self.events:
            return False
        self.events[event_id]["capacities"].append([timestamp, capacity])
        return True

    def get_capacity(self, event_id: str, timestamp: int) -> int | None:
        """
        Returns capacity at timestamp, or None if not set/event doesn't exist.
        """
        if event_id not in self.events:
            return None
        sorted_capacities = sorted(self.events[event_id]["capacities"])
        if len(sorted_capacities) == 0 or timestamp < sorted_capacities[0][0]:
            return None
        for i in range(len(sorted_capacities)):
            if timestamp >= sorted_capacities[i][0] and (i == len(sorted_capacities)-1 or timestamp < sorted_capacities[i+1][0]):
                return sorted_capacities[i][1]
        return sorted_capacities[-1][1]

    def get_waitlist_helper(self, event_id: str, timestamp: int):
        user_logs = []
        for user_id_ in self.events[event_id]["attendants"]:
            exists, log = self.exists_at_timestamp(
                event_id, user_id_, timestamp)
            if exists:
                user_logs.append([log[0], user_id_, log[1]])
        user_logs = sorted(user_logs)
        return user_logs

    def get_waitlist_position(
        self, event_id: str, user_id: str, timestamp: int
    ) -> int | None:
        """
        Returns 1-indexed waitlist position, or None if not on waitlist.
        """
        if not self.exists_at_timestamp(event_id, user_id, timestamp)[0]:
            return None
        capacity = self.get_capacity(event_id, timestamp)
        if capacity is None:
            return None
        user_logs = self.get_waitlist_helper(event_id, timestamp)
        for log in user_logs:
            if log[1] == user_id:
                break
            capacity -= 1
        if capacity > 0:
            return None
        return -capacity+1

    def get_waitlist(self, event_id: str, timestamp: int) -> list[str]:
        if event_id not in self.events:
            return []
        user_logs = self.get_waitlist_helper(event_id, timestamp)
        capacity = self.get_capacity(event_id, timestamp)
        if capacity is None:
            return []
        in_waiting_list = []
        for log in user_logs:
            if capacity <= 0:
                in_waiting_list.append(f"{log[1]}({log[2]})")
            capacity -= 1
        return in_waiting_list
