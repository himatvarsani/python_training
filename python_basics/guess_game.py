import random
import time
# We want the input to be an int and not a string
# This would input a string
# guess = input ("What is your guess?: ")

# We need to an input as an int
print("Hi! Welcome to the guessing game. Please guess a number between 1 to 100.")
time.sleep(3)
print("Picking a number....")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1, 100)
guess_count = 1

# While loop - a combination of a if statement and a for loop
while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong Guess! You need to guess higher, What is your guess?: "))
    else:
        guess = int(input("Wrong Guess! You need to guess lower, What is your guess?: "))

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")