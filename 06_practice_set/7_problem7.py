# write a program that finds out wheter the post (entered by user )is talking about prabhat or not .

post=input("enter your comment:  ")
if("prabhat" in post.upper()):
    print("this post is talkking about prabhat")
if("prabhat" in post.lower()):
    print("this post is talking about prabhat")

else:
    print("this post is not talking about prabhat ")    