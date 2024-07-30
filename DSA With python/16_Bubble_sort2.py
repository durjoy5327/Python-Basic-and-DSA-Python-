def Bubble_Sort(Array ,key=None):
    n= len(Array)
    for i in range(n-1):
        swapped=False
        for j in range( n-1-i):
            a= Array[j][key]
            b= Array[j+1][key]
            if a>b:
                temp=Array[j][key]
                Array[j][key]= Array[j+1][key]
                Array[j+1][key] =Array[j][key]
        if not swapped:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    Bubble_Sort(elements, key='transaction_amount')
    print(elements)