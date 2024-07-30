def Insertion_Sort(Array):
    n= len(Array)
    for i in range( 1, n):
        key= Array[i]
        j=i-1
        while j>=0 and Array[j]>key:
            Array[j+1]=Array[j]
            j=j-1
        Array[j+1]=key


    




if __name__=='__main__':
    Array=[25,2,17,9,23,15,7,12,19,20,15]
    Insertion_Sort(Array )
    print(Array)