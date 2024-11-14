class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto the stack.")

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        print(f"Popped {popped_data} from the stack.")
        return popped_data

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        print(f"Top of stack: {self.top.data}")
        return self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return
        print("Stack elements:")
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued {data} to the queue.")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued {dequeued_data} from the queue.")
        return dequeued_data

    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        print(f"Front of queue: {self.front.data}")
        return self.front.data

    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return
        print("Queue elements:")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    stack = Stack()
    queue = Queue()

    while True:
        print("\nChoose an operation:")
        print("1. Push to Stack")
        print("2. Pop from Stack")
        print("3. Peek Stack")
        print("4. Display Stack")
        print("5. Enqueue to Queue")
        print("6. Dequeue from Queue")
        print("7. Peek Queue")
        print("8. Display Queue")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter value to push onto stack: "))
            stack.push(data)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            data = int(input("Enter value to enqueue to queue: "))
            queue.enqueue(data)
        elif choice == '6':
            queue.dequeue()
        elif choice == '7':
            queue.peek()
        elif choice == '8':
            queue.display()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
