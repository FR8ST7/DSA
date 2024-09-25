class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            item= self.stack.pop()
            print(f"popped item:{item}")
            return item
        else:
            print("empty stack cant pop")
    
    def peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            print("empty stack cant peek")
    
    def empty(self):
        return len(self.stack)==0
    
    def display(self):
        if self.empty():
            print("empty")
        else:
            print("stack:")
        for item in self.stack:
            print(item)
    
    def stack_operation(self):
        while True:
            print("1. push 2.pop 3.peek 4.display 5.exit")
            choice= int(input("enter your choice:"))
            if choice==1:
                item=input("enter to push")
                self.push(item)
            elif choice==2:
                self.pop()
            elif choice==3:
                top=self.peek()
                if top is not None:
                 print(f"top item:{top}")
                self.peek()
            elif choice==4:
                self.display()
            elif choice==5:
                print("exiting...")
                break
            else:
                print("invalid input")
stack= Stack()
stack.stack_operation()
        