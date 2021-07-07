class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        hash=0
        for char in key:
            hash+=ord(char)
        return hash % self.MAX

    def add(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val

    def delete(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

    def get(self,key):
        h=self.get_hash(key)
        print(self.arr[h])

h=HashTable()
h.add("March 6",210)
h.add("March 7",230)
h.delete("March 7")
h.add("March 5",330)
h.add("March 4",430)
h.get("March 6")
print(h.arr)
