# QUESTION NO. 7 :
#Write a program to find out the line number where python is present.
with open(f"dummy7.txt")as f :
    lines = f.readlines()
lineno= 1 
for line in lines:
        

 if("python"in line):
    print(f"yes python is in the lineno:{lineno} ")   
  
    break
 lineno+=1   

else:
    print("no!,python is not in the string ")