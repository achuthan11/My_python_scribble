class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circularLL:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data)
        node.next=self.head
        temp=self.head
        if self.head is not None:
            while(temp.next!=self.head):
                temp=temp.next
            temp.next=node
        else:
            node.next=node
        self.head=node

    def insert_at_end(self,data):
        node=Node(data)
        if self.head is not None:
            temp=self.head
            while True:
                if temp.next!=self.head:
                    temp=temp.next
                else:
                    break
            temp.next=node
        else:
            self.head=node
        node.next=self.head

    def count(self):
        if self.head is None:
            return 0
        num=1
        temp=self.head
        while temp.next!=self.head:
            num+=1
            temp=temp.next
        return num


    def insert_at_pos(self,data,pos):
        if pos>self.count():
            print("Wrong Index")
            return
        else:
            if pos==1:
                self.insert_at_begining(data)
            else:
                node=Node(data)
                temp=self.head
                for i in range(pos-2):
                    temp=temp.next
                node.next=temp.next
                temp.next=node

    def print(self):
        if self.head is None:
            print("Circular linkded list is empty")
        else:
            st=""
            st+=str(self.head.data)+"->"
            temp=self.head.next
            while temp!=self.head:
                st+=str(temp.data)+"->"
                temp=temp.next
        print(st)


if __name__ == '__main__':
    cll=circularLL()
    cll.insert_at_begining(3)
    cll.insert_at_begining(2)
    cll.insert_at_begining(1)
    cll.insert_at_end(4)
    cll.insert_at_end(5)
    cll.insert_at_pos(6,3)
    cll.print()
    print(cll.count())
