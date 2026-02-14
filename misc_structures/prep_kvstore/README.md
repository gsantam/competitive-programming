# Key-Value Store with Transactions - Interview Prep

This project simulates a coding interview where you build a key-value store with progressive requirements. Each phase builds on the previous one, requiring refactoring and adaptation.

**Time Target:** 90 minutes total  
**Language:** Python (standard library only)

---

## Phase 1: Basic Key-Value Store (15-20 min)

Implement a simple in-memory key-value store with the following operations:

| Method | Description |
|--------|-------------|
| `set(key: str, value: int) -> None` | Store the value for the given key |
| `get(key: str) -> int \| None` | Return the value for the key, or `None` if not found |
| `delete(key: str) -> bool` | Delete the key and return `True` if it existed, `False` otherwise |
| `exists(key: str) -> bool` | Return `True` if the key exists |

**Example:**
```python
store = KeyValueStore()
store.set("a", 10)
store.get("a")      # Returns 10
store.exists("a")   # Returns True
store.delete("a")   # Returns True
store.get("a")      # Returns None
```

---

## Phase 2: Counting and Querying (20-25 min)

Extend your store with efficient counting and querying capabilities:

| Method | Description |
|--------|-------------|
| `count(value: int) -> int` | Return how many keys have the given value |
| `keys_with_value(value: int) -> list[str]` | Return all keys that have the given value (order doesn't matter) |

**Critical:** These operations should be efficient. If you have 1 million keys, `count()` should NOT iterate through all of them.

**Example:**
```python
store = KeyValueStore()
store.set("a", 10)
store.set("b", 10)
store.set("c", 20)
store.count(10)           # Returns 2
store.keys_with_value(10) # Returns ["a", "b"] (any order)
store.set("a", 20)        # Update a's value
store.count(10)           # Returns 1 (only "b" now)
store.count(20)           # Returns 2 ("a" and "c")
```

---

## Phase 3: Transaction Support (25-30 min)

Add transaction support with commit and rollback:

| Method | Description |
|--------|-------------|
| `begin() -> None` | Start a new transaction |
| `commit() -> bool` | Commit the current transaction. Returns `False` if no transaction is active |
| `rollback() -> bool` | Rollback the current transaction. Returns `False` if no transaction is active |

**Transaction Semantics:**
- Changes made within a transaction are visible immediately (even before commit)
- `rollback()` reverts ALL changes made since the matching `begin()`
- `commit()` makes changes permanent
- All operations (set, delete, count, etc.) should work correctly within transactions

**Example:**
```python
store = KeyValueStore()
store.set("a", 10)
store.begin()
store.set("a", 20)
store.get("a")       # Returns 20 (visible within transaction)
store.rollback()     # Returns True
store.get("a")       # Returns 10 (rolled back)

store.begin()
store.set("b", 30)
store.commit()       # Returns True
store.get("b")       # Returns 30 (committed)
```

---

## Phase 4: Nested Transactions (20-25 min)

Extend transactions to support nesting:

**Nested Transaction Semantics:**
- Transactions can be nested arbitrarily deep
- `begin()` always starts a new nested transaction
- `commit()` commits the innermost transaction to its parent (not to permanent storage until all transactions are committed)
- `rollback()` only reverts the innermost transaction
- A rollback of an outer transaction also reverts all inner transaction changes

**Example:**
```python
store = KeyValueStore()
store.set("a", 10)

store.begin()           # Transaction 1
store.set("a", 20)
store.begin()           # Transaction 2 (nested)
store.set("a", 30)
store.get("a")          # Returns 30
store.rollback()        # Rollback Transaction 2
store.get("a")          # Returns 20 (Transaction 1's value)
store.commit()          # Commit Transaction 1
store.get("a")          # Returns 20

store.begin()           # New Transaction 1
store.set("a", 100)
store.begin()           # Transaction 2
store.set("a", 200)
store.commit()          # Commit Transaction 2 to Transaction 1
store.get("a")          # Returns 200
store.rollback()        # Rollback Transaction 1 (including committed Transaction 2)
store.get("a")          # Returns 20 (from earlier)
```

---

## Running Tests

```bash
# Run all tests
pytest test_kvstore.py -v

# Run specific phase
pytest test_kvstore.py -v -k "phase1"
pytest test_kvstore.py -v -k "phase2"
pytest test_kvstore.py -v -k "phase3"
pytest test_kvstore.py -v -k "phase4"
```

---

## Tips

1. **Read all phases first** - Understanding future requirements helps avoid major refactors
2. **Don't over-engineer Phase 1** - But do keep extensibility in mind
3. **Phase 2 requires careful data structure choice** - Think about what auxiliary structures you need
4. **Phase 3 & 4 require tracking state changes** - Consider how to snapshot/restore state efficiently
5. **Prioritize passing tests** - Working code > perfect code
