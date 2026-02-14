"""
Test suite for KeyValueStore

Run with: pytest test_kvstore.py -v
Run specific phase: pytest test_kvstore.py -v -k "phase1"
"""

import pytest
from kvstore import KeyValueStore


# ============================================================================
# PHASE 1: Basic Key-Value Operations
# ============================================================================

class TestPhase1BasicOperations:
    """Phase 1: Basic set, get, delete, exists operations."""

    def test_phase1_set_and_get_single_key(self):
        """Can set and retrieve a single value."""
        store = KeyValueStore()
        store.set("name", 42)
        assert store.get("name") == 42

    def test_phase1_get_nonexistent_returns_none(self):
        """Getting a nonexistent key returns None."""
        store = KeyValueStore()
        assert store.get("missing") is None

    def test_phase1_set_overwrites_existing(self):
        """Setting an existing key overwrites the value."""
        store = KeyValueStore()
        store.set("x", 10)
        store.set("x", 20)
        assert store.get("x") == 20

    def test_phase1_multiple_keys(self):
        """Can store and retrieve multiple independent keys."""
        store = KeyValueStore()
        store.set("a", 1)
        store.set("b", 2)
        store.set("c", 3)
        assert store.get("a") == 1
        assert store.get("b") == 2
        assert store.get("c") == 3

    def test_phase1_exists_returns_true_for_existing(self):
        """exists() returns True for existing keys."""
        store = KeyValueStore()
        store.set("key", 100)
        assert store.exists("key") is True

    def test_phase1_exists_returns_false_for_missing(self):
        """exists() returns False for nonexistent keys."""
        store = KeyValueStore()
        assert store.exists("missing") is False

    def test_phase1_delete_existing_key(self):
        """Deleting an existing key returns True and removes it."""
        store = KeyValueStore()
        store.set("temp", 999)
        assert store.delete("temp") is True
        assert store.get("temp") is None
        assert store.exists("temp") is False

    def test_phase1_delete_nonexistent_key(self):
        """Deleting a nonexistent key returns False."""
        store = KeyValueStore()
        assert store.delete("never_existed") is False

    def test_phase1_delete_then_set_again(self):
        """Can set a key again after deleting it."""
        store = KeyValueStore()
        store.set("reuse", 1)
        store.delete("reuse")
        store.set("reuse", 2)
        assert store.get("reuse") == 2

    def test_phase1_zero_and_negative_values(self):
        """Handles zero and negative integer values."""
        store = KeyValueStore()
        store.set("zero", 0)
        store.set("negative", -50)
        assert store.get("zero") == 0
        assert store.get("negative") == -50
        assert store.exists("zero") is True  # 0 is a valid value, key exists


# ============================================================================
# PHASE 2: Counting and Querying
# ============================================================================

class TestPhase2CountingAndQuerying:
    """Phase 2: Efficient counting and value-based queries."""

    def test_phase2_count_single_occurrence(self):
        """count() returns 1 for a value with one key."""
        store = KeyValueStore()
        store.set("only", 42)
        assert store.count(42) == 1

    def test_phase2_count_multiple_occurrences(self):
        """count() returns correct count for multiple keys with same value."""
        store = KeyValueStore()
        store.set("a", 10)
        store.set("b", 10)
        store.set("c", 10)
        store.set("d", 20)
        assert store.count(10) == 3
        assert store.count(20) == 1

    def test_phase2_count_zero_for_missing_value(self):
        """count() returns 0 for a value that doesn't exist."""
        store = KeyValueStore()
        store.set("x", 5)
        assert store.count(999) == 0

    def test_phase2_count_updates_on_set_overwrite(self):
        """count() updates correctly when a key's value changes."""
        store = KeyValueStore()
        store.set("key", 10)
        store.set("other", 10)
        assert store.count(10) == 2

        store.set("key", 20)  # Change key's value from 10 to 20
        assert store.count(10) == 1
        assert store.count(20) == 1

    def test_phase2_count_updates_on_delete(self):
        """count() updates correctly when a key is deleted."""
        store = KeyValueStore()
        store.set("a", 5)
        store.set("b", 5)
        assert store.count(5) == 2

        store.delete("a")
        assert store.count(5) == 1

    def test_phase2_keys_with_value_single(self):
        """keys_with_value() returns the single key with that value."""
        store = KeyValueStore()
        store.set("unique", 100)
        assert store.keys_with_value(100) == ["unique"]

    def test_phase2_keys_with_value_multiple(self):
        """keys_with_value() returns all keys with that value."""
        store = KeyValueStore()
        store.set("x", 7)
        store.set("y", 7)
        store.set("z", 7)
        store.set("other", 8)

        result = store.keys_with_value(7)
        assert sorted(result) == ["x", "y", "z"]

    def test_phase2_keys_with_value_empty(self):
        """keys_with_value() returns empty list for nonexistent value."""
        store = KeyValueStore()
        store.set("a", 1)
        assert store.keys_with_value(999) == []

    def test_phase2_keys_with_value_updates_on_change(self):
        """keys_with_value() reflects changes when values are updated."""
        store = KeyValueStore()
        store.set("a", 10)
        store.set("b", 10)

        store.set("a", 20)  # Move 'a' to value 20

        assert store.keys_with_value(10) == ["b"]
        assert store.keys_with_value(20) == ["a"]

    def test_phase2_count_after_delete_and_readd(self):
        """Counts remain accurate after delete and re-add cycles."""
        store = KeyValueStore()
        store.set("k", 50)
        assert store.count(50) == 1

        store.delete("k")
        assert store.count(50) == 0

        store.set("k", 50)
        assert store.count(50) == 1


