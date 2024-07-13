def print_pattern(n):
    for i in range(n):
        s=''
        for j in range(i+1):
            s+='*'
        print(s)




if __name__=='__main__':
    n= input('Enter a number for triangle:')
    print_pattern(int(n))z