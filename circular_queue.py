class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow! Cannot insert", item)
            return

        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Inserted {item} into queue")

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow! Cannot delete")
            return

        deleted_item = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Deleted {deleted_item} from queue")
        return deleted_item

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        print("Queue contents:", end=" ")
        if self.rear >= self.front:
            print(" ".join(map(str, self.queue[self.front:self.rear + 1])))
        else:
            print(" ".join(map(str, self.queue[self.front:self.size])), end=" ")
            print(" ".join(map(str, self.queue[0:self.rear + 1])))

# Interactive user input
def main():
    size = int(input("Enter the size of the circular queue: "))
    q = CircularQueue(size)

    while True:
        print("\nOperations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the item to enqueue: "))
            q.enqueue(item)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()