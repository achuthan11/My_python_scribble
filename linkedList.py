class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head==None:
            print("Linked list is empty ")
            return
        itr=self.head
        llstr=""
        while itr:
            if itr:
                llstr+= str(itr.data) + "-->"
            itr=itr.next
        llstr+="NULL"
        print(llstr)

    def insert_at_end(self,data):
        node=Node(data,None)
        if self.head == None:
            self.head=node
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=node

    def insert_multiple(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def count_list(self):
        count=0
        itr=self.head
        while  itr:
            count+=1
            itr=itr.next
        return(count)

    def insert_at_pos(self,index,data):
        if index==0:
            self.insert_at_begining(data)
            return
        if index<0 or index>self.count_list():
            raise Exception("Invalid Index")
        if index==self.count_list():
            self.insert_at_end(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                return
            itr=itr.next
            count+=1
    def remove(self,index):
        if index<0 or index>self.count_list():
            raise Exception("Invalid Index")
        count=0
        itr=self.head
        while itr:
            if(count==index-1):
                itr.next=itr.next.next
            itr=itr.next
            count+=1

    def replace_at_pos(self,index,data):
        self.remove(index)
        self.insert_at_pos(index,data)

    def swap(self,index1,index2):
        itr=self.head
        count=0
        while itr:
            if count==index1-1:
                data1=itr.data
                break
            itr=itr.next
            count+=1
        itr1=self.head
        count1=0
        while itr1:
            if count1==index2-1:
                data2=itr1.data
                break
            itr1=itr1.next
            count1+=1
        self.remove(index1-1)
        self.insert_at_pos(index1-1,data2)
        self.remove(index2-1)
        self.insert_at_pos(index2-1,data1)
        return

    def search(self,data):
        itr=self.head
        count=0
        while itr:
            if itr.data==data:
                return count
            itr=itr.next
            count+=1
        raise Exception("No data found as you asked")

    def insert_after_value(self,prev_value,data):
        if self.search(prev_value) or self.search(prev_value)==0:
            pass
        itr=self.head
        count=0
        while itr:
            if itr.data==prev_value:
                node=Node(data,itr.next)
                itr.next=node
                return
            itr=itr.next
            count+=1

    def remove_by_value(self,data):
        if self.search(data) or self.search(data)==0:
            pass
        itr=self.head
        if self.head.data==data:
            self.head=self.head.next
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
            itr=itr.next


if __name__ == '__main__':
    ll=LinkedList()
    ll.insert_at_begining(3)
    ll.insert_at_begining(2)
    ll.insert_at_begining(1)
    ll.print()
    ll.insert_at_end(4)
    ll.print()
    ll.insert_multiple([5,6,7])
    ll.print()
    ll.insert_at_pos(3,8)
    ll.print()
    ll.remove(3)
    ll.print()
    ll.replace_at_pos(4,11)
    ll.print()
    ll.swap(3,4)
    ll.print()
    print(ll.count_list())
    print("Found at position ",ll.search(4))
    ll.insert_after_value(1,12)
    ll.print()
    ll.remove_by_value(1)
    ll.print()
