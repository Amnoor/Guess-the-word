import random
choices = ["Apple", "Phone", "Chair", "Bread", "Window", "Street", "Paper", "Cloud", "Light", "Door"]
Answer = random.choice(choices)
print("Welcome to guess the word!")
print("You will be given 10 words you have to choose from and you have 9 tries to guess the correct word. one round only.")
print(f"""a. {choices[0]}
b. {choices[1]}
c. {choices[2]}
d. {choices[3]}
e. {choices[4]}
f. {choices[5]}
g. {choices[6]}
h. {choices[7]}
i. {choices[8]}
j. {choices[9]}""")
guess = input("Enter your guess (letters only):")
if not guess.lower() == "a":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "a":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "b":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "b":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "c":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "c":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "d":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "d":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "e":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "e":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "f":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "f":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "g":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "g":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "h":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "h":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "i":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "i":
            invalid_state = False
        else:
            invalid_state = True
elif not guess.lower() == "j":
    invalid_state = True
    while invalid_state:
        print("Invalid! It is not in the choices! (letters only)")
        guess = input("Enter your guess (letters only):")
        if guess.lower() == "j":
            invalid_state = False
        else:
            invalid_state = True
elif guess not in Answer:
    print("Incorrect! you have 8 trie left")
    guess = input("Enter your guess (letters only):")
    if guess not in Answer:
        print("Incorrect! you have 7 trie left")
        guess = input("Enter your guess (letters only):")
        if not guess.lower() == "a":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "a":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "b":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "b":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "c":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "c":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "d":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "d":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "e":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "e":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "f":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "f":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "g":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "g":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "h":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "h":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "i":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "i":
                    invalid_state = False
                else:
                    invalid_state = True
        elif not guess.lower() == "j":
            invalid_state = True
            while invalid_state:
                print("Invalid! It is not in the choices! (letters only)")
                guess = input("Enter your guess (letters only):")
                if guess.lower() == "j":
                    invalid_state = False
                else:
                    invalid_state = True
        elif guess not in Answer:
            print("Incorrect! you have 6 trie left")
            guess = input("Enter your guess (letters only):")
            if not guess.lower() == "a":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "a":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "b":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "b":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "c":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "c":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "d":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "d":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "e":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "e":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "f":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "f":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "g":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "g":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "h":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "h":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "i":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "i":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif not guess.lower() == "j":
                invalid_state = True
                while invalid_state:
                    print("Invalid! It is not in the choices! (letters only)")
                    guess = input("Enter your guess (letters only):")
                    if guess.lower() == "j":
                        invalid_state = False
                    else:
                        invalid_state = True
            elif guess not in Answer:
                print("Incorrect! you have 5 trie left")
                guess = input("Enter your guess (letters only):")
                if not guess.lower() == "a":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "a":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "b":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "b":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "c":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "c":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "d":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "d":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "e":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "e":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "f":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "f":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "g":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "g":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "h":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "h":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "i":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "i":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif not guess.lower() == "j":
                    invalid_state = True
                    while invalid_state:
                        print("Invalid! It is not in the choices! (letters only)")
                        guess = input("Enter your guess (letters only):")
                        if guess.lower() == "j":
                            invalid_state = False
                        else:
                            invalid_state = True
                elif guess not in Answer:
                    print("Incorrect! you have 4 trie left")
                    guess = input("Enter your guess (letters only):")
                    if guess not in Answer:
                        print("Incorrect! you have 3 trie left")
                        guess = input("Enter your guess (letters only):")
                        if guess not in Answer:
                            print("Incorrect! you have 2 trie left")
                            guess = input("Enter your guess (letters only):")
                            if guess not in Answer:
                                print("Incorrect! you have 1 trie left")
                                guess = input("Enter your guess (letters only):")
                                if guess not in Answer:
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