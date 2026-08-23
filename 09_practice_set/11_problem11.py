# QUESTION NO .11 : write a python program to rename a file to "renamed_by_python.txt"
with open (f"old.txt")as f:
   content= f.read()

with open(f"renamed_by_python.txt","w")as f :
   f.write(content)
   