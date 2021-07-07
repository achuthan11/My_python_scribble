class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.MAX

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val

    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

    def __getitem__(self,key):
        h=self.get_hash(key)
        print(self.arr[h])

h=HashTable()
h["March 6"]=210
h["March 7"]=230
del h["March 7"]
h["March 5"]=330
h["March 4"]=430
h["March 5"]
print(h.arr)
