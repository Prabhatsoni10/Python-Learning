#Write a program to find out wheter a student is passed or failed ,if it requiers a total of 40% and minimum of 33% in3 subjects ,
# assume there are 3 subjects and take marks frm each students. 

marks1 = int(input("Enter your marks: "))
marks2= int(input("enter your marks: ")) 
marks3= int(input("Enter your marks :"))

# Check for total percentage:
Total_percentage=(100)* (marks1+marks2+marks3)/300
if(Total_percentage>=40 and marks1>33 and marks2>33 and marks3>33 ):
    print("Congratulations you are passed",Total_percentage)
else:
    print("you failed, try again next year! ,thank you.",Total_percentage)    
       
