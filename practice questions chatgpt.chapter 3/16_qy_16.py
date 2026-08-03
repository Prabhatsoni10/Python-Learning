# Write a program to find all spaces in the following string and print their index positions:
text = "Prabhat is a good boy"
for index,character in enumerate(text):
    if character == " ":

        print(index)