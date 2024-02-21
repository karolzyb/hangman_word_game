wordsFile = open('words.txt')
longWordsFile = open('longWords.txt', 'w')

for i in wordsFile:
    if len(i)>6:# and len(i)<6:
        # print(i)
        longWordsFile.write(i)

wordsFile.close()
longWordsFile.close()