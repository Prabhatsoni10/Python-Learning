#Write a program to fill the following template using replace()
#letter = '''
#Dear <|name|>,
#Welcome to our Python course.
#Your joining date is <|date|>.
#'''
letter = '''
Dear <|name|>,
Welcome to our Python course.
Your joining date is <|date|>.
'''
print(letter.replace ("<|name|>","prabhat").replace("<|date|>","8 july 2026"))
