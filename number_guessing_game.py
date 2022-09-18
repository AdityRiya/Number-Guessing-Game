import random
top_number = input("Type a number: ")
# print(type(top_number))

if top_number.isdigit():
    top_number=int(top_number)
    if top_number <= 0 :
        print("Please ! Type a number which is larger than Zero")
        quit()
    # print(type(top_number))
else:
    print("Please ! Type a number.")
    quit()

guess = 1

random_number = random.randint(0,top_number)
while True:
    user_guess = input("Type your Guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        # print(type(user_guess))
    else:
        print("Please ! Type a number.")
        continue
    
    if user_guess == random_number:
        print("Your Guess Is  Correct!")
        break
    elif user_guess <= random_number:
        print("The Random Number Is Larger Than Your Guess.")
        guess +=1
    elif user_guess >= random_number:
        print("The Random Number Is Smaller Than Your Guess.")
        guess+=1
    else:
        quit()
        
    

print("You Guessed ",guess," times")