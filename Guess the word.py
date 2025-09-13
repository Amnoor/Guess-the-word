# A simple guess the word game with 10 choices and 9 tries.
# First I will import the random module to randomly select a word from the list of choices.
import random
# Then I will create a list of 10 choices.
choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Then I will randomly select a word from the list of choices.
Answer = random.choice(choices)
# Then I will Welcome the user to the game and explain the rules.
print("Welcome to guess the word!")
print("You will be given 10 words you have to choose from and you have 9 tries to guess the correct word. one round only.")
# Then I will display the list of choices to the user.
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
# Then I will ask the user to enter their guess.
guess = input("Enter your guess (letters only): ")
# Then I will check if the user's input is valid (letters only).
while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
    if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
        print("Invalid input! Please enter again. (Letters only): ")
        guess = input("Enter your guess (letters only): ")
    else:
        break
# Then I will check if the user's guess is correct or not and give them 9 tries, and also check in each if statement if the input is valid or not.
if guess.lower() not in Answer:
    print("Incorrect! you have 8 trie left")
    guess = input("Enter your guess (letters only): ")
    while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
        if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
            print("Invalid input! Please enter again. (Letters only): ")
            guess = input("Enter your guess (letters only): ")
        else:
            break
    if guess.lower() not in Answer:
        print("Incorrect! you have 7 trie left")
        guess = input("Enter your guess (letters only): ")
        while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
            if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                print("Invalid input! Please enter again. (Letters only): ")
                guess = input("Enter your guess (letters only): ")
            else:
                break
        if guess.lower() not in Answer:
            print("Incorrect! you have 6 trie left")
            guess = input("Enter your guess (letters only): ")
            while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                    print("Invalid input! Please enter again. (Letters only): ")
                    guess = input("Enter your guess (letters only): ")
                else:
                    break
            if guess.lower() not in Answer:
                print("Incorrect! you have 5 trie left")
                guess = input("Enter your guess (letters only): ")
                while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                    if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                        print("Invalid input! Please enter again. (Letters only): ")
                        guess = input("Enter your guess (letters only): ")
                    else:
                        break
                if guess.lower() not in Answer:
                    print("Incorrect! you have 4 trie left")
                    guess = input("Enter your guess (letters only): ")
                    while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                        if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                            print("Invalid input! Please enter again. (Letters only): ")
                            guess = input("Enter your guess (letters only): ")
                        else:
                            break
                    if guess.lower() not in Answer:
                        print("Incorrect! you have 3 trie left")
                        guess = input("Enter your guess (letters only): ")
                        while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                            if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                                print("Invalid input! Please enter again. (Letters only): ")
                                guess = input("Enter your guess (letters only): ")
                            else:
                                break
                        if guess.lower() not in Answer:
                            print("Incorrect! you have 2 trie left")
                            guess = input("Enter your guess (letters only): ")
                            while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                                if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                                    print("Invalid input! Please enter again. (Letters only): ")
                                    guess = input("Enter your guess (letters only): ")
                                else:
                                    break
                            if guess.lower() not in Answer:
                                print("Incorrect! you have 1 trie left")
                                guess = input("Enter your guess (letters only): ")
                                while not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
                                    if not guess.lower() == "a" and not guess.lower() == "b" and not guess.lower() == "c" and not guess.lower() == "d" and not guess.lower() == "e" and not guess.lower() == "f" and not guess.lower() == "g" and not guess.lower() == "h" and not guess.lower() == "i" and not guess.lower() == "j":
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