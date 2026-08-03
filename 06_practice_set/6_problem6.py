#Write a programto calculate the marks of students undr the scheme:
#90-100->Ex
#2. 80-90 -> A
# 3. 70-80 -> B
# 4. 60-70 ->c
# 5. 60-50 ->d
# 6. <50 -> fail 


marks=float(input("enter your marks : "))
if(marks<=100 and marks>=90):
    print("grade Ex")
elif(marks<=90 and marks>=80):
    print("grade A")
elif(marks<=80 and marks>=70):
    print("grade B")
elif(marks<=70 and marks>=60):
    print("grade C")  
elif(marks<=60 and marks>=50):
    print("D")   
elif(marks <50):
    print("Fail") 
else:    
     print("invalid marks")