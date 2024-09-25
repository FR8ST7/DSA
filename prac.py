class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            while last.next:
                last=last.next
                last.next=new_node

    def search(self,key):
        current=self.head
        while current:
            if current.data==key:
                return True
            current= current.next
            return False
    
    def delete(self,key):
        #if 1st node is the key we r finding to delete
        current=self.head
        if current and current.data==key:
            self.head= current.next
            current= None
        #if 1st is not key we are searching the key in next node
            prev=None
            while current and current.data!=key:
                prev= current
                current = current.next
        #if key is not found
            if current is None:
                print(f"element {key} not found")
                return
        #unlink the bode
            prev.next= current.next
            current= None
            
    def display(self):
        if self.head is None:
            print("empty")
        else:
            current= self.head
            while current:
                print(current.data,end="->")
                current=current.next
            print("none")
    
    def Menu(self):
        while(True):
            print("1.insert 2.delete 3.search 4.display 5.exit")
            choice= int(input("enter your choice:"))
            if choice==1:
                data= input("enter the value:")
                self.insert(data)
            elif choice==2:
                key= input("enter the value to delete:")
                self.delete(key)
            elif choice==3:
                key= input("enter the value to delete:")
                self.search(key)
            elif choice==4:
                self.display()
            elif choice==5:
                print("exiting...")
                break
            else:
                print("invalid input")

LL=ll()
LL.Menu()
            

