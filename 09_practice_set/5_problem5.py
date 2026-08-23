# QUESTION NO. 5  Repaet the program 4 for a list fo such words to be censored
words = ["idiot","donkey","fool","thief"]
with open (f"prob5.txt")as f:
    content = f.read()
    for word in words:
        content = content.replace(word,"#"*len(word))


with open (f"prob5.txt","w")as f :
    f.write(content)    
