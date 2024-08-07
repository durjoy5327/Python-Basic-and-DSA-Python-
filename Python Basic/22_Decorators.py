
#mainly decorator is use for wrap a function into another function


#frist approach here we can see that in each function some line repeated that's mean these function are 
#not decorated we can decorate these and can reduce some line which are similar to both function
import time


def square_number(numbers):
    start= time.time()
    result=[]
    for i in numbers:
        result.append(i*i)
    end= time.time()
    print(f"Execution of square function take time:{str(end-start)*1000} mil sec")
    return result

def cube_number(numbers):
    start= time.time()
    result=[]
    for i in numbers:
        result.append(i*i*i)
    end= time.time()
    print(f"Execution of square function take time:{str(end-start)*1000} mil sec")
    return result


if __name__=='__main__':
    numbers= range(1,1000)
    square_number(numbers)
    cube_number(numbers)


#This is final approach using decoratos

import time

# Decorator to time functions
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution of {func.__name__} took {(end - start) * 1000:.2f} ms")
        return result
    return wrapper

@timing
def square_number(numbers):
    result = [i * i for i in numbers]
    return result

@timing
def cube_number(numbers):
    result = [i * i * i for i in numbers]
    return result

if __name__ == '__main__':
    numbers = range(1, 1000)
    square_number(numbers)
    cube_number(numbers)
