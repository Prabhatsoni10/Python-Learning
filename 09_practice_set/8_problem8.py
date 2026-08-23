# QUESTION NO. 8 : Write a program to make a copy of text file "this.txt"
with open (f"this.txt")as f:
   content = f.read()

with open (f"thiscopy.txt","w") as f:
   f.write(content)
