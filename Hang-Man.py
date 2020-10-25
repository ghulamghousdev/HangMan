# Both the additional tasks are done in C part
# 1. New game functionality
# 2. Printed physical representation of Hangman

def printBody(guesses):
    if(guesses == 6):
        print("\n")
        print("\t\t            /'''\\")
        print("\t\t           / * * \\")
        print("\t\t           |  ^  |")
        print("\t\t            \\ - /")
        print("\t\t             000")
        print("\t\t            0 0 0")
        print("\t\t           0  0  0")
        print("\t\t          0   0   0")
        print("\t\t         0    0    0")
        print("\t\t        0     0     0")
        print("\t\t       00     0     00")
        print("\t\t              0       ")
        print("\t\t             0 0      ")
        print("\t\t            0   0     ")
        print("\t\t           0     0    ")
        print("\t\t          0       0   ")
        print("\t\t         0         0  ")
        print("\t\t        0           0 ")
        print("\t\t       000         000")
        print("\n")
    elif(guesses == 5):
        print("\n")
        print("\t\t            /'''\\")
        print("\t\t           / * * \\")
        print("\t\t           |  ^  |")
        print("\t\t            \\ - /")
        print("\t\t             00")
        print("\t\t            0 0 ")
        print("\t\t           0  0  ")
        print("\t\t          0   0   ")
        print("\t\t         0    0    ")
        print("\t\t        0     0     ")
        print("\t\t       00     0     ")
        print("\t\t              0       ")
        print("\t\t             0 0      ")
        print("\t\t            0   0     ")
        print("\t\t           0     0    ")
        print("\t\t          0       0   ")
        print("\t\t         0         0  ")
        print("\t\t        0           0 ")
        print("\t\t       000         000")
        print("\n")
        
    elif(guesses == 4):      
        print("\n")
        print("\t\t            /'''\\")
        print("\t\t           / * * \\")
        print("\t\t           |  ^  |")
        print("\t\t            \\ - /")
        print("\t\t              0")
        print("\t\t              0 ")
        print("\t\t              0  ")
        print("\t\t              0   ")
        print("\t\t              0    ")
        print("\t\t              0     ")
        print("\t\t              0     ")
        print("\t\t              0       ")
        print("\t\t             0 0      ")
        print("\t\t            0   0     ")
        print("\t\t           0     0    ")
        print("\t\t          0       0   ")
        print("\t\t         0         0  ")
        print("\t\t        0           0 ")
        print("\t\t       000         000")
        print("\n")
    elif(guesses == 3):      
        print("\n")
        print("\t\t            /'''\\")
        print("\t\t           / * * \\")
        print("\t\t           |  ^  |")
        print("\t\t            \\ - /")
        print("\t\t              0")
        print("\t\t              0 ")
        print("\t\t              0  ")
        print("\t\t              0   ")
        print("\t\t              0    ")
        print("\t\t              0     ")
        print("\t\t              0     ")
        print("\t\t              0       ")
        print("\t\t               0      ")
        print("\t\t                0     ")
        print("\t\t                 0    ")
        print("\t\t                  0   ")
        print("\t\t                   0  ")
        print("\t\t                    0 ")
        print("\t\t                   000")
        print("\n")
    elif(guesses == 2):      
        print("\n")
        print("\t\t            /'''\\")
        print("\t\t           / * * \\")
        print("\t\t           |  ^  |")
        print("\t\t            \\ - /")
        print("\t\t              0")
        print("\t\t              0 ")
        print("\t\t              0  ")
        print("\t\t              0   ")
        print("\t\t              0    ")
        print("\t\t              0     ")
        print("\t\t              0     ")
        print("\t\t              0       ")
        print("\t\t                     ")
        print("\n")
    elif(guesses == 1):      
        print("\n")
        print("\t\t            /'''\\")
        print("\t\t           / * * \\")
        print("\t\t           |  ^  |")
        print("\t\t            \\ - /")
        print("\t\t              ")
        print("\n")


def chooseRandomWord(listOfWords):
    import random
    while True:
        word = (''.join(random.choices(listOfWords)))
        print(word) # just for practise purposes the word is printed
        guessed = []
        falseGuesses = []
        chances = 6
        while (chances>0):
            clue = ""
            wordGuessed = ""
            for letter in word:
                if letter in guessed:
                    clue = clue + letter+" " # this word is used as we need to print the gussed word as - - - - - 
                    wordGuessed = wordGuessed + letter # To store letters to check if the word is guessed or not
                else:
                    clue = clue + "_ "
                    wordGuessed = wordGuessed + "-"
            if (wordGuessed == word):
                break
            printBody(chances)
            print("Guess a letter in the word:", clue)
            guessedChar = input()
            if (guessedChar in guessed or guessedChar in falseGuesses):
                print("Already guessed",guessedChar)
            elif (guessedChar in word):
                print("Correct Guess!")
                guessed.append(guessedChar)
            else:
                print("Incorrect Guess!")
                chances = chances - 1
                falseGuesses.append(guessedChar)
        if (chances>0):
            print("Congratulations you guessed the word:", word)
        else:
            print("You couldn't guess the word",word)
        print("Press 1 if you want to start new game and for exit press any number other than 1")
        flag = int(input())
        if(flag != 1):
            break
            

                

def main():
    listOfWords = ['APPLE', 'BILBO', 'CHORUSED', 'DISIMAGINE','ENSURING', 'FORMALISING', 'GLITCHES',
                   'HARMINE', 'INDENTATION', 'JACKED', 'KALPACS', 'LAUNDRY', 'MASKED', 'NETTED',
                   'OXFORD', 'PARODY', 'QUOTIENTS', 'RACERS', 'SADNESS', 'THYREOID', 'UNDUE',
                   'VENT', 'WEDGED', 'XERIC', 'YOUTHHOOD', 'ZIFFS']
    chooseRandomWord(listOfWords)
if __name__ == "__main__":
    main()



