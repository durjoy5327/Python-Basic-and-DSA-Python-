def Bubble_Sort(Array):
    n= len(Array)
    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if Array[j]>Array[j+1]:
                temp=Array[j]
                Array[j]=Array[j+1]
                Array[j+1]=temp
                swapped=True
        if not swapped:
            break



if __name__=='__main__':
    Array=[25,2,17,9,23,15,7,12,19,20,15]
    Bubble_Sort(Array)
    print(Array)