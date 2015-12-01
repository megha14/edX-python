# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\edx_py\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = False
    for letter in secretWord:
        if letter in lettersGuessed:
            flag = True
        else:
            flag = False
            break
    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    let = ""
    for letter in secretWord:
        if letter not in lettersGuessed:
            let += "_ "
        else:
            let += letter
    return let


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    let = "abcdefghijklmnopqrstuvwxyz"
    let1 =""
    for letter in let:
        if letter not in lettersGuessed:
            let1 += letter
    return let1

def letterInWord(secretWord, letter):
    if letter in secretWord:
        return True
    else:
        return False

def letterinList(letter, alist):
    if len(alist) == 0:
        return False
    elif letter in alist:
        return True
    else:
        return False

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
 
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    lettersGuessed = []
    num_choices = 8
    print "Welcome to the game Hangman!"
    print "I am thinking of the word that is "+str(len(secretWord))+" letters long."
    print "-------------"
    while(num_choices>=1):
        print "You have "+str(num_choices)+" guesses left."
        print "Available Letters: "+getAvailableLetters(lettersGuessed)
        user_input = raw_input("Please guess a letter: ")
        us_in = user_input.lower()                      
        if letterinList(us_in,lettersGuessed):
            print "Oops! You've already guessed that letter: "+getGuessedWord(secretWord,lettersGuessed)
            print "-------------"
        elif letterInWord(secretWord,us_in):
            lettersGuessed.append(us_in)
            print "Good guess: "+getGuessedWord(secretWord,lettersGuessed)
            print "-------------"
            
        elif not letterInWord(secretWord,us_in):
            lettersGuessed.append(us_in)
            print "Oops! That letter is not in my word: "+getGuessedWord(secretWord,lettersGuessed)
            print "-------------"
            num_choices -= 1
        if isWordGuessed(secretWord, lettersGuessed) and num_choices>=1:
            print "Congratulations, you won!"
            break
            
    if num_choices==0:
        print "Sorry, you ran out of guesses. The word was "+secretWord
        
            
            



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
