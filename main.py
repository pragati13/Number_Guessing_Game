#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1,100)
print(f"Pssst, the correct answer is {random_number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
  n = 10
  while n > 0:
    print(f"You have {n} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    if guess_number < random_number:
      print("Too low.")
      print("Guess again.")
      n = n - 1
    elif guess_number > random_number:
      print("Too high.")
      print("Guess again.")
      n = n - 1
    elif guess_number == random_number:
      print(f"You got it! The answer was {guess_number}.")
      exit(0)
elif level == "hard":
  n = 5
  while n > 0:
    print(f"You have {n} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))
    if guess_number < random_number:
      print("Too low.")
      print("Guess again.")
      n = n - 1
    elif guess_number > random_number:
      print("Too high.")
      print("Guess again.")
      n = n - 1
    elif guess_number == random_number:
      print(f"You got it! The answer was {guess_number}.")
      exit(0)
else:
  print("Please enter valid input...")
  exit(0)

print("You've run out of guesses, you lose.")