# CodeSignal Interview Preparation - Library Management System

A practice project simulating the CodeSignal coding assessment format. This project involves implementing a library management system across 4 levels of increasing complexity, focusing on refactoring and adapting to new requirements.

## Overview

- **Time Target:** 90 minutes for all 4 levels
- **Language:** Python (standard library only)
- **Testing:** pytest
- **Focus:** Quick, correct implementation; code quality is not evaluated

## How to Use

1. Implement the methods in `library_system.py`
2. Run tests for each level: `pytest test_library_system.py -v -k "level1"`
3. Progress to the next level only after passing all tests in the current level
4. Later levels build on earlier ones and may require refactoring

## Running Tests

```bash
# Run all tests
pytest test_library_system.py -v

# Run tests for a specific level
pytest test_library_system.py -v -k "level1"
pytest test_library_system.py -v -k "level2"
pytest test_library_system.py -v -k "level3"
pytest test_library_system.py -v -k "level4"
```

---

## Level 1: Basic Book Operations (Estimated: 15 minutes)

Implement a basic library system that can manage books.

### Requirements

1. **Add books** to the library with a unique `book_id` and `title`
2. **Remove books** from the library by `book_id`
3. **Check out books** - mark a book as checked out (returns `True` if successful, `False` if book doesn't exist or is already checked out)
4. **Return books** - mark a book as available (returns `True` if successful, `False` if book doesn't exist or wasn't checked out)
5. **Get available books** - return a list of all available book titles (sorted alphabetically)

### Methods to Implement

- `add_book(book_id: str, title: str) -> bool`
- `remove_book(book_id: str) -> bool`
- `checkout_book(book_id: str) -> bool`
- `return_book(book_id: str) -> bool`
- `get_available_books() -> list[str]`

---

## Level 2: User Management (Estimated: 20 minutes)

Extend the system to track users and enforce borrowing limits.

### New Requirements

1. **Register users** with a unique `user_id` and `name`
2. **Track which user** has checked out which book
3. **Enforce borrowing limit** - users can have at most 3 books checked out at a time
4. **Get user's books** - return list of book titles a user currently has

### Methods to Implement/Modify

- `register_user(user_id: str, name: str) -> bool`
- `checkout_book(book_id: str, user_id: str) -> bool` (modified signature)
- `return_book(book_id: str, user_id: str) -> bool` (modified signature)
- `get_user_books(user_id: str) -> list[str]`

### Constraints

- Checkout fails if user doesn't exist, book doesn't exist, book is already out, or user has 3+ books
- Return fails if user doesn't have that specific book

---

## Level 3: Due Dates & Late Fees (Estimated: 25 minutes)

Add time-based tracking with due dates and late fee calculations.

### New Requirements

1. **Due dates** - books are due 14 days after checkout
2. **Check overdue books** - get list of overdue books for a user
3. **Calculate late fees** - $0.25 per day overdue per book
4. **Borrowing history** - track all past and current borrowings

### Methods to Implement

- `checkout_book(book_id: str, user_id: str, checkout_date: str) -> bool` (modified - date format: "YYYY-MM-DD")
- `return_book(book_id: str, user_id: str, return_date: str) -> bool` (modified)
- `get_overdue_books(user_id: str, current_date: str) -> list[str]`
- `calculate_late_fees(user_id: str, current_date: str) -> float`
- `get_borrowing_history(user_id: str) -> list[dict]` (returns list of {book_id, title, checkout_date, return_date or None})

### Constraints

- Late fees only apply to books that have been returned late OR are currently overdue
- History should be ordered by checkout date (oldest first)

---

## Level 4: Reservations & Waitlist (Estimated: 30 minutes)

Add a reservation system for books that are currently checked out.

### New Requirements

1. **Reserve books** - users can reserve a book that's currently checked out
2. **Waitlist management** - multiple users can reserve the same book (FIFO order)
3. **Auto-assignment** - when a book is returned, it's automatically assigned to the first person in the waitlist
4. **Reservation limits** - users can have at most 2 active reservations
5. **Cancel reservations** - users can cancel their reservations

### Methods to Implement

- `reserve_book(book_id: str, user_id: str) -> bool`
- `cancel_reservation(book_id: str, user_id: str) -> bool`
- `get_waitlist(book_id: str) -> list[str]` (returns list of user names in order)
- `get_user_reservations(user_id: str) -> list[str]` (returns list of book titles)
- `return_book(...)` - modified to handle auto-assignment to waitlist

### Constraints

- Cannot reserve a book that's available
- Cannot reserve a book you already have checked out
- Cannot reserve a book you already have reserved
- When auto-assigned, the reservation is removed and counts toward the user's checkout limit
- If the first person in waitlist has 3 books, skip to next person

---

## Tips

1. **Start simple** - get Level 1 working before adding complexity
2. **Refactor as needed** - later levels may require restructuring your data
3. **Read requirements carefully** - edge cases matter
4. **Use Python's standard library** - `datetime` for date handling
5. **Don't over-engineer** - focus on passing tests, not perfect code

Good luck! 🚀
