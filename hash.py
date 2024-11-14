class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
            print(f"Inserted {key} at index {index}")
        else:
            print(f"Duplicate key {key} not inserted.")

    def search(self, key):
        index = self.hash(key)
        if key in self.table[index]:
            print(f"Found {key} at index {index}")
            return True
        else:
            print(f"{key} not found.")
            return False

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

def main():
    size = int(input("Enter size of hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\nChoose an option:")
        print("1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter a key to insert: "))
            hash_table.insert(key)
        elif choice == 2:
            key = int(input("Enter a key to search: "))
            hash_table.search(key)
        elif choice == 3:
            hash_table.display()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
