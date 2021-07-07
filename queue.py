'''s=[]
s.insert(0,1)
s.insert(0,2)
s.insert(0,3)
s.insert(0,4)
print(*s)
s.pop()
print(*s)'''
#using deque from collections to make efficient as it uses DoublyLinkedList structure
from collections import deque
class queue:
    def __init__(self):
        self.q=deque()
    def enqueue(self,val):
        self.q.appendleft(val)
    def dequeue(self):
        return self.q.pop()
    def peek(self):
        print(self.q[-1])
    def is_empty(self):
        return len(self.q)==0
    def print(self):
        print(self.q)
    def size(self):
        print(len(self.q))
if __name__ == '__main__':
    que=queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)
    que.peek()
    que.print()
    print(que.is_empty())
    print("The removed ele is : ",que.dequeue())
    que.print()
    que.size()
