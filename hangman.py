# tasks guessing game

# 0
# Hangman-0.png
# Word:	hangman
# Guess:	E
# Misses:
# 1
# Hangman-1.png
# Word:	_ _ _ _ _ _ _
# Guess:	T
# Misses:	e
# 2
# Hangman-2.png
# Word:	_ _ _ _ _ _ _
# Guess:	A
# Misses:	e, t
# 3
# Hangman-2.png
# Word:	_ A _ _ _ A _
# Guess:	O
# Misses:	e, t

# option+ cmd + L
import re


def check_whole_answer(arrayOfGuessAnswer, answer):
    strArray = ''.join(arrayOfGuessAnswer)  # convert list to string
    if strArray == answer:
        return True  # it is in the array, stop
    else:
        return False  # not in the array, just going


def insert_answer(arrayOfGuessAnswer, guess, answer):
    for n, i in enumerate(answer):  # n returns number, i return the character
        if guess in i:
            arrayOfGuessAnswer[n] = guess


def check_input(guess):
    checkCharacter = False
    while not checkCharacter:
        guess = input("please guess a letter \n")
        if not re.match("[a-z]", guess):
            print("Invalid character!")
            checkCharacter = False
        elif len(guess) > 1:
            print("only a single character is allowed!")
            checkCharacter = False
        else:
            checkCharacter = True
            return guess


# initial
answer = "hangman" # declare the answer, convert the answer to no space and small letter
answer = answer.lower() # lowercase
answer = answer.replace(" ", "") # no space
miss_time = 0
MAX_ESTIMATED_TIME = 6
arrayOfGuessAnswer = []
for a in range(len(answer)):
    arrayOfGuessAnswer.append("_")
print(arrayOfGuessAnswer)
setOfMissAnswer = set()
guess = ""
print("hangman begin! \n")
print("Chances : ", MAX_ESTIMATED_TIME)
while not check_whole_answer(arrayOfGuessAnswer, answer) and miss_time < MAX_ESTIMATED_TIME:  # not only refer to the first condition
    guess = check_input(guess)
    if guess in answer:
        insert_answer(arrayOfGuessAnswer, guess, answer)
        print(arrayOfGuessAnswer)
    else:
        setOfMissAnswer.add(guess)
        print("you guessed it wrong!")
        print(setOfMissAnswer)
        miss_time += 1
        print("remaining chance : ",  MAX_ESTIMATED_TIME - miss_time)

if miss_time >= 6:
    print("you lose!")
else:
    print("you win!, end game")
