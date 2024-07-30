def LinearSearch(Array, value):
    n= len(Array)
    for i in range(n):
        if Array[i]==value:
            return i
    return -1

def BinarySearch(Array ,value):
    left=0
    right= len(Array)-1
    while left<=right:
        mid= left+ (right-left)//2
        if Array[mid]==value:
            return mid
        elif Array[mid]<value:
            left=mid+1
        else:
            right=mid-1
    return -1


if __name__=='__main__':
    Array=[2,5,6,9,10,15,20,25,26,28,29,38]
    target= 28
    t=BinarySearch(Array , target)
    print(f"The index of {target} is {t}" if t>=0 else "Not found")
    