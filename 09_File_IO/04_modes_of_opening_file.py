#r = openfor reading 
# w = open for writing
# a = open for appending
# +- = open for updating
# 'rb' will open for read in binary mode 
# 'rt' will open for read in text mode 


# EXAMPLE OF 'a' :
st="prabhat you have done a good job"
f = open("myfile.txt","a") #IT ADD THE ORIGINALL TEXT ("ST") x TIMES YOU RUN THE CODE,after running the cod you can see that teh same cdoe will print in that fie 
f.write(st)
f.close()
