
from itertools import product
import math

## alter list creation to comprehension


list_words = open("allowed_words.csv", 'r')
allWords_n = list_words.readlines()



all_words = [] 
for word in allWords_n:
    all_words.append(word.strip("\n"))

list_words.close()
allWordList = all_words
forFrequencytest = allWordList
LetterFrequencyDict = {}
newList = []
alphabet = "abcdefghijklmnopqrstuvwxyz"



def collection_andManipulation(word, data_states, newList): #pass another parameter that is the list of words
    global allWordList
    for position in range(0, 5):
        if data_states[position] == "correct":
            target = word[position]
            #newList = correct_letterCount(target, position, newList)
            newList = [word for word in newList if (target == word[position])]

        elif data_states[position] == "present":
            target = word[position]
            #newList = present_letterCount(target, position, newList)
            newList = [word for word in newList if (target in word) and (target != word[position])]


        elif data_states[position] == 'absent':
            target = word[position]
            #newList = absent_letterCount(target, newList)
            newList = [word for word in newList if (target not in word)]
            
            #print(newList)
            
        elif data_states[position] == "absentAtPosition":
            target = word[position]
            #newList = absent_atPosition(target, position, newList)
            newList = [word for word in newList if (target not in word[:position] or (target not in word[position:])) and (target != word[position])]
            #eliminate at position

    #print(newList)
    return newList
    #print(len(present_words))  



# using list comprehension 
def present_letterCount(target, position, startList): #modifiers
    #global allWordList
    #alteredList = []
    #for word in startList:
        
        #if (target in word) and (target != word[position]):
            #alteredList.append(word)
    alteredList = [word for word in startList if (target in word) and (target != word[position])]
    #print(present_words)
    #print(len(present_words))
    return alteredList


def correct_letterCount(target, position, startList): #modifiers #changed empty presentwords to altered list adn returing altered list
    #startList usually would be present words except for use in calculating expected value
    #alteredList = []
    #for word in startList:   
        #if (target == word[position]):
            #alteredList.append(word)
    alteredList = [word for word in startList if (target == word[position])]
    #print(present_words)
    #print(len(present_words))
    return alteredList

def absent_letterCount(target, startList):
    #global present_words
    #alteredList = []
    #for word in startList:
        #if (target not in word):
            #alteredList.append(word)
    alteredList = [word for word in startList if (target not in word)]
    return alteredList


def absent_atPosition(target, position, startList):
    #alteredList = []
    #for word in startList:
        #if (target not in word[:position] or (target not in word[position:])) and (target != word[position]):
            #alteredList.append(word)
    alteredList = [word for word in startList if (target not in word[:position] or (target not in word[position:])) and (target != word[position])]
    #print(present_words)
    #print(len(present_words))
    return alteredList


#eliminate at the position 
def checkForDouble(word, data_states): #buffer function 
   for i in range(0,len(word)-1):
    #print(word[i+1:len(word)])
    for j in range(i+1,len(word)):
        if word[i] == word[j]:
            if data_states[i] == "absent":
                data_states [i] = "absentAtPosition"

            elif data_states[j] == "absent":
                data_states[j] = "absentAtPosition"


def sorting_frequencyCounter(List): #sorts by maximum present
    #counting
    for i in alphabet:
        counter = 0 
        for j in List:
            if (i in j):
                counter += 1
        LetterFrequencyDict.update({i:counter})

    LetterFrequency2 = LetterFrequencyDict.copy()
    sortedLetterFrequency = {}
    #sorting
    while LetterFrequencyDict:
        maxValue = list(LetterFrequencyDict.values())[0]
        for key in LetterFrequencyDict:
            value = LetterFrequencyDict.get(key)
            if value >= maxValue:
                maxValue = value
                maxKey = key
        sortedLetterFrequency.update({maxKey:maxValue})
        LetterFrequencyDict.pop(maxKey)

    print(sortedLetterFrequency)
    return sortedLetterFrequency
#print(wordFrequency)
weary_state = ['correct', 'absent', 'absent', 'absent', 'absent']
soare_state = ['absent','absent', 'absent', 'absent', 'absent']
slate_state = ['correct','correct','absent', 'absent', 'absent']
tares_state = ["absent", "absent", "present", "correct", "absent"]

weary = "weary" 
soare = "crane"
slate = "slate"
tares = "tares"

possible_states = ["absent", "correct", "present", "correct", "present"]
allCorrectState = ('correct','correct','correct','correct', 'correct')
allAbsents = ('absent','absent','absent','absent', 'absent')
allStateList = []

def information(prevSize, currSize):
    probability = (currSize/prevSize) 
    information = math.log(1/probability, 2)
    expected = probability * information
    #for me to see
    #print("infromation is: {}".format(information))
    #print("probability:{}".format(probability*100))
    return expected


def all_combinations(iterable, size):

   return list(product(iterable, repeat= size))

def allPossibleStates(): #updates a list of tuples of all states - all correct
    counter = 0
    for i in all_combinations(possible_states, 5):
        if i in allStateList or (i is allCorrectState):
            continue
        allStateList.append(i) 
    #print(i)
        counter+=1
   # print(allStateList)
    return allStateList

#sorting_frequencyCounter(allWordList)
prevSize = len(allWordList)
#print(prevSize)
newList = collection_andManipulation(soare, soare_state, allWordList)
print(len(newList))
#updatedDict = sorting_frequencyCounter(newList) #new dictianry 
currSize = len(newList)
#print(currSize)

#firstround
expected = information(prevSize,currSize)

# calculating the expected value
def expectedValue(word, wordList, allStateList): #operates on allStateList
    global expected
    expected = 0
    counter = 0
    for data_state in allStateList:
        #print(data_state)
        counter+=1
        #if data_state == allAbsents:
            #print("\nhere!\n")
        try:
            #if (data_state == returnedState):
                #continue
            prevSize = len(wordList)
            newList1 = collection_andManipulation(word, data_state, wordList)
            currSize = len(newList1)
            exp = information(prevSize, currSize)
            expected = exp + expected
        except ZeroDivisionError:
            continue
    #print(counter)
    #print(expected)
    return expected

def evaluatingGuess(allWordList, allStates):
    infoDict = {}
    counte = 0
    for i in allWordList:
        counte += 1
        value = expectedValue(i, allWordList, allStates)
        infoDict.update({i:value})
        print(counte)
    
    sortedInfoDict = {}

    while infoDict:
        maxValue = list(infoDict.values())[0]
        for key in infoDict:
            value = infoDict.get(key)
            if value >= maxValue:
                maxValue = value
                maxKey = key
        sortedInfoDict.update({maxKey:maxValue})
        infoDict.pop(maxKey)
    
    print(sortedInfoDict)
    return sortedInfoDict



evaluatingGuess(allWordList, allPossibleStates())
#should check through dectionary 
        
#after each guess you detect, evaluate (collect&manipulate)

