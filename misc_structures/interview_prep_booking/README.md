# Event Booking System - Interview Prep

This project simulates a coding interview where you build an event booking system with progressive requirements. Each phase introduces new constraints that may require refactoring your data structures.

**Time Target:** 90 minutes total  
**Language:** Python (standard library only)

---

## Phase 1: Basic Event Management (15-20 min)

Implement a simple event booking system:

| Method | Description |
|--------|-------------|
| `create_event(event_id: str, start: int, end: int, capacity: int) -> bool` | Create an event with given time range and capacity. Returns `False` if event_id already exists |
| `book(event_id: str, user_id: str) -> bool` | Book a user for an event. Returns `False` if event doesn't exist, user already booked, or at capacity |
| `cancel(event_id: str, user_id: str) -> bool` | Cancel a user's booking. Returns `False` if event doesn't exist or user wasn't booked |
| `get_bookings(event_id: str) -> list[str] \| None` | Return list of user_ids booked for event (order doesn't matter). Returns `None` if event doesn't exist |

**Notes:**
- `start` and `end` are integers representing time (e.g., minutes since midnight)
- `start < end` is guaranteed for valid inputs
- Event times can overlap in Phase 1

**Example:**
```python
system = EventBookingSystem()
system.create_event("meeting", 100, 200, 3)  # Returns True
system.book("meeting", "alice")               # Returns True
system.book("meeting", "bob")                 # Returns True
system.get_bookings("meeting")                # Returns ["alice", "bob"]
system.cancel("meeting", "alice")             # Returns True
system.get_bookings("meeting")                # Returns ["bob"]
```

---

## Phase 2: Time Conflict Detection (20-25 min)

Add the ability to prevent double-booking users and query available time slots:

| Method | Description |
|--------|-------------|
| `book(event_id: str, user_id: str) -> bool` | **Now also returns `False`** if the user is already booked for another event during overlapping time |
| `get_user_schedule(user_id: str) -> list[tuple[int, int, str]]` | Return list of (start, end, event_id) tuples for all events the user is booked for, sorted by start time |
| `find_conflicts(start: int, end: int, user_id: str) -> list[str]` | Return list of event_ids where user is booked that overlap with the given time range |

**Overlap Definition:** Two events overlap if one starts before the other ends, and ends after the other starts.  
Events `[100, 200)` and `[200, 300)` do **NOT** overlap (end-to-end is fine).

**Example:**
```python
system = EventBookingSystem()
system.create_event("e1", 100, 200, 5)
system.create_event("e2", 150, 250, 5)  # Overlaps with e1
system.create_event("e3", 300, 400, 5)  # No overlap

system.book("e1", "alice")               # True
system.book("e2", "alice")               # False - conflict with e1!
system.book("e3", "alice")               # True - no conflict
system.get_user_schedule("alice")        # [(100, 200, "e1"), (300, 400, "e3")]
system.find_conflicts(180, 350, "alice") # ["e1", "e3"]
```

---

## Phase 3: Recurring Events (25-30 min)

Add support for recurring events that repeat at regular intervals:

| Method | Description |
|--------|-------------|
| `create_recurring_event(event_id: str, start: int, end: int, capacity: int, interval: int, count: int) -> bool` | Create a recurring event that repeats `count` times with `interval` between starts |
| `get_occurrences(event_id: str) -> list[tuple[int, int]]` | Return list of (start, end) tuples for all occurrences of the event. Returns `None` if event doesn't exist |
| `book_occurrence(event_id: str, occurrence_index: int, user_id: str) -> bool` | Book user for a specific occurrence (0-indexed). Each occurrence has independent capacity |
| `cancel_occurrence(event_id: str, occurrence_index: int, user_id: str) -> bool` | Cancel booking for specific occurrence |

**Notes:**
- Regular `book()` and `cancel()` should still work for non-recurring events
- Conflict detection must work across all occurrences of recurring events
- `occurrence_index` must be valid (0 to count-1)

**Example:**
```python
system = EventBookingSystem()
# Weekly meeting: starts at 100, duration 50, repeats 3 times every 1000 time units
system.create_recurring_event("weekly", 100, 150, 2, 1000, 3)
# Creates occurrences: [100,150), [1100,1150), [2100,2150)

system.get_occurrences("weekly")  # [(100, 150), (1100, 1150), (2100, 2150)]

system.book_occurrence("weekly", 0, "alice")  # Book first occurrence
system.book_occurrence("weekly", 2, "alice")  # Book third occurrence

# Alice can't book something that conflicts with occurrence 0
system.create_event("conflict", 120, 180, 5)
system.book("conflict", "alice")  # False - conflicts with weekly occurrence 0
```

---

## Phase 4: Waitlist with Priority (20-25 min)

Add a waitlist system where users can queue for full events and get automatically promoted:

| Method | Description |
|--------|-------------|
| `join_waitlist(event_id: str, user_id: str, priority: int) -> bool` | Add user to waitlist with priority (lower = higher priority). Returns `False` if event doesn't exist, user already booked, or already on waitlist |
| `leave_waitlist(event_id: str, user_id: str) -> bool` | Remove user from waitlist. Returns `False` if not on waitlist |
| `get_waitlist(event_id: str) -> list[tuple[str, int]] \| None` | Return waitlist as [(user_id, priority)] sorted by priority (ascending). `None` if event doesn't exist |
| `cancel(event_id: str, user_id: str) -> bool` | **Enhanced:** When a booking is cancelled, automatically promote the highest-priority waitlisted user (if any) |

**Waitlist Rules:**
- Users can only be on waitlist if event is at capacity
- Users cannot be on waitlist if they're already booked or have a time conflict
- When promoted from waitlist, conflict check must still pass
- If promoted user would have a conflict, skip them and try next in priority order
- Users with same priority are ordered by insertion time (FIFO)

**Example:**
```python
system = EventBookingSystem()
system.create_event("talk", 100, 200, 1)
system.book("talk", "alice")              # True - gets the spot

system.join_waitlist("talk", "bob", 1)    # True - priority 1
system.join_waitlist("talk", "charlie", 0) # True - priority 0 (higher)
system.get_waitlist("talk")               # [("charlie", 0), ("bob", 1)]

system.cancel("talk", "alice")            # True - charlie gets promoted
system.get_bookings("talk")               # ["charlie"]
system.get_waitlist("talk")               # [("bob", 1)]
```

---

## Running Tests

```bash
# Run all tests
pytest test_booking.py -v

# Run specific phase
pytest test_booking.py -v -k "phase1"
pytest test_booking.py -v -k "phase2"
pytest test_booking.py -v -k "phase3"
pytest test_booking.py -v -k "phase4"
```

---

## Data Structure Hints

This problem is designed to make you think about data structure choices:

1. **Phase 1:** Simple dicts work fine
2. **Phase 2:** You need to efficiently query a user's time commitments. Consider what structures allow fast overlap detection
3. **Phase 3:** Recurring events add complexity - do you store all occurrences or compute them? How does this affect your Phase 2 structures?
4. **Phase 4:** Waitlist with priority + FIFO for ties requires careful structure choice. When a spot opens, you need the minimum priority efficiently

**Don't over-engineer early phases**, but be aware that Phase 2-4 will require refactoring if you don't plan ahead.
