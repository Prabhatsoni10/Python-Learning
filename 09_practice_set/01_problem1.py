# QUESTION 1) Wrte a program to read a text from a given file 'poem.txt' and find out wheter it contains the word 'twinkle' and how many times
f = open("poem.txt")
content= f.read()
count = content.lower().count("twinkle")
print(count)
if("twinkle"in content):
    print("twinkle is in poem.txt")
else:
    print("twinkle is not  in poem.txt")

f.close()

