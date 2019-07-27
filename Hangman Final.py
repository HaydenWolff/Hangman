###############################
##    Author: Hayden Wolff   ##
##      Date: 3/11/2018      ##
##  Description: Hangman.py  ##
###############################
import random # Allows to randomize the words from the category that is being guessed
food = ['pineapple','cucumber','celery','gingerbread','jellybeans','pumpernickel','watermelon','spaghetti','marshmallow','asparagus'] #List of words for the category of food
animals = ['bloodhound','chimpanzee','estemmenosuchus','kookaburra','hummingbird','clipspringer','pronghorn','woodpecker','rhinoceros','roadrunner'] #List of words for the category of animals
sports = ['mountaineering','taekkyeon','baguzhang','naginatajustu','soccer','hockey','baseball','basketball','dressage','goaltimate'] #List of words for the category of sports
WCI_Teachers = ['phone','grigorova','zhou','dumitrache','demopoulos','berdichevskaia','cotnareanu','gutfreund','danjoux','mavrodin'] #List of words for the category of teachers at westmount
usedLetters = "" #Empty string stat will store all letters guessed by the user
print("Welcome to my game!\nThis is a pretty standard game of hangman.\nYou will have 7 wrong attempts.\nThe rules are quite simple.") #First part of the introduction that introduces the user to the game
print("1. You may not guess more than 1 letter.\n2. You may not guess a number.\nIf you guess the same letter twice, do not worry! It will not make you lose an attempt.") #The rules of my game
print("You must choose between 4 categories that contain 10 words each.") #Tells the user that they will need to choose a category
print() #Used for spacing
def drawing1(): #The function for the initial Drawing of the Hangman Game when the user has no wrong guesses
    print()
    print(" __________________")
    print("|        |         ")
    print("|                  ")
    print("|                  ")
    print("|                  ")
    print("|                  ")
    print("|                  ")
    print("|                  ")
    print("-------------------")
    print()
def drawing2(): #The function for the second Drawing of the Hangman Game when the user has one wrong guess
    print()
    print(" __________________ ")
    print("|        |          ")
    print("|        0          ")
    print("|                   ")
    print("|                   ")
    print("|                   ")
    print("|                   ")
    print("|                   ")
    print("-------------------")
    print()
def drawing3(): #The function for the third Drawing of the Hangman Game when the user has two wrong guesses
    print()
    print(" __________________ ")
    print("|        |          ")
    print("|        0          ")
    print("|        |          ")
    print("|                   ")
    print("|                   ")
    print("|                   ")
    print("|                   ")
    print("-------------------")
    print()
def drawing4(): #The function for the fourth Drawing of the Hangman Game when the user has three wrong guesses
    print()
    print(" __________________  ")
    print("|        |           ")
    print("|        0           ")
    print("|       /|           ")
    print("|                    ")
    print("|                    ")
    print("|                    ")
    print("|                    ")
    print("-------------------")
    print()
def drawing5(): #The function for the fifth Drawing of the Hangman Game when the user has four wrong guesses
    print()
    print(" __________________  ")
    print("|        |           ")
    print("|        0           ")
    print("|       /|\          ")
    print("|                    ")
    print("|                    ")
    print("|                    ")
    print("|                    ")
    print("-------------------")
    print()
def drawing6(): #The function for the sixth Drawing of the Hangman Game when the user has five wrong guesses
    print()
    print(" __________________  ")
    print("|        |           ")
    print("|        0           ")
    print("|       /|\          ")
    print("|        |           ")
    print("|                    ")
    print("|                    ")
    print("|                    ")
    print("-------------------")
    print()
def drawing7(): #The function for the seventh Drawing of the Hangman Game when the user has six wrong guesses
    print()
    print(" __________________  ")
    print("|        |           ")
    print("|        0           ")
    print("|       /|\          ")
    print("|        |           ")
    print("|         \          ")
    print("|                    ")
    print("|                    ")
    print("-------------------")
    print()
def drawing8(): #The function for the last Drawing of the Hangman Game when the user has no more guesses left
    print()
    print(" __________________  ")
    print("|        |           ")
    print("|        X           ")
    print("|       /|\          ")
    print("|        |           ")
    print("|       / \          ")
    print("|                    ")
    print("|                    ")
    print("-------------------")
    print()
while True: #First loop in the game that forces the user to choose one of the four categories
    category = input("Pick a category: Food[F], Animals[A], Sports[S], WCI Teachers[W]: ") #Asks the user to input either the name of the topic or the first letter. 
    if category.upper() == "FOOD" or category.upper() == "F": #Checks to see if the inputted category by the user in capital letters is FOOD or the letter F
        secretWord = random.choice(food) #Sets the secret word to a random word from the list of words for the category food
        drawing1() #calls the function for the initial hangman drawing
        print("Hangman!") #Writes the word hangman just to make sure the user knows what game they are playing
        break #Removes the user from the first loop so they can continue on into the game
    elif category.upper() == "ANIMALS" or category.upper() == "A": #Checks to see if the inputted category by the user in capital letters is ANIMALS or the letter A
        secretWord = random.choice(animals) #Sets the secret word to a random word from the list of words for the category animals
        drawing1() #calls the function for the initial hangman drawing
        print("Hangman!") #Writes the word hangman just to make sure the user knows what game they are playing
        break #Removes the user from the first loop so they can continue on into the game
    elif category.upper() == "SPORTS" or category.upper() == "S": #Checks to see if the inputted category by the user in capital letters is SPORTS or the letter S
        secretWord = random.choice(sports) #Sets the secret word to a random word from the list of words for the category sports
        drawing1() #calls the function for the initial hangman drawing
        print("Hangman!") #Writes the word hangman just to make sure the user knows what game they are playing
        break #Removes the user from the first loop so they can continue on into the game
    elif category.upper() == "WCI TEACHERS" or category.upper() == "W": #Checks to see if the inputted category by the user in capital letters is WCI TEACHERS or the letter W
        secretWord = random.choice(WCI_Teachers) #Sets the secret word to a random word from the list of words for the category westmount teachers
        drawing1() #calls the function for the initial hangman drawing
        print("Hangman!") #Writes the word hangman just to make sure the user knows what game they are playing
        break #Removes the user from the first loop so they can continue on into the game
    else: #If the user does not input any of the required inputs then the user will be told their answer is invalid and then will be asked for another input until the answer fits the standards
        print() #Used for spacing
        print("Invalid input! Try Again!") #Informs the user that their input is invalid and asks them to try again
        print() #Used for spacing
