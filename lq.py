class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,x):
        self.queue.append(x)
    def dequeue(self):
        if not self.empty():
            x= self.queue.pop(0)
            print(f"popped element:{x}")
            return x
        else:
            print("empty")
    def peek(self):
        if not self.empty():
            return self.queue[0]
        else:
            print("empty")
    def empty(self):
        return len(self.queue)==0
    def front(self):
        if not self.empty():
            return self.queue[0],0
        else:
            return -1
    def rear(self):
        if not self.empty():
            return self.queue[-1],len(self.queue)-1
        else:
            return -1
    def display(self):
        if not self.empty():
            for x in self.queue:
                print("queue:")
                print(x)
        else:
            print("empty")
    def operation(self):
        while True:
            print("1.enqueue 2.dequeue 3.peek 4.display 5.front 6.rear 7.exit")
            c=int(input("enterur choice:"))
            if c==1:
                x=input("enter the elment:")
                self.enqueue(x)
            elif c==2:
                self.dequeue()
            elif c==3:
                top=self.peek()
                print(f"topelement{top}")
            elif c==5:
                Front,front=self.front()
                if front!= -1:
                    print(f"front:{Front}index:{front}")
            elif c==6:
                Rear,rear=self.rear()
                if rear!= -1:
                    print(f"rear:{Rear}index:{rear}")
            elif c==4:
                self.display()
            elif c==7:
                print("exiting...")
                break
            else:
                print("invalid")
q=queue()
q.operation()

    