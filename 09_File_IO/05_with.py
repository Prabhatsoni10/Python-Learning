f = open("file.txt")
print((f.read()))
f.close()

#THE SAME CAN BE WRITTEN USEN THE STATEMENT LIKE THIS 
with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file     

