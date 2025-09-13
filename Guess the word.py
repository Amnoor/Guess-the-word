# Guess the word
# A simple word guessing game where the player has to guess the correct word from a list of options within a limited number of tries.
# The game provides feedback on whether the guess is correct or incorrect and keeps track of the number of tries left.
# The game ends when the player guesses the correct word or runs out of tries.
# The game is designed to be played in a single round.
# I import the choice function from the random module to randomly select the answer from a list of choices.
from random import choice
# List of choices for the game
choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Randomly select the answer from the list of choices
Answer = choice(choices)
# Welcome message and instructions
print("Welcome to guess the word!")
print("You will be given 10 words you have to choose from and you have 9 tries to guess the correct word. one round only.")
# Display the list of choices to the player
print(f"""{choices[0]}. Apple
{choices[1]}. Phone
{choices[2]}. Chair
{choices[3]}. Bread
{choices[4]}. Window
{choices[5]}. Street
{choices[6]}. Paper
{choices[7]}. Cloud
{choices[8]}. Light
{choices[9]}. Door""")
# Prompt the player to enter their guess
guess = input("Enter your guess (letters only): ")
# Validate the input to ensure it is one of the allowed choices
while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
    if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
        print("Invalid input! Please enter again. (Letters only): ")
        guess = input("Enter your guess (letters only): ")
    else:
        break
# Check if the guess is correct and provide feedback
if guess.lower() not in Answer:
    print("Incorrect! you have 8 trie left")
    guess = input("Enter your guess (letters only): ")
    while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
        if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
            print("Invalid input! Please enter again. (Letters only): ")
            guess = input("Enter your guess (letters only): ")
        else:
            break
    if guess.lower() not in Answer:
        print("Incorrect! you have 7 trie left")
        guess = input("Enter your guess (letters only): ")
        while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
            if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                print("Invalid input! Please enter again. (Letters only): ")
                guess = input("Enter your guess (letters only): ")
            else:
                break
        if guess.lower() not in Answer:
            print("Incorrect! you have 6 trie left")
            guess = input("Enter your guess (letters only): ")
            while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                    print("Invalid input! Please enter again. (Letters only): ")
                    guess = input("Enter your guess (letters only): ")
                else:
                    break
            if guess.lower() not in Answer:
                print("Incorrect! you have 5 trie left")
                guess = input("Enter your guess (letters only): ")
                while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                    if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                        print("Invalid input! Please enter again. (Letters only): ")
                        guess = input("Enter your guess (letters only): ")
                    else:
                        break
                if guess.lower() not in Answer:
                    print("Incorrect! you have 4 trie left")
                    guess = input("Enter your guess (letters only): ")
                    while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                        if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                            print("Invalid input! Please enter again. (Letters only): ")
                            guess = input("Enter your guess (letters only): ")
                        else:
                            break
                    if guess.lower() not in Answer:
                        print("Incorrect! you have 3 trie left")
                        guess = input("Enter your guess (letters only): ")
                        while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                            if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                                print("Invalid input! Please enter again. (Letters only): ")
                                guess = input("Enter your guess (letters only): ")
                            else:
                                break
                        if guess.lower() not in Answer:
                            print("Incorrect! you have 2 trie left")
                            guess = input("Enter your guess (letters only): ")
                            while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                                if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                                    print("Invalid input! Please enter again. (Letters only): ")
                                    guess = input("Enter your guess (letters only): ")
                                else:
                                    break
                            if guess.lower() not in Answer:
                                print("Incorrect! you have 1 trie left")
                                guess = input("Enter your guess (letters only): ")
                                while not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                                    if not guess.strip().lower() == "a" and not guess.strip().lower() == "b" and not guess.strip().lower() == "c" and not guess.strip().lower() == "d" and not guess.strip().lower() == "e" and not guess.strip().lower() == "f" and not guess.strip().lower() == "g" and not guess.strip().lower() == "h" and not guess.strip().lower() == "i" and not guess.strip().lower() == "j":
                                        print("Invalid input! Please enter again. (Letters only): ")
                                        guess = input("Enter your guess (letters only): ")
                                    else:
                                        break
                                if guess.lower() not in Answer:
                                    print("Incorrect! You loose!")
                                else:
                                    print("Congratulations! You won!")
                            else:
                                print("Congratulations! You won!")
                        else:
                            print("Congratulations! You won!")
                    else:
                        print("Congratulations! You won!")
                else:
                    print("Congratulations! You won!")
            else:
                print("Congratulations! You won!")
        else:
            print("Congratulations! You won!")
    else:
        print("Congratulations! You won!")
else:
    print("Congratulations! You won!")