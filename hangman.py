import random

wordsFile = open('longWords.txt').read().splitlines()
wordToGuess = random.choice(wordsFile).upper()
# wordToGuess = input("Pass a word to be guessed: ").upper()

signList = ['_' for i in wordToGuess]
isWin = False
wrongGuessCounter = 0
totalPossibleAttempts = 10

print(f"Word to be guessed: ")
print(signList)

while (isWin == False and wrongGuessCounter < totalPossibleAttempts):

    letterGuess = input("Pass a letter: ").upper()[0]

    if letterGuess in signList:
        print(f"Letter already guessed.")
        print(signList)
        continue

    lengthOfWord = len(wordToGuess)
    for i in range(lengthOfWord):
        if wordToGuess[i] == letterGuess:
            signList[i] = letterGuess
            continue
    if not letterGuess in wordToGuess:
            wrongGuessCounter += 1
            print(f"Wrong guess. Remaining wrong guesses: {totalPossibleAttempts - wrongGuessCounter}.")
    print(signList)

    if not '_' in signList:
        isWin = True
        print(f"Congrats, you've won!")

    if wrongGuessCounter == totalPossibleAttempts:
        print(f"You've lost, too many incorrect guesses.")

print(wordToGuess)