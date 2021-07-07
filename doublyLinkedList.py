class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head,None)
        if self.head==None:
            self.head=node
            return
        self.head.prev=node
        self.head=node

    def print(self):
        if self.head==None:
            print("No element in the list ")
            return
        itr=self.head
        st=""
        while itr:
            if(itr.next==None):
                st+=str(itr.data)
            else:
                st+=str(itr.data)+"-->"
            itr=itr.next
        print(st)

    def print_backward(self):
        last=self.last_node()
        itr=last
        st=""
        while itr:
            if itr.prev!=None:
                st+=str(itr.data)+"-->"
            else:
                st+=str(itr.data)
            itr=itr.prev
        print(st)

    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data,None,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)

    def remove_at_pos(self,index):
        count=0
        itr=self.head
        while itr:
            if(count==index):
                itr.prev.next=itr.next
                if itr.next:
                    itr.next.prev=itr.prev
                    break
            itr=itr.next
            count+=1

    def pop(self):
        if self.head==None:
            print("No element in the list")
            return
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None

    def insert_multiple(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def count_list(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count

    def last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr

if __name__ == '__main__':
    dll=DoublyLinkedList()
    dll.insert_at_begining(3)
    dll.insert_at_begining(2)
    dll.insert_at_begining(1)
    dll.print()
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    dll.print()
    dll.remove_at_pos(2)
    dll.print()
    dll.pop()
    dll.print()
    dll.insert_multiple([5,6,7])
    dll.print()
    print(dll.count_list())
    dll.print_backward()
