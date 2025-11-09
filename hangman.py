import random

"""
Function containing main logic of the hangman game.
"""

def hangman():

    try:
        with open('longWords.txt', 'r') as f:
            words = [w.strip() for w in f if w.strip()]
    except FileNotFoundError:
        print("File 'longWords.txt' not found.")
        return

    if not words:
        print("No words in 'longWords.txt'.")
        return

    word_to_guess = random.choice(words).upper()
    sign_list = ['_' for i in word_to_guess]
    wrong_guess_counter = 0
    max_attempts = 10

    print(f"Word to be guessed: ")
    print(' '.join(sign_list))

    while '_' in sign_list and wrong_guess_counter < max_attempts:
        letter_guess = input("Pass a letter: ").upper()[0]

        if letter_guess in sign_list:
            print(f"Letter already guessed.")
            print(' '.join(sign_list))
            continue

        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter_guess:
                sign_list[i] = letter_guess
                continue
        if not letter_guess in word_to_guess:
                wrong_guess_counter += 1
                print(f"Wrong guess. Remaining attempts: {max_attempts - wrong_guess_counter}.")
        print(' '.join(sign_list))

        if not '_' in sign_list:
            print(f"Congrats, you've won!")

        if wrong_guess_counter == max_attempts:
            print(f"You've lost, too many incorrect guesses.")
            print(f"The word was: {word_to_guess}")

    print(word_to_guess)