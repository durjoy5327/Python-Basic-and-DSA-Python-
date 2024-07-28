class Node:
    def __init__(self , data=None,  next= None , prev=None ):
        self.data=data
        self.prev=prev
        self.next=next

class Doubly_linked_list:
    def __init__(self):
        self.head=None

    def print_forward(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return
        itr= self.head
        doubly_list=""
        while itr:
            doubly_list+=str(itr.data)+"-->"
            itr= itr.next
        print("Doubly linked list forward list is :",doubly_list)    

    def get_last_node(self):
        itr= self.head
        while itr.next:
            itr= itr.next
        return itr

    def print_backward(self):
        if self.head is None:
            print("Doubly linked list is empty")
            return
        last_node= self.get_last_node()
        doubly_list=""
        while last_node:
            doubly_list+=str(last_node.data)+"-->"
            last_node=last_node.prev
        print("Doubly linked list backward list is :",doubly_list)
        
    def get_length(self):
        count=0
        itr= self.head
        while itr:
            count+=1
            itr=itr.next
            
        return count
    
    def insert_at_beginning(self, data):
        if self.head == None:
            node= Node(data , self.head, None)
            self.head=node
        else:
            node= Node(data , self.head, None)
            self.head.prev = node
            self.head= node
    def insert_at_end(self, data):
        if self.head is None:
            node= Node(data , self.head, None)
            self.head=node
            return
        itr= self.head
        while itr.next:
            itr= itr.next
        itr.next= Node(data , None, itr)

    def insert_At(self, index ,data):
        if index<0 or index >= self.get_length():
            print("Invalid index")
            return
        if index==0:
            self.insert_at_beginning(data)
            return
        count=0
        itr= self.head
        while itr:
            if count==index-1:
                node = Node(data , itr.next, itr)
                if itr.next:
                    itr.prev=node
                itr.next= node
                return
            itr=itr.next
            count+=1

    def insert_values(self , datalist):
        for data in datalist:
            self.insert_at_end(word)
        
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            print("Invalid index")
            return
        itr = self.head
        count=0
        while itr:
            if index == count:
                itr.prev.next= itr.next
                if itr.next:
                    itr.next.prev= itr.prev
                return
            itr= itr.next
            count+=1


obj=Doubly_linked_list()
obj.get_length()
obj.insert_at_beginning(25)
obj.insert_at_beginning(30)
obj.insert_at_beginning(41)
obj.insert_at_beginning(50)
obj.insert_at_beginning(60)
obj.insert_at_end(100)
obj.insert_at_end(150)
obj.insert_at_end(200)
obj.insert_At(7,180)
obj.print_forward()
obj.remove_at(7)
obj.print_forward()
k=obj.get_length()
print(k)
