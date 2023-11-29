print("welcome to quiz game".upper().center(145))

playing = input("Do you want to play: ").lower()
if playing == "no":
    quit()
print("ok let's play :)")
score = 0

#question 1

answer = input("Full form of CPU?: ").lower()
if answer == "central processing unit":
    print("Its correct answer :)")
    score += 1
else:
    print("incorrect answer !!")

#question2

answer2 = input("Full Form of GPU: ").lower()
if answer2.lower() == "graphic processing unit":
    print("Its correct answer :)")
    score += 1
else:
    print("incorrect answer !!")

#question3

answer3 = input("Full Form of RAM: ").lower()
if answer3 == "random access memory":
    print("Its correct answer :)")
    score += 1
else:
    print("incorrect answer !!")

print("YOU GOT "+ str(score) + " QUESTIONS CORRECT")
print("YOU GOT "+ str((score/3)*100)+"%")

