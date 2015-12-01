WORDLIST_FILENAME = "C:\edx_py\ProblemSet4\words.txt"

from ps4a import *

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def makeWord(hand, n, wordList):
    word_list = []
    for word in wordList:
        if isValidWord(word,hand,wordList) and len(word) <= n:
            word_list.append(word)
    return word_list
    
wordList = loadWords()
print makeWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1},6,wordList)