# QUESTION NO.4 A file contains a wrod "donkey" multiple times . You need to write a program to replace the word with ######

word = "donkey"
with open(f"File.txt")as f:
    content= f.read()
    contentnew =  content.replace(word,"######")
    print(contentnew)

with open(f"File.txt","w")as f:
    f.write(contentnew)   