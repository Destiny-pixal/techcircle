import random 

#number guessing 

#generate random number between 1 and 100
number_to_guess = random.randint(1,100)
attempt = 0
print("welcome to the Number Guessing Game")
print("guess a number between 1 and 100 ")
while True:
    user_guess = int(input("Enter a number "))
    if user_guess <  number_to_guess:
        print(" Too low! Try again")
    elif user_guess > number_to_guess:
        print(" Too high! Try again")
    else:
        print("Congratulations! You guessed the number")