# ============================================================================
# PHASE 3: Transaction Support
# ============================================================================

class TestPhase3Transactions:
    """Phase 3: Basic transaction support with commit and rollback."""

    def test_phase3_commit_without_transaction_returns_false(self):
        """commit() returns False when no transaction is active."""
        store = KeyValueStore()
        assert store.commit() is False

    def test_phase3_rollback_without_transaction_returns_false(self):
        """rollback() returns False when no transaction is active."""
        store = KeyValueStore()
        assert store.rollback() is False

    def test_phase3_begin_and_commit(self):
        """Changes persist after commit."""
        store = KeyValueStore()
        store.begin()
        store.set("key", 100)
        assert store.commit() is True
        assert store.get("key") == 100

    def test_phase3_begin_and_rollback(self):
        """Changes are reverted after rollback."""
        store = KeyValueStore()
        store.set("key", 10)
        store.begin()
        store.set("key", 20)
        assert store.get("key") == 20  # Visible during transaction
        assert store.rollback() is True
        assert store.get("key") == 10  # Reverted

    def test_phase3_rollback_new_key(self):
        """Rolling back removes keys that were added in the transaction."""
        store = KeyValueStore()
        store.begin()
        store.set("new_key", 999)
        assert store.exists("new_key") is True
        store.rollback()
        assert store.exists("new_key") is False

    def test_phase3_rollback_delete(self):
        """Rolling back restores keys that were deleted in the transaction."""
        store = KeyValueStore()
        store.set("to_delete", 50)
        store.begin()
        store.delete("to_delete")
        assert store.exists("to_delete") is False
        store.rollback()
        assert store.get("to_delete") == 50

    def test_phase3_multiple_changes_in_transaction(self):
        """Multiple changes in a transaction all get rolled back."""
        store = KeyValueStore()
        store.set("a", 1)
        store.set("b", 2)

        store.begin()
        store.set("a", 100)
        store.set("b", 200)
        store.set("c", 300)
        store.delete("a")

        store.rollback()

        assert store.get("a") == 1
        assert store.get("b") == 2
        assert store.exists("c") is False

    def test_phase3_count_visible_in_transaction(self):
        """count() reflects uncommitted changes during transaction."""
        store = KeyValueStore()
        store.set("a", 10)
        assert store.count(10) == 1

        store.begin()
        store.set("b", 10)
        assert store.count(10) == 2  # Visible during transaction

        store.rollback()
        assert store.count(10) == 1  # Reverted

    def test_phase3_count_after_commit(self):
        """count() reflects committed changes."""
        store = KeyValueStore()
        store.begin()
        store.set("x", 7)
        store.set("y", 7)
        store.commit()
        assert store.count(7) == 2

    def test_phase3_sequential_transactions(self):
        """Can have multiple sequential transactions."""
        store = KeyValueStore()

        store.begin()
        store.set("first", 1)
        store.commit()

        store.begin()
        store.set("second", 2)
        store.rollback()

        store.begin()
        store.set("third", 3)
        store.commit()

        assert store.get("first") == 1
        assert store.exists("second") is False
        assert store.get("third") == 3


# ============================================================================
# PHASE 4: Nested Transactions
# ============================================================================

