# QUESTION NO. 9 : write a program to find out whether 2 fles have the same content or not?
with open (f"this.txt")as f:
   content1= f.read()

with open(f"dummy7.txt")as f:
   content2=f.read()

if(content1==content2):
   print("yes these files are identical  ")

else:
   print("no these files not identical")   