# Subtract guess if user gets right 
import random
from words import words

wordList = words
wordSplit = [i.capitalize() for i in random.choice(wordList)]
wordDashes = []
usedLetters = set()
guess = 0

for i in wordSplit:
  wordDashes.append('-')
print(''.join(wordDashes))

while guess <= 6:
  wordIndexes = list(enumerate(wordSplit))
  userInput = input('\nPlease Enter Letter Guess:').capitalize()

  if userInput in usedLetters:
    print('Already Used')
    guess -= 1
    
  if userInput in wordSplit:  
    for i in range(0, len(wordSplit)):
      if wordIndexes[i][1] == userInput:
        wordDashes.pop(i)
        wordDashes.insert(i, userInput) 
  else:
    guess += 1
    if len(userInput) == 1:
      usedLetters.add(userInput)

  if ''.join(wordSplit) == ''.join(wordDashes):
    print(f'You won! You lost {guess} lives! The word was {"".join(wordDashes)}\n')
    break
    
  print(f'Not In Word: {", ".join(usedLetters)}')
  print(f"\n{''.join(wordDashes)}")
  print(f'Lives Remaining: {7 - abs(guess)}')
  
if guess > 6:
  print(f'The Word was {"".join(wordSplit)}!, Try Again.')  