# Event Booking System - Coding Interview Practice

## Overview

This is a practice coding interview similar to the Anthropic CodeSignal assessment. You'll implement a simple event booking system with 4 levels of increasing complexity. The system manages events, attendees, and their registrations.

**Time Limit:** 90 minutes (simulating the real test)

**Goal:** Progress through all 4 levels, passing all tests at each level before moving to the next.

---

## Level 1: Basic Event Operations

Implement fundamental CRUD operations for events and attendees.

### Methods to Implement:

- **`create_event(event_id: str, name: str) -> bool`**  
  Creates a new event with the given ID and name. Returns `True` if successful, `False` if an event with that ID already exists.

- **`add_attendee(event_id: str, user_id: str, name: str) -> bool`**  
  Adds an attendee to an event. If the attendee already exists for this event, update their name. Returns `True` if the event exists, `False` otherwise.

- **`get_attendee(event_id: str, user_id: str) -> str | None`**  
  Returns the name of the attendee with the given user_id at the specified event. Returns `None` if the event or attendee doesn't exist.

- **`remove_attendee(event_id: str, user_id: str) -> bool`**  
  Removes an attendee from an event. Returns `True` if the attendee was successfully removed, `False` if the event or attendee doesn't exist.

---

## Level 2: Query Operations

Add search and listing capabilities.

### Methods to Implement:

- **`list_attendees(event_id: str) -> list[str]`**  
  Returns a list of strings in the format `["<user_id1>(<name1>)", "<user_id2>(<name2>)", ...]` for all attendees of an event. The list should be sorted lexicographically by user_id. Returns an empty list if the event doesn't exist or has no attendees.

- **`list_attendees_by_prefix(event_id: str, prefix: str) -> list[str]`**  
  Same as `list_attendees`, but only includes attendees whose user_id starts with the given prefix.

- **`count_events_for_user(user_id: str) -> int`**  
  Returns the number of events the user is currently registered for.

---

## Level 3: Time-Based Operations

Add timestamp support for all operations, enabling point-in-time queries and TTL (Time-To-Live) for registrations.

### Important Notes:
- All timestamps are integers representing time units.
- Operations at a timestamp affect the state from that timestamp forward.
- TTL means the registration is valid during the interval `[timestamp, timestamp + ttl)`.
- A registration expires at exactly `timestamp + ttl` (not available at that time).

### Methods to Implement:

- **`add_attendee_at(event_id: str, user_id: str, name: str, timestamp: int) -> bool`**  
  Same as `add_attendee`, but the registration takes effect at the given timestamp.

- **`add_attendee_with_ttl(event_id: str, user_id: str, name: str, timestamp: int, ttl: int) -> bool`**  
  Same as `add_attendee_at`, but the registration automatically expires after `ttl` time units. The attendee is valid during `[timestamp, timestamp + ttl)`.

- **`remove_attendee_at(event_id: str, user_id: str, timestamp: int) -> bool`**  
  Same as `remove_attendee`, but the removal takes effect at the given timestamp.

- **`get_attendee_at(event_id: str, user_id: str, timestamp: int) -> str | None`**  
  Same as `get_attendee`, but returns the state at the specified timestamp.

- **`list_attendees_at(event_id: str, timestamp: int) -> list[str]`**  
  Same as `list_attendees`, but returns the state at the specified timestamp.

- **`list_attendees_by_prefix_at(event_id: str, prefix: str, timestamp: int) -> list[str]`**  
  Same as `list_attendees_by_prefix`, but returns the state at the specified timestamp.

---

## Level 4: Capacity and Waitlist Management

Add capacity limits and automatic waitlist management.

### Important Notes:
- When capacity is set and the event is full, new registrations go to the waitlist.
- When an attendee is removed (or their registration expires), the first person on the waitlist is automatically promoted.
- Waitlist is ordered by the timestamp when the user was added to it (FIFO).
- Promoted attendees inherit the TTL behavior: if they were added with TTL, their TTL countdown starts when promoted.

### Methods to Implement:

- **`set_capacity(event_id: str, capacity: int, timestamp: int) -> bool`**  
  Sets the maximum number of attendees for an event starting at the given timestamp. If current attendees exceed capacity, no one is removed, but no new direct registrations are allowed until count drops below capacity. Returns `True` if the event exists, `False` otherwise.

- **`get_waitlist_position(event_id: str, user_id: str, timestamp: int) -> int | None`**  
  Returns the position (1-indexed) of the user in the waitlist at the given timestamp. Returns `None` if the user is not on the waitlist or the event doesn't exist.

- **`get_waitlist(event_id: str, timestamp: int) -> list[str]`**  
  Returns the waitlist in order, formatted as `["<user_id1>(<name1>)", ...]`. Returns an empty list if no waitlist exists.

- **`get_capacity(event_id: str, timestamp: int) -> int | None`**  
  Returns the current capacity of the event at the timestamp. Returns `None` if no capacity is set or event doesn't exist.

---

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests for a specific level
pytest tests/ -v -k "level1"
pytest tests/ -v -k "level2"
pytest tests/ -v -k "level3"
pytest tests/ -v -k "level4"
```

## Tips

1. **Start simple:** Get Level 1 working before worrying about timestamps.
2. **Refactor incrementally:** Level 3 builds on Level 1-2, so design with extension in mind.
3. **Test as you go:** Run the tests for each level before moving on.
4. **Time management:** If stuck on a level, move on and return later if time permits.
5. **Edge cases:** Pay attention to the return values (bool, None, empty list, etc.).

Good luck! 🚀
