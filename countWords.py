import os
import operator

def listdir_fullpath(d):
    #Function to create the full path of the directory or file given
    return [os.path.join(d, f) for f in os.listdir(d)]

def getWordFiles(rootDir):
    #Function to retrieve the txt files from the given directory and any further subdirectories
    #This function will return a list with the full path file names of each txt file
    dirList = [rootDir]
    fileList = []
    while(len(dirList)!=0):
        for i in listdir_fullpath(dirList.pop()):
            if(os.path.isdir(i)):
                dirList.append(i)
            else:
                fileList.append(i)
    return fileList

def countWords(fileList):
    #Function to count occurrences of words in a series of txt files provided in a list
    #This function will return a dictionary where the structure is {"word", number of occurrences}
    words = {}
    for i in fileList:
        wordFile = open(i, "r+")
        for word in wordFile.read().split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
    return words

def sortWords(wordList):
    #Function to sort a dictionary of words and their occurrences
    #The function will sort the keys by their value and return a list of tuples
    # The sorted list will be in Descending Order
    return sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)

def displayTop10(wordList):
    #Function to display the top 10 words and the number of occurrences
    #If less than 10 words exist in all of the txt files then the top x number of words will be displayed with x being the number of words that exist
    displayCount = 10
    if (len(wordList)<10):
        displayCount = len(wordList)

    for i in range(displayCount):
        print( str((i+1))+ ". "+ wordList[i][0] + "("+str(wordList[i][1])+" times)")

#Ask the user for the path of the root directory
#Keep asking until they provide a valid path
pathname = ""
while (os.path.isdir(pathname)==False):
    pathname = input('Enter a valid directory path: ')

fileList = getWordFiles(pathname)
words = countWords(fileList)
words = sortWords(words)
displayTop10(words)

