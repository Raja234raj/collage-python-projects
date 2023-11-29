import random

range_of_number = input("type a number: ")

if range_of_number.isdigit():
    range_of_number = int(range_of_number)
    
    if range_of_number <= 0:
        print("Enter the number that is greater than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()
    
random_number = random.randint(0, range_of_number)

guesess = 0

while True:
    guesess += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time.")
        continue
    if user_guess == random_number:
        print("you got it!!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You are below the number")
        
print("you got it in", guesess,"guesess")