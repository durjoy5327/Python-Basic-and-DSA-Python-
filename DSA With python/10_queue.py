from collections import deque

"""
q= deque()
q.appendleft(25)
q.appendleft(30)
q.appendleft(35)
q.appendleft(40)
q.appendleft(45)


while q:
    print(q.pop())

    """
class Queue:
    def __init__(self):
        self.container= deque()
    
    def enqueue(self, value):
        self.container.appendleft(value)
    
    def dequeue(self):
        self.container.pop()

    def isempty(self):
        return len(self.container)==0

    def print(self):
        while self.container:
            print(self.container.pop())


Q= Queue()
Q.enqueue(25)
Q.enqueue(30)
Q.enqueue(35)
Q.enqueue(40)
Q.enqueue(45)
Q.enqueue(50)
Q.enqueue({
    'Company': 'Wal Mart',
    'Timestamp':'27 july 6:20PM',
    'Price': '130$'
})
Q.dequeue()

Q.print()






    
