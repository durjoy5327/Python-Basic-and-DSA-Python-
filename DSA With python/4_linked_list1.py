class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next=next

class Linkedlist():
    def __init__(self):
        self.head= None
    
    def insert_at_begginning(self , data):
        self.head=Node(data , self.head)
    
    def insert_at_end(self , data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        k = self.head
        while k.next:
            k=k.next
        k.next =Node(data,None)

    
    def LinkedList_length(self):
        if self.head is Node:
            print("Length of the Linked lis is now Zeor")
            return
        k= self.head
        count=0
        while k:
            count+=1
            k= k.next
        return count
    
    def insert_values(self, valuelist):
        self.head=None
        for val in valuelist:
            self.insert_at_end(val)

    def print(self):
        if self.head==None:
            return 0
        itr= self.head
        llstr=""
        while itr:
            llstr+= str(itr.data)+"--->"
            itr=itr.next
        print("Linked list values are : ",llstr)

    def remove(self, index):
        if index<0 or index>= self.LinkedList_length():
            raise Exception("This is Not valid index")
            
        if index==0:
            self.head= self.head.next
            return
        count=0
        current= self.head
        while current:
            if count==index-1:
                current.next= current.next.next
                return
            count+=1
            current=current.next
    def insert_At(self , index , value):
        if index<0 :
            raise Exception("This is Not valid index")
            return
        if index==0:
            self.insert_at_begginning(value)

        itr = self.head
        count=0
        while itr:
            if count==index-1:
                node= Node(value, itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1
    def insert_after_value(self, data_after, data_to_insert):
        itr= self.head
        while itr:
            if itr.data ==data_after:
                node= Node(data_to_insert, itr.next)
                itr.next= node
                return
            itr= itr.next
        raise Exception(f"No data found like {data_after} in linked list")
    
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        itr= self.head
        while itr:
            if itr.next.data==data:
                itr.next= itr.next.next
                return
            itr= itr.next
        raise Exception("The Value was not found or doesn't exist ")




link= Linkedlist()
"""
link.insert_at_begginning(25)
link.insert_at_begginning(28)
link.insert_at_begginning(20)
link.insert_at_begginning(89)
link.insert_at_end(500)

link.insert_values(["Durjoy","Mehlaching","Belal","Promi","Rubel"])
link.remove(3)
link.print()

print("Length of the linked list is :" ,link.LinkedList_length())

link.insert_values(["Durjoy","Mehlaching","Belal","Promi","Rubel"])
link.insert_At(0, "Akash")
link.insert_At(3, "Joya")
link.print()
"""
link.insert_values(["Durjoy","Mehlaching","Belal","Promi","Rubel"])
link.insert_after_value("Mehlaching" ,"Joya")
link.print()
link.remove_by_value("Promi")
link.print()

