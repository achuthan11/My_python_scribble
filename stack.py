'''s=[]
s.append(1)
s.append(2)
s.append(3)
s.append(4)
print(*s)
s.pop()
print(*s)'''
#using deque from collections to make efficient as it uses DoublyLinkedList structure
from collections import deque
class stack:
    def __init__(self):
        self.container=deque()
    def append(self,val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def peek(self):
        print(self.container[-1])
    def is_empty(self):
        return len(self.container)==0
    def print(self):
        print(self.container)
    def size(self):
        print(len(self.container))
if __name__ == '__main__':
    st=stack()
    st.append(1)
    st.append(2)
    st.append(3)
    st.peek()
    st.print()
    print(st.is_empty())
    st.pop()
    st.size()
