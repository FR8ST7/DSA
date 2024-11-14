class Node:
    def __init__(self,x):
        self.x=x
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,x):
        new_node=Node(x)
        new_node.next=self.top
        self.top=new_node
        print(f"pushed:{x}")
    def pop(self):
        if self.top is None:
            print("empty")
            return None
        popped= self.top.x
        self.top=self.top.next
        print(f"popped:{popped}")
        return popped
    def peek(self):
        return self.top.x
    def display(self):
        if self.top is None:
            print("empty")
            return 
        print("stack:")
        current=self.top
        while current:
            print(current.x,end=" ")
            current=current.next
        print()
        
    def operation(self):
        while True:
            print("1. push 2. pop 3.peek 4.display 5.exit")
            c=int(input("enter ur choice:"))
            if c==1:
                x=input("enter the value:")
                stack.push(x)
            elif c==2:
                stack.pop()
            elif c==3:
                top=stack.peek()
                print(f"top element:{top}")
            elif c==4:
                stack.display()
            elif c==5:
                print("exiting....")
                break
            else:
                print("invalid")
stack=Stack()
stack.operation()