f =  open("myfile2.txt")

lines =f.readlines()

print(lines,type(lines))
f.close()

# YOU CAN ALSO WRITE THESE CODES WITH AN ANOTHER WAY 
#f =  open("myfile2.txt")


# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

# line5 = f.readline()
# print(line5,type(line5))
# f.close()

# THIS IS A VERY LOMG PROCESS I WROTE IT BECUASE OF KNOWELEDGE.
# WE CAN DO THIS WITH WHILE LOOP
f =  open("myfile2.txt")
line = f.readline()
while(line!=""):
    print(line)
    line = f.readline()


f.close()    








