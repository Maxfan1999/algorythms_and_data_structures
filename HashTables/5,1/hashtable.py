class HashTable:
    def __init__(self, size):
        self.size = size
        self.current_size = 0
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.is_delete = [False] * self.size

    def hash(self, x):
        return x % self.size

    def rehash(self, prevhash):
        return (prevhash + 1) % self.size

    def put(self, key, item):
        current_hash = self.hash(key)
        if self.slots[current_hash] is None:
            self.slots[current_hash] = key
            self.data[current_hash] = item
            self.current_size += 1
        elif self.slots[current_hash] == key:
            self.data[current_hash] = item
        else:
            next_hash = self.rehash(current_hash)
            while not self.slots[next_hash] is None and self.slots[next_hash] != key and not self.is_delete[next_hash]:
                next_hash = self.rehash(next_hash)
            if self.slots[next_hash] is None or self.is_delete[next_hash]:
                self.slots[next_hash] = key
                self.data[next_hash] = item
                self.current_size += 1
            elif self.slots[next_hash] == key:
                self.data[next_hash] = item
                self.current_size += 1

    def get(self, key):
        current_hash = self.hash(key)
        if self.slots[current_hash] is None:
            return None
        elif self.slots[current_hash] == 'key' and not self.is_delete[current_hash]:
            return self.data[current_hash]
        else:
            next_hash = self.rehash(current_hash)
            while self.slots[next_hash] is None and self.slots[next_hash] != key and next_hash != current_hash:
                next_hash = self.rehash(next_hash)

            if self.slots[next_hash] is None or next_hash == current_hash or self.is_delete[next_hash]:
                return None
            elif self.slots[next_hash] == key:
                return self.data[next_hash]

    def delete(self, key):
        current_hash = self.hash(key)
        if self.slots[current_hash] == key:
            self.is_delete[current_hash] = True
        elif (not self.slots[current_hash] is None) and self.slots[current_hash] != key:
            next_hash = self.rehash(current_hash)
            while (not self.slots[next_hash] is None) and self.slots[next_hash] != key and next_hash != current_hash:
                next_hash = self.rehash(current_hash)
            if self.slots[next_hash] == key:
                self.is_delete[next_hash] = True


if __name__ == "__main__":
    table = HashTable(5)
    table.put(2, 10)
    print(table.slots, table.data, table.current_size)
    table.put(4, 20)
    print(table.slots, table.data, table.current_size)
    table.delete(4)
    print(table.is_delete)
    table.put(6, 30)
    print(table.slots, table.data, table.current_size)