# learn flashcards
# CLI for flashcards bc I have AP bio to study

import sys
import random
fileName = sys.argv
answer = None
right = 0
wrong = 0
print("⭑･ﾟﾟ･*:༅｡.｡༅:*ﾟ:*:✼✿  Quizlet sucks  ✿✼:*:༅｡.｡:*･ﾟﾟ･⭑\n")
print("Make sure the text file separates definitions from vocabulary using a tab!")
print(fileName)
print("Type quit, q, or close to leave!")

if len(fileName) == 1:
    fileName = input("Enter file name containing vocab words: ")
else:
    fileName = fileName[1]
file = open(fileName, "r")
termsList = file.read().splitlines()


def quiz(correct, incorrect):
    line = random.choice(termsList)
    separator = line.index("\t")
    term = line[0:separator]
    key = line[separator+1:len(line)]

    answer = input("Match the correct term with: " + term + " ")
    if answer.strip(" ") == key.strip(" "):
        correct+=1
        print("Correct! Here's the next one:")
    else:
        print("Incorrect, term does not match")
        print("Correct term is: " + key)
        override = input("Override, I was correct. y/N ?")
        if override == "y":
            correct+=1
            print("Incorrect answer overriden, correct score increased by 1.")
        else:
            incorrect +=1
            print("Answer not overriden, try again next time!")

    print("\nCorrect terms: " , correct , " Incorrect terms: " , incorrect , "\n")


def quit():
    file.close() 
    exit()


def game(right,wrong):
    while(answer !=  "quit" or "q" or "close" ):
        quiz(right, wrong)
    quit()

game(right, wrong)
