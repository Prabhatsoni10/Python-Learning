# write a program of finding the greatest number of four numbers enterd by the user .
a=int(input("enter your number 1: "))
b=int(input("enter your number 2: "))
c=int(input("enter your number 3: "))
d=int(input("enter your number 4: ")) 
if(a>b and a>c and a>d):
    print("greatest number is a ",a)
elif(b>a and b>c and b>d):
    print("greatest number is b",b)
elif(c>a and c>b and c>d):
    print("greatest number is c ",c)    
else:print("greatest number is d ",d)