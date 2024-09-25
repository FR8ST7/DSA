class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if not self.empty():
            item= self.queue.pop(0)
            print(f"deleted item:{item}")
            return item
    def peek(self):
        if not self.empty():
            return self.queue[0]
    
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
    
    def empty(self):
        return len(self.queue)==0
    
    def display(self):
        if not self.empty():
            for item in self.queue:
                print("queue:")
                print(item)
        else:
            print("empty queue")

    def queue_operation(self):
        while(True):
            print("1. enueue 2.dequeue 3.peek 4.display 5.front value 6.rear value 7.exit")
            choice= int(input("enter the choice:"))
            if choice==1:
                item=input("enter the element:")
                self.enqueue(item)
            elif choice==2:
                self.dequeue()
            elif choice==3:
                top=self.peek()
                if top is not None:
                    print(f"top item:{top}")
            elif choice==4:
                self.display()
            elif choice==5:
                Front,front= self.front()
                if front!= -1:
                    print(f"front:{Front}index:{front}")
            elif choice==6:
                Rear,rear= self.rear()
                if rear!=-1:
                    print(f"rear:{Rear}index:{rear}")
            elif choice==7:
                print("exiting...")
                break
            else:
                print("invalid input")
queue= Queue()
queue.queue_operation()
                
            
