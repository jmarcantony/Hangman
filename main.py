import os
import time
import random
from words import words
from art import logo, steps

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_missing_values(word, guessed_letters):
    string = ""
    for x in word:
        if x not in guessed_letters:
            string += "_"
        else:
            string += x
    return string

def check_valid(word, guess):
    if guess in word:
        return True
    else:
        return False

def check_game_over(missing_values):
    game_over = True

    for x in missing_values:
        if x == "_":
            game_over = False
            break 
    return game_over

def main():
    word = random.choice(words)
    guessed_letters = []
    curr_step = 0
    win = False
    while True:
        clear()
        print(steps[curr_step])
        missing_values = get_missing_values(word, guessed_letters)
        print(f"Guessed Word: {missing_values}")
        guess = input("\n[*] Enter a guess: ")
        guessed_letters.append(guess)
        valid = check_valid(word, guess)
        if not valid:
            curr_step += 1
            print("\nIncorrect Letter\n")
            time.sleep(0.3)
        missing_values = get_missing_values(word, guessed_letters)
        over = check_game_over(missing_values)
        if curr_step == 6:
            clear()
            break
        elif over:
            clear()
            win = True
            break

    missing_values = get_missing_values(word, guessed_letters)
    print("---- GAME OVER ----")
    print(steps[curr_step])
    print(f"Guessed Word: {missing_values}")
    if win:
        print("\nYOU WIN!\n")
    else:
        print(f"\nYOU LOSE!\nThe word was: {word}\n")

if __name__ == "__main__":
    print(logo)
    try:
        input("\n[*] PRESS ENTER TO START!")
        clear()
        main()
    except KeyboardInterrupt:
        print("\nQuitting...\n")
        quit()