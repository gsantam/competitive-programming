"""
Key-Value Store with Transactions

Implement the KeyValueStore class according to the requirements in README.md.
Progress through each phase, ensuring all tests pass before moving on.

Phase 1: Basic operations (set, get, delete, exists)
Phase 2: Counting and querying (count, keys_with_value)
Phase 3: Transaction support (begin, commit, rollback)
Phase 4: Nested transactions
"""


class Log:
    def __init__(self, father):
        self.transaction_log = []
        self.father = father
        self.children = []
        if father is not None:
            self.father.children.append(self)
        self.commited = False
        self.rolledback = False


class KeyValueStore:
    """
    A key-value store supporting transactions.

    Implement the following methods:

    Phase 1 - Basic Operations:
        - set(key: str, value: int) -> None
        - get(key: str) -> int | None
        - delete(key: str) -> bool
        - exists(key: str) -> bool

    Phase 2 - Counting (must be efficient, not O(n) iteration):
        - count(value: int) -> int
        - keys_with_value(value: int) -> list[str]

    Phase 3 - Transactions:
        - begin() -> None
        - commit() -> bool
        - rollback() -> bool

    Phase 4 - Nested Transactions:
        - Same methods as Phase 3, but supporting arbitrary nesting
    """

    def __init__(self):
        self.db = dict()
        self.inv_db = dict()
        self.log = None
        # TODO: Initialize your data structures here
        pass

    # ==================== PHASE 1 ====================

    def set(self, key: str, value: int) -> None:
        """Store the value for the given key."""
        if key in self.db:
            prev_value = self.db[key]
            self.inv_db[prev_value].remove(key)
        else:
            prev_value = None
        if value not in self.inv_db:
            self.inv_db[value] = set()
        self.inv_db[value].add(key)
        self.db[key] = value
        if self.log is not None:
            self.log.transaction_log.append(
                [key, prev_value])

        return True

    def get(self, key: str) -> int | None:
        """Return the value for the key, or None if not found."""
        if key not in self.db:
            return None
        return self.db[key]

    def delete(self, key: str) -> bool:
        """Delete the key and return True if it existed, False otherwise."""
        if key not in self.db:
            return False
        value = self.db[key]
        self.inv_db[value].remove(key)
        del self.db[key]
        if self.log is not None:
            self.log.transaction_log.append(
                [key, value])
        return True

    def exists(self, key: str) -> bool:
        """Return True if the key exists."""
        return key in self.db

    # ==================== PHASE 2 ====================

    def count(self, value: int) -> int:
        """Return how many keys have the given value. Must be O(1) or O(k) where k is the count."""
        return len(self.keys_with_value(value))

    def keys_with_value(self, value: int) -> list[str]:
        """Return all keys that have the given value."""
        if value not in self.inv_db:
            return []
        return list(self.inv_db[value])

    # ==================== PHASE 3 & 4 ====================

    def begin(self) -> None:
        self.log = Log(self.log)

        """Start a new transaction (can be nested in Phase 4)."""

    def commit(self) -> bool:
        if self.log is None:
            return False
        self.log.commited = True
        self.log = self.log.father
        return True

    def rollback_recurse(self, log):
        all_transactions = list(reversed(log.transaction_log))
        for log_children in log.children:
            self.rollback_recurse(log_children)
        for key, prev_value in all_transactions:
            if prev_value is not None:
                self.set(key, prev_value)
            else:
                self.delete(key)

    def rollback(self) -> bool:
        if not self.log:
            return False
        self.rollback_recurse(self.log)
        self.log = self.log.father
        return True
