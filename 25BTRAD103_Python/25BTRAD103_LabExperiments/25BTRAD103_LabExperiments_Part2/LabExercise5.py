
import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess == number:
    print("Correct! You guessed the number.")
elif guess > number:
    print("Your guess is too high.")
else:
    print("Your guess is too low.")

print("The correct number was:", number)
