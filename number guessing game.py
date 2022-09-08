import random
top_of_range=input("Type a number:  ")
if top_of_range.isdigit():
 top_of_range=int(top_of_range)
 if top_of_range<=0:
    print("Please type a number more than 0 next time")
    quit()
else:
    print("Type a number next time.")
random_number=random.randint(0,top_of_range)#random_number=random.randrange(-5,11)  doesnt include 11 if we changed to randint it will be cover 11 as well
guesses=0
while True:
    guesses+=1  
    user_guess=input("Type a number:  ")
    if user_guess.isdigit():
     user_guess=int(user_guess)
    else:
     print("Type a number next time.")
     continue

    if user_guess==random_number:
        print("You got it!")
        break
    elif user_guess>random_number:
        print("You are below the number")
    else:
        print("You are under the number")
print(f"You got it in {guesses} guesses.")