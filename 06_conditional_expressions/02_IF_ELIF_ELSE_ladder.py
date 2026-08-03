a = int(input("Enter your age: "))

if a < 0:
    print("Hey! Negative age is not valid.")

elif a == 0:
    print("0 is not a valid age.")

elif a <= 5:
    print("Go study, kid!")

elif a >= 16:
    print("You are eligible for this consent.")

else:
    print("You are below the age of consent.")

print("End of program.") 