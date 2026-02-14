"""
Library Management System

Implement the methods below to pass all tests across 4 levels.
See README.md for detailed requirements for each level.

Tips:
- Start with Level 1 and progress sequentially
- Later levels may require refactoring earlier code
- Use Python's standard library (datetime for date handling)
- Focus on correctness over code quality
"""
from datetime import datetime, timedelta


class LibrarySystem:
    """
    A library management system that handles books, users, checkouts,
    due dates, late fees, and reservations.
    """

    def __init__(self):
        """Initialize the library system."""
        self.books = {}
        self.users = {}

    # ==================== LEVEL 1: Basic Book Operations ====================

    def add_book(self, book_id: str, title: str) -> bool:
        """
        Add a book to the library.

        Args:
            book_id: Unique identifier for the book
            title: Title of the book

        Returns:
            True if book was added, False if book_id already exists
        """
        if book_id in self.books:
            return False
        self.books[book_id] = {"title": title,
                               "checkout": False, "waitlist": []}
        return True

    def remove_book(self, book_id: str) -> bool:
        """
        Remove a book from the library.

        Args:
            book_id: Unique identifier for the book

        Returns:
            True if book was removed, False if book doesn't exist
        """
        if book_id not in self.books:
            return False
        del self.books[book_id]
        return True

    def get_available_books(self) -> list:
        """
        Get all available (not checked out) books.

        Returns:
            List of book titles sorted alphabetically
        """
        return sorted([self.books[x]["title"] for x in self.books if not self.books[x]["checkout"]])

    # ==================== LEVEL 2: User Management ====================

    def register_user(self, user_id: str, name: str) -> bool:
        """
        Register a new user in the system.

        Args:
            user_id: Unique identifier for the user
            name: Name of the user

        Returns:
            True if user was registered, False if user_id already exists
        """
        if user_id in self.users:
            return False
        self.users[user_id] = {"name": name,
                               "books": dict(),
                               "reservations": set()}
        return True

    def get_user_books(self, user_id: str) -> list:
        """
        Get all books currently checked out by a user.

        Args:
            user_id: Unique identifier for the user

        Returns:
            List of book titles the user has checked out (sorted alphabetically),
            or empty list if user doesn't exist
        """
        if user_id not in self.users:
            return []
        user_books = []
        for book_id in self.users[user_id]["books"]:
            for log in self.users[user_id]["books"][book_id]:
                if "return_date" not in log:
                    user_books.append(self.books[book_id]["title"])
                    break

        return sorted(user_books)

    # ==================== LEVEL 1 & 2 & 3: Checkout/Return ====================
    # Note: These methods evolve across levels. Start with Level 1 signature,
    # then modify for Level 2 (add user_id), then Level 3 (add dates).

    def checkout_book(self, book_id: str, user_id: str = None, checkout_date: str = None) -> bool:
        """
        Check out a book from the library.

        Level 1: Only book_id is used
        Level 2: user_id is required
        Level 3: checkout_date is required (format: "YYYY-MM-DD")

        Args:
            book_id: Unique identifier for the book
            user_id: Unique identifier for the user (Level 2+)
            checkout_date: Date of checkout as string (Level 3+)

        Returns:
            True if checkout successful, False otherwise

        Failure conditions:
            - Book doesn't exist
            - Book is already checked out
            - User doesn't exist (Level 2+)
            - User has 3+ books checked out (Level 2+)
        """
        if book_id not in self.books:
            return False

        book = self.books[book_id]
        if book["checkout"]:
            return False

        if user_id:
            if user_id not in self.users:
                return False
            user = self.users[user_id]
            books_not_returned = sum(
                1 for book in user["books"] for log in user["books"][book] if "return_date" not in log)
            if books_not_returned >= 3:
                return False
            if book_id not in user["books"]:
                user["books"][book_id] = []
            user["books"][book_id].append({"checkout_date": checkout_date})
        book["checkout"] = True
        return True

    def return_book(self, book_id: str, user_id: str = None, return_date: str = None) -> bool:
        """
        Return a book to the library.

        Level 1: Only book_id is used
        Level 2: user_id is required
        Level 3: return_date is required (format: "YYYY-MM-DD")
        Level 4: Auto-assigns to waitlist if applicable

        Args:
            book_id: Unique identifier for the book
            user_id: Unique identifier for the user (Level 2+)
            return_date: Date of return as string (Level 3+)

        Returns:
            True if return successful, False otherwise

        Failure conditions:
            - Book doesn't exist
            - Book wasn't checked out
            - User doesn't have this book (Level 2+)
        """
        if book_id not in self.books:
            return False
        book = self.books[book_id]
        if not book["checkout"]:
            return False
        book["checkout"] = False
        if user_id:
            if user_id not in self.users:
                return False
            user = self.users[user_id]

            if book_id not in user["books"] or "return_date" in user["books"][book_id][-1]:
                return False

            user["books"][book_id][-1]["return_date"] = return_date
            for user_id_wt in self.books[book_id]["waitlist"]:
                try_check_out = self.checkout_book(
                    book_id, user_id_wt, return_date)
                if try_check_out:
                    self.cancel_reservation(book_id, user_id_wt)
                    break
        return True

    # ==================== LEVEL 3: Due Dates & Late Fees ====================

    def get_overdue_books(self, user_id: str, current_date: str) -> list:
        """
        Get all overdue books for a user.
        Books are due 14 days after checkout.

        Args:
            user_id: Unique identifier for the user
            current_date: Current date as string (format: "YYYY-MM-DD")

        Returns:
            List of overdue book titles (sorted alphabetically),
            or empty list if user doesn't exist
        """
        if user_id not in self.users:
            return []
        books = self.users[user_id]["books"]
        over_due_books = list()
        for book_id in books:
            for log in books[book_id]:
                if "return_date" not in log and datetime.strptime(current_date, '%Y-%m-%d').date() > datetime.strptime(log["checkout_date"], '%Y-%m-%d').date() + timedelta(days=14):
                    over_due_books.append(self.books[book_id]["title"])
        return sorted(over_due_books)

    def calculate_late_fees(self, user_id: str, current_date: str) -> float:
        """
        Calculate total late fees for a user.
        Fee is $0.25 per day overdue per book.
        Includes both currently overdue books and books returned late.

        Args:
            user_id: Unique identifier for the user
            current_date: Current date as string (format: "YYYY-MM-DD")

        Returns:
            Total late fees as float, or 0.0 if user doesn't exist
        """
        if user_id not in self.users:
            return 0
        books = self.users[user_id]["books"]
        total_fee = 0
        for book_id in books:
            for log in books[book_id]:
                if "return_date" in log:
                    total_fee += max((datetime.strptime(
                        log["return_date"], '%Y-%m-%d').date() - datetime.strptime(
                        log["checkout_date"], '%Y-%m-%d').date()).days-14, 0)*0.25
                else:
                    total_fee += max((datetime.strptime(
                        current_date, '%Y-%m-%d').date() - datetime.strptime(
                        log["checkout_date"], '%Y-%m-%d').date()).days-14, 0)*0.25
        return total_fee

    def get_borrowing_history(self, user_id: str) -> list:
        """
        Get complete borrowing history for a user.

        Args:
            user_id: Unique identifier for the user

        Returns:
            List of dicts with keys: book_id, title, checkout_date, return_date
            (return_date is None if book is still checked out)
            Ordered by checkout_date (oldest first)
            Returns empty list if user doesn't exist
        """

        if user_id not in self.users:
            return []
        borrowed_books = self.users[user_id]["books"]
        borrowing_history = []
        for book_id in borrowed_books:
            for borrow_entry in borrowed_books[book_id]:
                borrowing_history.append(
                    {"book_id": book_id, "title": self.books[book_id]["title"], "checkout_date": borrow_entry["checkout_date"], "return_date": borrow_entry["return_date"] if "return_date" in borrow_entry else None})
        return sorted(borrowing_history, key=lambda x: x['checkout_date'])

        # ==================== LEVEL 4: Reservations & Waitlist ====================

    def reserve_book(self, book_id: str, user_id: str) -> bool:

        if book_id not in self.books:
            return False
        book = self.books[book_id]
        if not book["checkout"]:
            return False
        if user_id not in self.users:
            return False

        if len(self.users[user_id]["reservations"]) >= 2:
            return False
        if book_id in self.users[user_id]["reservations"]:
            return False
        if self.books[book_id]["title"] in self.get_user_books(user_id):
            return False
        self.users[user_id]["reservations"].add(book_id)
        self.books[book_id]["waitlist"].append(user_id)
        return True

    def cancel_reservation(self, book_id: str, user_id: str) -> bool:
        if book_id not in self.books:
            return False
        book = self.books[book_id]
        if user_id not in self.users:
            return False
        if book_id not in self.users[user_id]["reservations"]:
            return False
        self.users[user_id]["reservations"].remove(book_id)
        for i in range(len(self.books[book_id]["waitlist"])):
            if self.books[book_id]["waitlist"][i] == user_id:
                del self.books[book_id]["waitlist"][i]
                break
        return True

    def get_waitlist(self, book_id: str) -> list:
        """
    Get the waitlist for a book.

    Args:
        book_id: Unique identifier for the book

    Returns:
        List of user names in waitlist order (FIFO),
        or empty list if book doesn't exist or no waitlist
    """
        if book_id not in self.books:
            return []
        return [self.users[user_id]["name"] for user_id in self.books[book_id]["waitlist"]]

    def get_user_reservations(self, user_id: str) -> list:
        """
    Get all active reservations for a user.

    Args:
        user_id: Unique identifier for the user

    Returns:
        List of book titles the user has reserved (sorted alphabetically),
        or empty list if user doesn't exist
    """
        if user_id not in self.users:
            return []

        return list(sorted([self.books[book_id]["title"] for book_id in self.users[user_id]["reservations"]]))
