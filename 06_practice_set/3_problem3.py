#A spam comment is defind as a text containg following keyword :
# "make a lot of money", "buy now", "subscribe this","click this" 

p1= "make a lot of money "
p2="buy now"
p3="subscribe this "
p4= "click this"

meassage= input("enter your comments: ")

if((p1 in meassage)or(p2 in meassage)or(p3 in meassage)or (p4 in meassage)):
    print("this comment is a spam")



else:
    print("this comment is not a spam") 
