#Q. solve problem number 1 with WHILE loop .
n=int(input("enter your number:  "))
i=1

while(i<11):
    print(f"{n} x {i} = {n * i}")
    
    if n*i==70:
        break
    i+=1
        
    
    