# Generator is a simply way to create iterator


def Remote_Control_Next():
    yield "Hi"
    yield "Hello"
    yield "Hey"


itr= Remote_Control_Next()
print(next(itr))
print(next(itr))
print(next(itr))

#otherwise we can make a loop for print
print('\n\nFor loop: ')
for c in Remote_Control_Next():
    print(c)


# Now implementing fibonacci series 

def fibo():
    a ,b = 0 , 1
    while(True):
        yield a
        a ,b =b ,a+b
        
for f in fibo():
    if f>50:
        break
    print(f)
