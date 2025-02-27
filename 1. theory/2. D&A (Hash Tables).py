class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update value if key exists
                return
        self.table[index].append([key, value])  # Insert new key-value pair

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


if __name__ == "__main__":
    ht = HashTable(10)

    # Inserting key-value pairs
    ht.insert("name", "Alice")
    ht.insert("age", "25")
    ht.insert("city", "New York")

    ht.display()

    # Searching for a key
    print("\nSearch 'age':", ht.search("age"))

    # Updating a value
    ht.insert("age", "26")
    print("Updated 'age':", ht.search("age"))

    # Deleting a key
    ht.delete("city")
    ht.display()