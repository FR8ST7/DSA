class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head= None

    def insert(self,data):
        new_node= Node(data)#insert at begining
        if self.head is None:
            self.head= new_node
        else:
            last= self.head#insert at last if front is already occupied
            while last.next:
                last= last.next
                last.next= new_node
    
    def delete(self,key):
        current= self.head

        if current and current.data ==key:
            self.head = current.next
            current= None
            return
        prev= None
        while current and current.data != key:
            prev= current
            current= current.next
            if current
    
