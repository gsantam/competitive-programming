"""
Test suite for Library Management System.

Run with: pytest test_library_system.py -v
Run specific level: pytest test_library_system.py -v -k "level1"
"""

import pytest
from library_system import LibrarySystem


# ==================== LEVEL 1: Basic Book Operations ====================

class TestLevel1AddBook:
    """Tests for add_book functionality."""

    def test_level1_add_single_book(self):
        lib = LibrarySystem()
        assert lib.add_book("B001", "The Great Gatsby") is True

    def test_level1_add_multiple_books(self):
        lib = LibrarySystem()
        assert lib.add_book("B001", "The Great Gatsby") is True
        assert lib.add_book("B002", "1984") is True
        assert lib.add_book("B003", "Pride and Prejudice") is True

    def test_level1_add_duplicate_book_id(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.add_book("B001", "Different Title") is False

    def test_level1_add_same_title_different_id(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.add_book("B002", "The Great Gatsby") is True


class TestLevel1RemoveBook:
    """Tests for remove_book functionality."""

    def test_level1_remove_existing_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.remove_book("B001") is True

    def test_level1_remove_nonexistent_book(self):
        lib = LibrarySystem()
        assert lib.remove_book("B999") is False

    def test_level1_remove_already_removed_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.remove_book("B001")
        assert lib.remove_book("B001") is False


class TestLevel1CheckoutBook:
    """Tests for checkout_book functionality (Level 1 - no user)."""

    def test_level1_checkout_available_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.checkout_book("B001") is True

    def test_level1_checkout_nonexistent_book(self):
        lib = LibrarySystem()
        assert lib.checkout_book("B999") is False

    def test_level1_checkout_already_checked_out(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.checkout_book("B001")
        assert lib.checkout_book("B001") is False


class TestLevel1ReturnBook:
    """Tests for return_book functionality (Level 1 - no user)."""

    def test_level1_return_checked_out_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.checkout_book("B001")
        assert lib.return_book("B001") is True

    def test_level1_return_nonexistent_book(self):
        lib = LibrarySystem()
        assert lib.return_book("B999") is False

    def test_level1_return_available_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.return_book("B001") is False

    def test_level1_checkout_after_return(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.checkout_book("B001")
        lib.return_book("B001")
        assert lib.checkout_book("B001") is True


class TestLevel1GetAvailableBooks:
    """Tests for get_available_books functionality."""

    def test_level1_available_books_empty_library(self):
        lib = LibrarySystem()
        assert lib.get_available_books() == []

    def test_level1_available_books_all_available(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Zebra Stories")
        lib.add_book("B002", "Apple Tales")
        lib.add_book("B003", "Mango Adventures")
        assert lib.get_available_books() == [
            "Apple Tales", "Mango Adventures", "Zebra Stories"]

    def test_level1_available_books_some_checked_out(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Zebra Stories")
        lib.add_book("B002", "Apple Tales")
        lib.add_book("B003", "Mango Adventures")
        lib.checkout_book("B002")
        assert lib.get_available_books() == [
            "Mango Adventures", "Zebra Stories"]

    def test_level1_available_books_after_return(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.checkout_book("B001")
        lib.return_book("B001")
        assert lib.get_available_books() == ["The Great Gatsby"]


# ==================== LEVEL 2: User Management ====================

class TestLevel2RegisterUser:
    """Tests for register_user functionality."""

    def test_level2_register_single_user(self):
        lib = LibrarySystem()
        assert lib.register_user("U001", "Alice") is True

    def test_level2_register_multiple_users(self):
        lib = LibrarySystem()
        assert lib.register_user("U001", "Alice") is True
        assert lib.register_user("U002", "Bob") is True
        assert lib.register_user("U003", "Charlie") is True

    def test_level2_register_duplicate_user_id(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        assert lib.register_user("U001", "Different Name") is False


class TestLevel2CheckoutWithUser:
    """Tests for checkout_book with user_id."""

    def test_level2_checkout_valid_user_and_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        assert lib.checkout_book("B001", "U001") is True

    def test_level2_checkout_nonexistent_user(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.checkout_book("B001", "U999") is False

    def test_level2_checkout_nonexistent_book(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        assert lib.checkout_book("B999", "U001") is False

    def test_level2_checkout_limit_three_books(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.add_book("B003", "Book 3")
        lib.add_book("B004", "Book 4")

        lib.checkout_book("B001", "U001")
        lib.checkout_book("B002", "U001")
        lib.checkout_book("B003", "U001")
        assert lib.checkout_book("B004", "U001") is False

    def test_level2_checkout_after_return_within_limit(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.add_book("B003", "Book 3")
        lib.add_book("B004", "Book 4")

        lib.checkout_book("B001", "U001")
        lib.checkout_book("B002", "U001")
        lib.checkout_book("B003", "U001")
        lib.return_book("B001", "U001")
        assert lib.checkout_book("B004", "U001") is True


class TestLevel2ReturnWithUser:
    """Tests for return_book with user_id."""

    def test_level2_return_own_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001")
        assert lib.return_book("B001", "U001") is True

    def test_level2_return_others_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001")
        assert lib.return_book("B001", "U002") is False

    def test_level2_return_nonexistent_user(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001")
        assert lib.return_book("B001", "U999") is False


class TestLevel2GetUserBooks:
    """Tests for get_user_books functionality."""

    def test_level2_get_user_books_empty(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        assert lib.get_user_books("U001") == []

    def test_level2_get_user_books_multiple(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        lib.add_book("B001", "Zebra Stories")
        lib.add_book("B002", "Apple Tales")
        lib.checkout_book("B001", "U001")
        lib.checkout_book("B002", "U001")
        assert lib.get_user_books("U001") == ["Apple Tales", "Zebra Stories"]

    def test_level2_get_user_books_nonexistent_user(self):
        lib = LibrarySystem()
        assert lib.get_user_books("U999") == []

    def test_level2_get_user_books_after_return(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        lib.add_book("B001", "The Great Gatsby")
        lib.checkout_book("B001", "U001")
        lib.return_book("B001", "U001")
        assert lib.get_user_books("U001") == []


# ==================== LEVEL 3: Due Dates & Late Fees ====================

class TestLevel3CheckoutWithDate:
    """Tests for checkout_book with date."""

    def test_level3_checkout_with_date(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        assert lib.checkout_book("B001", "U001", "2024-01-01") is True

    def test_level3_checkout_multiple_dates(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-05")
        assert lib.get_user_books("U001") == ["Book 1", "Book 2"]


class TestLevel3ReturnWithDate:
    """Tests for return_book with date."""

    def test_level3_return_with_date(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        assert lib.return_book("B001", "U001", "2024-01-10") is True


class TestLevel3OverdueBooks:
    """Tests for get_overdue_books functionality."""

    def test_level3_no_overdue_books(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        # Day 14 is still on time
        assert lib.get_overdue_books("U001", "2024-01-15") == []

    def test_level3_one_overdue_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        # Day 15 is overdue (due on day 14)
        assert lib.get_overdue_books(
            "U001", "2024-01-16") == ["The Great Gatsby"]

    def test_level3_multiple_overdue_books(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Zebra Stories")
        lib.add_book("B002", "Apple Tales")
        lib.add_book("B003", "Mango Adventures")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-01")
        lib.checkout_book("B003", "U001", "2024-01-10")
        # B001 and B002 overdue, B003 not overdue
        assert lib.get_overdue_books(
            "U001", "2024-01-20") == ["Apple Tales", "Zebra Stories"]

    def test_level3_overdue_books_nonexistent_user(self):
        lib = LibrarySystem()
        assert lib.get_overdue_books("U999", "2024-01-20") == []

    def test_level3_overdue_books_after_return(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.return_book("B001", "U001", "2024-01-20")  # Returned late
        assert lib.get_overdue_books("U001", "2024-01-25") == []


class TestLevel3LateFees:
    """Tests for calculate_late_fees functionality."""

    def test_level3_no_late_fees(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        assert lib.calculate_late_fees("U001", "2024-01-15") == 0.0

    def test_level3_late_fee_one_day(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        # Due on Jan 15, checking on Jan 16 = 1 day late
        assert lib.calculate_late_fees("U001", "2024-01-16") == 0.25

    def test_level3_late_fee_multiple_days(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        # Due on Jan 15, checking on Jan 20 = 5 days late
        assert lib.calculate_late_fees("U001", "2024-01-20") == 1.25

    def test_level3_late_fee_multiple_books(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-01")
        # Both due on Jan 15, checking on Jan 17 = 2 days late each
        assert lib.calculate_late_fees("U001", "2024-01-17") == 1.0

    def test_level3_late_fee_returned_late(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.return_book("B001", "U001", "2024-01-20")  # 5 days late
        # Fee should still be calculated for returned late book
        assert lib.calculate_late_fees("U001", "2024-01-25") == 1.25

    def test_level3_late_fee_nonexistent_user(self):
        lib = LibrarySystem()
        assert lib.calculate_late_fees("U999", "2024-01-20") == 0.0


class TestLevel3BorrowingHistory:
    """Tests for get_borrowing_history functionality."""

    def test_level3_empty_history(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        assert lib.get_borrowing_history("U001") == []

    def test_level3_history_current_checkout(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        history = lib.get_borrowing_history("U001")
        assert len(history) == 1
        assert history[0]["book_id"] == "B001"
        assert history[0]["title"] == "The Great Gatsby"
        assert history[0]["checkout_date"] == "2024-01-01"
        assert history[0]["return_date"] is None

    def test_level3_history_returned_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.return_book("B001", "U001", "2024-01-10")
        history = lib.get_borrowing_history("U001")
        assert len(history) == 1
        assert history[0]["return_date"] == "2024-01-10"

    def test_level3_history_multiple_ordered(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.add_book("B003", "Book 3")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B002", "U001", "2024-01-05")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B003", "U001", "2024-01-10")
        history = lib.get_borrowing_history("U001")
        assert len(history) == 3
        assert history[0]["checkout_date"] == "2024-01-01"
        assert history[1]["checkout_date"] == "2024-01-05"
        assert history[2]["checkout_date"] == "2024-01-10"

    def test_level3_history_nonexistent_user(self):
        lib = LibrarySystem()
        assert lib.get_borrowing_history("U999") == []


# ==================== LEVEL 4: Reservations & Waitlist ====================

class TestLevel4ReserveBook:
    """Tests for reserve_book functionality."""

    def test_level4_reserve_checked_out_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        assert lib.reserve_book("B001", "U002") is True

    def test_level4_reserve_available_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        assert lib.reserve_book("B001", "U001") is False

    def test_level4_reserve_own_checked_out_book(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        assert lib.reserve_book("B001", "U001") is False

    def test_level4_reserve_already_reserved(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        assert lib.reserve_book("B001", "U002") is False

    def test_level4_reserve_limit_two(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.add_book("B003", "Book 3")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-01")
        lib.checkout_book("B003", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B002", "U002")
        assert lib.reserve_book("B003", "U002") is False

    def test_level4_reserve_nonexistent_book(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        assert lib.reserve_book("B999", "U001") is False

    def test_level4_reserve_nonexistent_user(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        assert lib.reserve_book("B001", "U999") is False


class TestLevel4CancelReservation:
    """Tests for cancel_reservation functionality."""

    def test_level4_cancel_existing_reservation(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        assert lib.cancel_reservation("B001", "U002") is True

    def test_level4_cancel_nonexistent_reservation(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        assert lib.cancel_reservation("B001", "U001") is False

    def test_level4_reserve_after_cancel(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.add_book("B003", "Book 3")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-01")
        lib.checkout_book("B003", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B002", "U002")
        lib.cancel_reservation("B001", "U002")
        assert lib.reserve_book("B003", "U002") is True


class TestLevel4GetWaitlist:
    """Tests for get_waitlist functionality."""

    def test_level4_empty_waitlist(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        assert lib.get_waitlist("B001") == []

    def test_level4_waitlist_order(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.register_user("U003", "Charlie")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B001", "U003")
        assert lib.get_waitlist("B001") == ["Bob", "Charlie"]

    def test_level4_waitlist_nonexistent_book(self):
        lib = LibrarySystem()
        assert lib.get_waitlist("B999") == []


class TestLevel4GetUserReservations:
    """Tests for get_user_reservations functionality."""

    def test_level4_no_reservations(self):
        lib = LibrarySystem()
        lib.register_user("U001", "Alice")
        assert lib.get_user_reservations("U001") == []

    def test_level4_multiple_reservations(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Zebra Stories")
        lib.add_book("B002", "Apple Tales")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B002", "U002")
        assert lib.get_user_reservations(
            "U002") == ["Apple Tales", "Zebra Stories"]

    def test_level4_reservations_nonexistent_user(self):
        lib = LibrarySystem()
        assert lib.get_user_reservations("U999") == []


class TestLevel4AutoAssignment:
    """Tests for automatic assignment from waitlist on return."""

    def test_level4_auto_assign_on_return(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        lib.return_book("B001", "U001", "2024-01-10")
        # Book should now be checked out to Bob
        assert lib.get_user_books("U002") == ["The Great Gatsby"]
        assert lib.get_waitlist("B001") == []
        assert lib.get_user_reservations("U002") == []

    def test_level4_auto_assign_fifo(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.register_user("U003", "Charlie")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B001", "U003")
        lib.return_book("B001", "U001", "2024-01-10")
        # Book should be assigned to Bob (first in line)
        assert lib.get_user_books("U002") == ["The Great Gatsby"]
        assert lib.get_waitlist("B001") == ["Charlie"]

    def test_level4_auto_assign_skip_at_limit(self):
        lib = LibrarySystem()
        lib.add_book("B001", "Book 1")
        lib.add_book("B002", "Book 2")
        lib.add_book("B003", "Book 3")
        lib.add_book("B004", "Book 4")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.register_user("U003", "Charlie")

        # Alice checks out Book 1
        lib.checkout_book("B001", "U001", "2024-01-01")
        # Bob checks out 3 books (at limit)
        lib.checkout_book("B002", "U002", "2024-01-01")
        lib.checkout_book("B003", "U002", "2024-01-01")
        lib.checkout_book("B004", "U002", "2024-01-01")
        # Bob and Charlie reserve Book 1
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B001", "U003")

        # Alice returns Book 1
        lib.return_book("B001", "U001", "2024-01-10")

        # Bob is at limit, so Charlie should get the book
        assert lib.get_user_books("U003") == ["Book 1"]
        assert "Bob" in lib.get_waitlist("B001")  # Bob stays in waitlist
        assert lib.get_user_reservations("U003") == []

    def test_level4_no_auto_assign_empty_waitlist(self):
        lib = LibrarySystem()
        lib.add_book("B001", "The Great Gatsby")
        lib.register_user("U001", "Alice")
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.return_book("B001", "U001", "2024-01-10")
        # Book should be available
        assert lib.get_available_books() == ["The Great Gatsby"]


class TestLevel4Integration:
    """Integration tests for Level 4 features."""

    def test_level4_complex_scenario(self):
        lib = LibrarySystem()

        # Setup books and users
        lib.add_book("B001", "The Great Gatsby")
        lib.add_book("B002", "1984")
        lib.register_user("U001", "Alice")
        lib.register_user("U002", "Bob")
        lib.register_user("U003", "Charlie")

        # Alice checks out both books
        lib.checkout_book("B001", "U001", "2024-01-01")
        lib.checkout_book("B002", "U001", "2024-01-01")

        # Bob reserves both books
        lib.reserve_book("B001", "U002")
        lib.reserve_book("B002", "U002")

        # Charlie reserves Book 1
        lib.reserve_book("B001", "U003")

        # Verify waitlists
        assert lib.get_waitlist("B001") == ["Bob", "Charlie"]
        assert lib.get_waitlist("B002") == ["Bob"]

        # Alice returns Book 1 - should go to Bob
        lib.return_book("B001", "U001", "2024-01-10")
        assert lib.get_user_books("U002") == ["The Great Gatsby"]
        assert lib.get_waitlist("B001") == ["Charlie"]

        # Bob returns Book 1 - should go to Charlie
        lib.return_book("B001", "U002", "2024-01-15")
        assert lib.get_user_books("U003") == ["The Great Gatsby"]
        assert lib.get_waitlist("B001") == []
