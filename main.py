class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction = None
    
    def get(self, key):
        if key in self.data:
            return self.data[key]
        return None
    
    def put(self, key, value):
        if self.transaction is None:
            raise Exception("No transaction")
        self.transaction[key] = value
    
    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("Transaction already running")
        self.transaction = {}
    
    def commit(self):
        if self.transaction is None:
            raise Exception("No transaction")
        for key in self.transaction:
            self.data[key] = self.transaction[key]
        self.transaction = None
    
    def rollback(self):
        if self.transaction is None:
            raise Exception("No transaction")
        self.transaction = None


if __name__ == "__main__":
    inmemoryDB = InMemoryDB()
    
    # get on empty DB
    print(inmemoryDB.get("A"))  # None
    
    # transaction: put and commit
    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5)
    inmemoryDB.put("A", 6)
    inmemoryDB.commit()
    print(inmemoryDB.get("A"))  # 6
    
    # rollback example
    inmemoryDB.begin_transaction()
    inmemoryDB.put("B", 10)
    inmemoryDB.rollback()
    print(inmemoryDB.get("B"))  # None
    
    # error handling
    try:
        inmemoryDB.put("C", 1)
    except Exception as e:
        print(e)
