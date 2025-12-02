# In-Memory Database

This is an in-memory key-value database that supports transactions. You can make changes in a transaction and either commit them to save or rollback to undo.

## How to Run

Make sure you have Python 3.

Run:
```bash
python3 main.py
```
Or run the tests:
```bash
python3 test.py
```
## Features

- `get(key)` - gets a value, returns None if key doesn't exist
- `put(key, value)` - sets a value (must be in a transaction)
- `begin_transaction()` - starts a new transaction
- `commit()` - saves all changes from the transaction
- `rollback()` - cancels the transaction and undoes changes

## Example

```python
from main import InMemoryDB

inmemoryDB = InMemoryDB()

inmemoryDB.begin_transaction()
inmemoryDB.put("A", 5)
inmemoryDB.commit()

print(inmemoryDB.get("A"))
```

## Notes
If this was an assignment, I would make the instructions clearer, especially about what happens if you try to start a transaction when one is already running. I would also add a few more methods like delete() or clear() so the project feels more complete. It would help to include some starter code so students know how to begin, and I would add test cases that count for points to make grading easier. 
