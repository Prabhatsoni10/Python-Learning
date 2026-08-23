import random

def game():
    print("you are playing the game.. ")
    score = random.randint(1,10000)
    #
    with open ("hiscore.txt")as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore = 0



    print(f"yourscore:{score}") 
    if(score>hiscore):
        #write the score to te file 
        with open("hiscore.txt","w")as f:
            f.write(str(score))

    return score

game()           

     



    