from main import InMemoryDB

def runTests():
    db = InMemoryDB()

    try:
        # Test 1
        assert db.get("A") is None
        print("Test 1 passed: get('A') returns None")

        # Test 2
        try:
            db.put("A", 5)
            print("Test 2 failed: put() without transaction should fail")
            return False
        except:
            print("Test 2 passed: put() without transaction throws error")

        # Test 3
        db.begin_transaction()
        print("Test 3 passed: begin_transaction() started")

        # Test 4
        db.put("A", 5)
        print("Test 4 passed: put('A', 5) in transaction")

        # Test 5
        assert db.get("A") is None
        print("Test 5 passed: get('A') still None before commit")

        # Test 6
        db.put("A", 6)
        print("Test 6 passed: put('A', 6) updated value in transaction")

        # Test 7
        db.commit()
        print("Test 7 passed: commit() applied changes")

        # Test 8
        assert db.get("A") == 6
        print("Test 8 passed: get('A') returns 6 after commit")

        # Test 9
        try:
            db.commit()
            print("Test 9 failed: commit() without transaction should fail")
            return False
        except:
            print("Test 9 passed: commit() without transaction throws error")

        # Test 10
        try:
            db.rollback()
            print("Test 10 failed: rollback() without transaction should fail")
            return False
        except:
            print("Test 10 passed: rollback() without transaction throws error")

        # Test 11
        assert db.get("B") is None
        print("Test 11 passed: get('B') returns None")

        # Test 12
        db.begin_transaction()
        print("Test 12 passed: begin_transaction() started for B")

        # Test 13
        db.put("B", 10)
        print("Test 13 passed: put('B', 10) in transaction")

        # Test 14
        db.rollback()
        print("Test 14 passed: rollback() discarded changes")

        # Test 15
        assert db.get("B") is None
        print("Test 15 passed: get('B') returns None after rollback")

        print("All tests passed!")
        return True

    except AssertionError as e:
        print(f"Test failed: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


if __name__ == "__main__":
    if not runTests():
        print("Some tests failed")
        exit(1)
