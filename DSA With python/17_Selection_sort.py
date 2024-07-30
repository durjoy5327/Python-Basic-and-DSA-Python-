def Selection_sort( Array):
    n= len(Array)
    for i in range(n-1):
        minindx= i  
        for j in range(i+1,n): 
            if Array[minindx]>Array[j]:
                minindx=j
        if minindx!=i:
            temp=Array[i]
            Array[i]=Array[minindx]
            Array[minindx]=temp




if __name__=='__main__':
    Array=[25,2,17,9,23,15,7,12,19,20,15]
    Selection_sort(Array)
    print(Array)