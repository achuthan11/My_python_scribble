class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.MAX

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        found=False
        for index,element in enumerate(self.arr[h]):
            if element[0]==key:
                found=True
                self.arr[h][index]= (key,val)
                break
        if not found:
            self.arr[h].append((key,val))

    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=[]

    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                print(element[1])
                break

    def print(self):
        for key in self.arr:
            print(*key)

h=HashTable()
h["March 6"]=210
h["March 7"]=230
del h["March 7"]
h["March 5"]=330
h["March 4"]=430
h["March 20"]=500
h["March 21"]=600
h["March 22"]=700
h["March 23"]=800
h["March 24"]=900
h["March 25"]=100
h["March 10"]=123
h["March 11"]=124
h["March 12"]=125
h["March 5"]
h["March 11"]
h["March 6"]=220
h.print()
