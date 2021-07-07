def insertion_sort(ele):
    for i in range(1,len(ele)-1):
        anchor=ele[i]
        j=i-1
        while j>=0 and anchor<ele[j]:
            ele[j+1]=ele[j]
            j-=1
        ele[j+1]=anchor

if __name__=='__main__':
    ele=[50,30,60,10,40,20,90,80,70]
    insertion_sort(ele)
    print(ele)
