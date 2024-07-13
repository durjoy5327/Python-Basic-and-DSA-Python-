"""
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
"""
OddNumberslist=[]
def OddNumbers(maxnumber):
    for i in range(1 , maxnumber+1):
        if i%2==1:
            OddNumberslist.append(i)


if __name__=='__main__':
    maxnumber=input('Enter a number to print odd numbers: ')
    maxnumber=int(maxnumber)
    OddNumbers(maxnumber)
    print("Odd numbers are:" ,OddNumberslist)