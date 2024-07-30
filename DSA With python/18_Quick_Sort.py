def partion(Array , left ,right):
    pivot= Array[right]
    i=left-1
    for j in range(left, right):
        if Array[j]<=pivot:
            i+=1
            Array[j] , Array[i]= Array[i], Array[j]
    Array[i+1], Array[right]= Array[right], Array[i+1]

    return i+1



def Quick_Sort( Array, left, right ):
    if left<right:
        pivotIndex= partion(Array, left, right)
        Quick_Sort(Array, left, pivotIndex-1)
        Quick_Sort(Array, pivotIndex+1, right)





if __name__=='__main__':
    Array=[25,2,17,9,23,15,7,12,19,20,15]
    left=0
    right= len(Array)-1
    Quick_Sort(Array ,left,right)
    print(Array)