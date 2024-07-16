"""
implementing stack using deque

Just for fun
"""
from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    
    def Push(self, value):
        return self.container.append(value)
    
    def Pop(self):
        return self.container.pop()
    
    def Peek(self):
        return self.container[-1]
    
    def Size(self):
        return len(self.container)
    
    def is_empty(self):
        return self.size()==0
    
    def Print(self):

        while self.container:
            k= self.container.pop()
            print(k)
            

st= Stack()
st.Push(25)
st.Push(50)
st.Push(75)
st.Push(100)
st.Push(125)
st.Print()



