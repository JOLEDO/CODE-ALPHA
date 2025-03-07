import random

word_bank = [
    "apple", "brave", "crisp", "dance", "eagle", "flame", "grape", "haste", "ideal", "jolly",
    "knack", "latch", "mango", "novel", "ocean", "plant", "quilt", "risky", "spice", "table",
    "unity", "vivid", "waste", "xenon", "yacht", "zebra", "angle", "beach", "charm", "drift",
    "elite", "frost", "globe", "heart", "inbox", "joker", "koala", "lunar", "music", "nerve",
    "optic", "piano", "quiet", "rider", "smile", "tiger", "urban", "vowel", "whale", "yield"
]
guess_lives = 3

print("Welcome to the hangman game 2025 👏👏👏")
index = random.randint(0, 49)
running = False


def start():
    global running
    global guess_lives
    rand_word = word_bank[index]
    word = [letter for letter in word_bank[index]]
    blank = ["_" for letter in word_bank[index]]
    print(blank)
    print(f"You have {guess_lives} lives"
          f"")
    line = " ".join(blank)
    while running:
        if guess_lives <= 0:
            print(f"you have exhausted all your lives, the word is {rand_word}")
            running = False

            print(f"{guess_lives} lives left....")
        elif guess_lives > 0:
            print(line)
            if "_" not in blank:
                print(f"You have successfully guessed the word '{word}' 😎")
            else:
                guess = input("Guess a letter: ")
                if guess in rand_word:
                    pos = rand_word.index(guess)
                    blank[pos] = guess
                    print(blank)
                elif guess in line:
                    print("You have already guessed this letter.")
                else:
                    print(f"{guess} is not in the word")
                    guess_lives -= 1
                    print(f"{guess_lives} lives left....")
        else:
            break


on = True
while on:
    running = True
    start()
    choice = input("Do you want to try again?(Y/N)").lower()
    if choice == "y":
        guess_lives = 3
        start()
    elif choice == "n":
        print("Thank you for playing the game, do have a nice day...")
        on = False
    else:
        print("Invalid command")
