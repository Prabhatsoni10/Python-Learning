'''
Factrial(0)=1
Factrial(1)=1
Factrial(2)=2x1
Factrial(3)=3x2x1
Factrial(4)=4x3x2x1
factorial(5)=5x4x3x2x1
Fcatorial(n)= n*(n-1).........3x2x1


factorial=nxfactorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
     return 1
    return n*factorial(n-1)


n=int(input("enter you number:  "))
print(f"The Factorial of the number is: {factorial(n)}")