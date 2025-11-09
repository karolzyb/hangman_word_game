
'''
Function to filter words from words.txt source file 
by the defined lenght in range from min_len 
and save them to longwords.txt output file.
'''

def filter_words():
    
    while True:
        try:
            min_len = int(input("Pass minimal length of words to be filtered and used in the game: "))
            if min_len < 0:
                print("Pass only positive numbers.")
                continue
            break
        except ValueError:
            print("Pass only integer value.")
        except KeyboardInterrupt:
            print("\nCanceled by user.")
            return

    with open('words.txt', 'r') as wordsFile, open('longWords.txt', 'w') as longWordsFile:
        for i in wordsFile:
            if len(i.strip()) >= min_len:
                longWordsFile.write(i)

    print(f'Minimal word lenght selected: {min_len} characters.')