class TestPhase4NestedTransactions:
    """Phase 4: Nested transaction support."""

    def test_phase4_nested_commit_then_outer_commit(self):
        """Inner commit + outer commit makes changes permanent."""
        store = KeyValueStore()
        store.set("val", 1)

        store.begin()       # Outer
        store.set("val", 2)
        store.begin()       # Inner
        store.set("val", 3)
        store.commit()      # Commit inner to outer
        assert store.get("val") == 3
        store.commit()      # Commit outer to permanent

        assert store.get("val") == 3

    def test_phase4_nested_rollback_preserves_outer(self):
        """Rolling back inner transaction preserves outer transaction state."""
        store = KeyValueStore()
        store.set("x", 10)

        store.begin()           # Outer
        store.set("x", 20)
        store.begin()           # Inner
        store.set("x", 30)
        assert store.get("x") == 30
        store.rollback()        # Rollback inner
        assert store.get("x") == 20  # Back to outer's value
        store.commit()          # Commit outer

        assert store.get("x") == 20

    def test_phase4_outer_rollback_reverts_committed_inner(self):
        """Rolling back outer transaction reverts even committed inner changes."""
        store = KeyValueStore()
        store.set("key", 100)

        store.begin()           # Outer
        store.set("key", 200)
        store.begin()           # Inner
        store.set("key", 300)
        store.commit()          # Commit inner to outer (key=300 in outer)
        assert store.get("key") == 300
        store.rollback()        # Rollback outer (including inner's committed change)

        assert store.get("key") == 100  # Back to original

    def test_phase4_three_levels_deep(self):
        """Transactions can be nested three levels deep."""
        store = KeyValueStore()
        store.set("n", 0)

        store.begin()       # Level 1
        store.set("n", 1)
        store.begin()       # Level 2
        store.set("n", 2)
        store.begin()       # Level 3
        store.set("n", 3)

        assert store.get("n") == 3
        store.rollback()    # Rollback level 3
        assert store.get("n") == 2
        store.commit()      # Commit level 2 to level 1
        assert store.get("n") == 2
        store.commit()      # Commit level 1
        assert store.get("n") == 2

    def test_phase4_nested_with_different_keys(self):
        """Nested transactions work correctly with different keys."""
        store = KeyValueStore()

        store.begin()           # Outer
        store.set("outer_key", 1)
        store.begin()           # Inner
        store.set("inner_key", 2)
        store.commit()          # Commit inner
        store.commit()          # Commit outer

        assert store.get("outer_key") == 1
        assert store.get("inner_key") == 2

    def test_phase4_nested_delete_and_rollback(self):
        """Nested transactions correctly handle delete + rollback."""
        store = KeyValueStore()
        store.set("data", 999)

        store.begin()           # Outer
        store.begin()           # Inner
        store.delete("data")
        assert store.exists("data") is False
        store.rollback()        # Rollback inner
        assert store.get("data") == 999
        store.rollback()        # Rollback outer

        assert store.get("data") == 999

    def test_phase4_commit_returns_true_in_nested(self):
        """commit() returns True for nested transactions."""
        store = KeyValueStore()
        store.begin()
        store.begin()
        assert store.commit() is True  # Commit inner
        assert store.commit() is True  # Commit outer

    def test_phase4_complex_nested_scenario(self):
        """Complex scenario with multiple operations across nesting levels."""
        store = KeyValueStore()
        store.set("a", 1)
        store.set("b", 2)

        store.begin()               # T1
        store.set("a", 10)
        store.set("c", 30)

        store.begin()               # T2 (nested in T1)
        store.set("b", 20)
        store.delete("c")
        store.set("d", 40)

        # At this point: a=10, b=20, c=deleted, d=40
        assert store.get("a") == 10
        assert store.get("b") == 20
        assert store.exists("c") is False
        assert store.get("d") == 40

        store.commit()              # Commit T2 to T1

        # Still: a=10, b=20, c=deleted, d=40 (in T1)
        assert store.get("a") == 10
        assert store.get("b") == 20

        store.begin()               # T3 (nested in T1)
        store.set("a", 100)
        store.rollback()            # Rollback T3

        # Back to T1 state: a=10
        assert store.get("a") == 10

        store.rollback()            # Rollback T1

        # Back to original: a=1, b=2, c doesn't exist (it was set in T1), d doesn't exist
        assert store.get("a") == 1
        assert store.get("b") == 2
        assert store.exists("c") is False
        assert store.exists("d") is False

    def test_phase4_count_with_nested_transactions(self):
        """count() works correctly with nested transactions and rollbacks."""
        store = KeyValueStore()
        store.set("k1", 5)

        store.begin()               # T1
        store.set("k2", 5)
        assert store.count(5) == 2

        store.begin()               # T2
        store.set("k3", 5)
        assert store.count(5) == 3
        store.set("k1", 99)         # Change k1's value
        assert store.count(5) == 2  # k2, k3

        store.rollback()            # Rollback T2
        assert store.count(5) == 2  # k1, k2

        store.rollback()            # Rollback T1
        assert store.count(5) == 1  # Just k1

    def test_phase4_keys_with_value_nested(self):
        """keys_with_value() works correctly in nested transactions."""
        store = KeyValueStore()
        store.set("x", 10)

        store.begin()
        store.set("y", 10)

        store.begin()
        store.set("z", 10)

        result = store.keys_with_value(10)
        assert sorted(result) == ["x", "y", "z"]

        store.rollback()  # Rollback inner
        result = store.keys_with_value(10)
        assert sorted(result) == ["x", "y"]

        store.rollback()  # Rollback outer
        result = store.keys_with_value(10)
        assert result == ["x"]