for i in range(len(secretWord)): #Second loop in the code, i starts with the initial value of 0 and then increases to the value of the length of the secret word
    print("_",end=" ") #every time the variable i increases, there will be an underscore ( _ ) printed
attempts = 7 #Sets the value of attempts for the user to 7
missingLetters = len(secretWord) #Sets the variable of missing letter to the length of the secretword
while attempts>0: #Third loop in the code that only runs when the attempts are greater than 0 (main loop that runs the actual hangman game)
    guess = input("Enter a letter: ").lower() #asks the user for a guess and then converts it the letter to lowercase
    if guess.isdigit(): #Checks to see if the guess is a number
        print() #Used for spacing
        print("Invalid Input! Try Again!") #Informs the user that their input is invalid and asks them to try again
        print() #Used for spacing
        continue #forces the loop to start over and will ask for the user to input a letter once again
    elif 1 < len(guess) > 1: #checks to see if the guess is less than 1 letter or greater than 1 letter
        print() #Used for spacing
        print("Invalid Input! Try Again!") #Informs the user that their input is invalid and asks them to try again
        print() #Used for spacing
        continue #forces the loop to start over and will ask for the user to input a letter once again
    elif guess in usedLetters: #Checks to see if the guess has been already guessed
        if guess.isalpha(): #Checks to see if the already guessed guess is a letter
            print() #Used for spacing
            print("Try a letter that you havent used already!") #Informs the user that they have guessed the letter already and asks them to try one they havent guessed already
            print() #Used for spacing
        else: #If the guess isnt a letter it will run through this statement that will inform them that their guess is an invalid input
            print() #Used for spacing
            print("Invalid Input! Try Again!") #Informs the user that their input is invalid and asks them to try again
            print() #Used for spacing
            continue #forces the loop to start over and will ask for the user to input a letter once again
    elif guess.isalpha(): #Check to see if the guess is a letter
        usedLetters+=guess #Adds the guessed letter to the string of used letters
        if guess.lower() not in secretWord: #Checks to see if the lowercase guess is not in the secret word 
            attempts-=1 #subtracts 1 from attempts
            print() #Used for spacing
            print("You have:",attempts,"attempts remaining") #Informs the user of how many guesses they have remaining
        if attempts == 7: #Checks to see if the user has 7 attemtps left
            drawing1() #calls the function for the initial hangman drawing
        elif attempts == 6: #Checks to see if the user has 6 attempts left
            drawing2() #calls the function for the second hangman drawing
        elif attempts == 5: #Checks to see if the user has 5 attempts left
            drawing3() #calls the function for the third hangman drawing
        elif attempts == 4: #Checks to see if the user has 4 attempts left
            drawing4() #calls the function for the fourth hangman drawing
        elif attempts == 3: #Checks to see if the user has 3 attempts left
            drawing5() #calls the function for the fifth hangman drawing
        elif attempts == 2: #Checks to see if the user has 2 attempts left
            drawing6() #calls the function for the sixth hangman drawing
        elif attempts == 1: #Checks to see if the user has 1 attempt left
            drawing7() #calls the function for the seventh hangman drawing
        else: #If the attempts are not equal to the previously stated statements
            drawing8() #calls the function for the hung man (last hanman drawing)
        for i in secretWord.lower(): #Fourth loop in the code, i becomes the first letter in the word, runs through the loop then becomes the second letter and so on.
            if i in usedLetters: #Checks to see if the letter i is in used letters
                print(i,end=" ") #prints the letter in the word
                missingLetters-=1 #Subtracts 1 from missing letters for every time the guessed letter is in used letters
            else: #If i is not in used letters
                print("_",end=" ") #Prints underscores ( _ ) where there there is no guessed letter
    else: #If the inputted letter doesnt fall under any previous conditions
        print() #Used for spacing
        print("Invalid Input! Try Again!!") #Informs the user that their input is invalid and asks them to try again
        print() #Used for spacing
        continue #forces the loop to start over and will ask the user to input a letter once again
    print("Used Letters:",usedLetters) #Informs the user of their letters that they have already used
    print() #Used for spacing
    if missingLetters==0: #Checks to see if the value of missing letters is equal to 0
        print("Congrats! You Guessed it! The word was:", secretWord) #The game will be over and the user wil be informed that they have won and will be reinformed what the word was
        break #Ends the code
    else: #If missing letters is not equal to 0 it will run through this code
        missingLetters=len(secretWord) #Resets the value of missing letters to the length of the secret word.
if attempts == 0: #Checks to see if attempts are 0
    print("Too Bad! The Secret Word Was:",secretWord) #Informs the user the user that they lost and informs them of what the word was
    

