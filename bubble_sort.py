#Efficient way of using bubble sort if an list of sorted elements are given
print("Click 1 for simple bubble sort")
print("Click 2 for store problem")
m= int(input())
if m==1:
    ls=list(map(int,input().split()))
    n=len(ls)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if ls[j]>ls[j+1]:
                tmp=ls[j]
                ls[j]=ls[j+1]
                ls[j+1]=tmp
                swapped=True
        if not swapped :
            break
    print(*ls)
#The bubble sort without swap flag will be in O(n^2),but with the flag and if the given array is not completely in a descending order, it can save time and space complexity is O(1)
if m==2:
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    print("There are name,transaction_amount,device keys to sort the data")
    st=input()
    for i in range(len(elements)-1):
        swapped=False
        for j in range(len(elements)-1-i):
            if elements[j][st]>elements[j+1][st]:
                temp=elements[j][st]
                elements[j][st]=elements[j+1][st]
                elements[j+1][st]=temp
                swapped=True
        if not swapped:
            break
    print(elements)
