class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.empty():
            x= self.stack.pop()
            print(f"popped item:{x}")
            return x
        else:
            print("empty stack")
    def peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            print("empty stack")
    def empty(self):
        return len(self.stack)==0
    def display(self):
        if not self.empty():
            for x in self.stack:
                print(x)
        else:
            print("empty stack")
    def operation(self):
        while True:
            print("1.push 2.pop 3.peek 4.display 5.exit")
            choice=int(input("enter ur choice:"))
            if choice==1:
                x=input("enter the element:")
                self.push(x)
            elif choice==2:
                self.pop()
            elif choice==3:
                top=self.peek()
                print(f"top item:{top}")
            elif choice==4:
                self.display()
            elif choice==5:
                print("exiting....")
                break
            else:
                print("invalid choice")
stack=Stack()
stack.operation()