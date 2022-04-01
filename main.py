# Hangman 
# Dashed List Letters
# Insert at specifc position relative to 
# ex: if count of i > 1, find multiple indexes of letter, replace, continue 
# .pop() index at the same index and then insert

import random
wordList = ['MISSISSIPPI']
wordSplit = [i for i in random.choice(wordList)]
wordDashes = []
letterUsed = []
guess = 0

# Creates List of dashes 
for i in wordSplit:
  wordDashes.append('-')

while guess < len(wordSplit) + 1:
  wordIndexes = list(enumerate(wordSplit))
  userInput = input('Please Enter Letter Guess: ')
  guess += 1
  # Enumerate pairs values with indexes 
  # Replace contents of wordDashes with userGuess
  if userInput in wordSplit:
    for i in range(0, len(wordSplit)):
      if wordIndexes[i][1] == userInput:
        wordDashes.pop(i)
        wordDashes.insert(i, userInput)
  if ''.join(wordSplit) == ''.join(wordDashes):
    print(f'You won! It took {guess} Tries. The word was {"".join(wordDashes)}')
    break
  print(''.join(wordDashes))
  