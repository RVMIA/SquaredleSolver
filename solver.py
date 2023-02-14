
def stripIndex(word):
    a = word.split(" ")
    return a[0]


def indexWord(inputWord):
    word = inputWord
    outputWord = []
    for i in range(len(inputWord)):
        letterIndexes = []
        for j in range(puzzleSize):
            for k in range(puzzleSize):
                if word[i] == puzzle[j][k]:
                    letterIndexes.append(word[i] + coordToIndex(j, k))
        outputWord.append(letterIndexes)
    output = []
    for i in range(len(inputWord)-1):
        lasttwo = []
        for j in range(len(outputWord[-2])):
            for k in range(len(outputWord[-1])):
                lasttwo.append(outputWord[-2][j] + " " + outputWord[-1][k])
        del outputWord[-2]
        del outputWord[-1]

        outputWord.append(lasttwo)
    outputWord = outputWord[0]
    output = []
    for i in range(len(outputWord)):
        outword = []
        word = outputWord[i].split()
        for j in range(len(word)):
            if set(word[j]).issubset(letters) is False:
                outword.append(word[j])
        outword.insert(0, inputWord)
        output.append(' '.join(outword))
    return output


def hasNoDuplicates(word):
    returnedWord = word
    a = word.split(" ")
    del a[0]
    if len(a) == len(set(a)):
        return returnedWord


def coordToIndex(j, k):
    return " " + str(((j*puzzleSize)+(k))+1)


def printWordList(a):
    print(a)
    print(len(a))
    print((float(int(1000 * float(len(a)/len(words)))))/10)

def getDict():
    with open("wordList.txt") as f:
        return f.read().split()

def isAdjacent(word):
    returnedWord = False
    a = word.split(" ")
    for k in range(len(a)-2):
        i = k + 1
        j = i + 1
        if puzzleSize == 3:
            if a[i] == '1' and (a[j] == '2' or a[j] == '4' or a[j] == '5'):
                returnedWord = True
            elif a[i] == '2' and (a[j] == '1' or a[j] == '3' or a[j] == '4' or a[j] == '5' or a[j] == '6'):
                returnedWord = True
            elif a[i] == '3' and (a[j] == '2' or a[j] == '5' or a[j] == '6'):
                returnedWord = True
            elif a[i] == '4' and (a[j] == '1' or a[j] == '2' or a[j] == '5' or a[j] == '7' or a[j] == '8'):
                returnedWord = True
            elif a[i] == '5' and (a[j] == '1' or a[j] == '2' or a[j] == '3' or a[j] == '4' or a[j] == '6' or a[j] == '7' or a[j] == '8' or a[j] == '9'):
                returnedWord = True
            elif a[i] == '6' and (a[j] == '2' or a[j] == '3' or a[j] == '5' or a[j] == '8' or a[j] == '9'):
                returnedWord = True
            elif a[i] == '7' and (a[j] == '4' or a[j] == '5' or a[j] == '8'):
                returnedWord = True
            elif a[i] == '8' and (a[j] == '4' or a[j] == '5' or a[j] == '6' or a[j] == '7' or a[j] == '9'):
                returnedWord = True
            elif a[i] == '9' and (a[j] == '5' or a[j] == '6' or a[j] == '8'):
                returnedWord = True
            else:
                return False
                break

        if puzzleSize == 4:
            if a[i] == '1' and (a[j] == '2' or a[j] == '5' or a[j] == '6'):
                returnedWord = True
            elif a[i] == '2' and (a[j] == '1' or a[j] == '3' or a[j] == '5' or a[j] == '6' or a[j] == '7'):
                returnedWord = True
            elif a[i] == '3' and (a[j] == '2' or a[j] == '6' or a[j] == '7' or a[j] == '8' or a[j] == '4'):
                returnedWord = True
            elif a[i] == '4' and (a[j] == '3' or a[j] == '7' or a[j] == '8'):
                returnedWord = True
            elif a[i] == '5' and (a[j] == '1' or a[j] == '2' or a[j] == '6' or a[j] == '9' or a[j] == '10'):
                returnedWord = True
            elif a[i] == '6' and (a[j] == '1' or a[j] == '2' or a[j] == '3' or a[j] == '5' or a[j] == '7' or a[j] == '9' or a[j] == '10' or a[j] == '11'):
                returnedWord = True
            elif a[i] == '7' and (a[j] == '2' or a[j] == '3' or a[j] == '4' or a[j] == '6' or a[j] == '8' or a[j] == '10' or a[j] == '11' or a[j] == '12'):
                returnedWord = True
            elif a[i] == '8' and (a[j] == '3' or a[j] == '4' or a[j] == '7' or a[j] == '11' or a[j] == '12'):
                returnedWord = True
            elif a[i] == '9' and (a[j] == '5' or a[j] == '6' or a[j] == '10' or a[j] == '13' or a[j] == '14'):
                returnedWord = True
            elif a[i] == '10' and (a[j] == '5' or a[j] == '6' or a[j] == '7' or a[j] == '9' or a[j] == '11' or a[j] == '13' or a[j] == '14' or a[j] == '15'):
                returnedWord = True
            elif a[i] == '11' and (a[j] == '6' or a[j] == '7' or a[j] == '8' or a[j] == '10' or a[j] == '11' or a[j] == '12'):
                returnedWord = True
            elif a[i] == '12' and (a[j] == '7' or a[j] == '8' or a[j] == '11' or a[j] == '15' or a[j] == '16'):
                returnedWord = True
            elif a[i] == '13' and (a[j] == '9' or a[j] == '10' or a[j] == '14'):
                returnedWord = True
            elif a[i] == '14' and (a[j] == '9' or a[j] == '10' or a[j] == '11' or a[j] == '13' or a[j] == '15'):
                returnedWord = True
            elif a[i] == '15' and (a[j] == '10' or a[j] == '11' or a[j] == '12' or a[j] == '14' or a[j] == '16'):
                returnedWord = True
            elif a[i] == '16' and (a[j] == '11' or a[j] == '12' or a[j] == '15'):
                returnedWord = True
            else:
                return False
                break

        if puzzleSize == 5:
            if a[i] == '1' and (a[j] == '2' or a[j] == '6' or a[j] == '7'):
                returnedWord = True
            elif a[i] == '2' and (a[j] == '1' or a[j] == '3' or a[j] == '6' or a[j] == '7' or a[j] == '8'):
                returnedWord = True
            elif a[i] == '3' and (a[j] == '2' or a[j] == '4' or a[j] == '7' or a[j] == '8' or a[j] == '9'):
                returnedWord = True
            elif a[i] == '4' and (a[j] == '3' or a[j] == '5' or a[j] == '8' or a[j] == '9' or a[j] == '10'):
                returnedWord = True
            elif a[i] == '5' and (a[j] == '4' or a[j] == '9' or a[j] == '10'):
                returnedWord = True
            elif a[i] == '6' and (a[j] == '1' or a[j] == '2' or a[j] == '7' or a[j] == '11' or a[j] == '12'):
                returnedWord = True
            elif a[i] == '7' and (a[j] == '1' or a[j] == '2' or a[j] == '3' or a[j] == '6' or a[j] == '8' or a[j] == '11' or a[j] == '12' or a[j] == '13'):
                returnedWord = True
            elif a[i] == '8' and (a[j] == '2' or a[j] == '3' or a[j] == '4' or a[j] == '7' or a[j] == '9' or a[j] == '12' or a[j] == '13' or a[j] == '4'):
                returnedWord = True
            elif a[i] == '9' and (a[j] == '3' or a[j] == '4' or a[j] == '5' or a[j] == '8' or a[j] == '10' or a[j] == '13' or a[j] == '14' or a[j] == '15'):
                returnedWord = True
            elif a[i] == '10' and (a[j] == '4' or a[j] == '5' or a[j] == '9' or a[j] == '14' or a[j] == '15'):
                returnedWord = True
            elif a[i] == '11' and (a[j] == '6' or a[j] == '7' or a[j] == '12' or a[j] == '16' or a[j] == '17'):
                returnedWord = True
            elif a[i] == '12' and (a[j] == '6' or a[j] == '7' or a[j] == '8' or a[j] == '11' or a[j] == '13' or a[j] == '16' or a[j] == '17' or a[j] == '18'):
                returnedWord = True
            elif a[i] == '13' and (a[j] == '7' or a[j] == '8' or a[j] == '9' or a[j] == '12' or a[j] == '14' or a[j] == '17' or a[j] == '18' or a[j] == '19'):
                returnedWord = True
            elif a[i] == '14' and (a[j] == '8' or a[j] == '9' or a[j] == '10' or a[j] == '13' or a[j] == '15' or a[j] == '18' or a[j] == '19' or a[j] == '20'):
                returnedWord = True
            elif a[i] == '15' and (a[j] == '9' or a[j] == '10' or a[j] == '14' or a[j] == '19' or a[j] == '20'):
                returnedWord = True
            elif a[i] == '16' and (a[j] == '11' or a[j] == '12' or a[j] == '17' or a[j] == '21' or a[j] == '22'):
                returnedWord = True
            elif a[i] == '17' and (a[j] == '11' or a[j] == '12' or a[j] == '13' or a[j] == '16' or a[j] == '18' or a[j] == '21' or a[j] == '22' or a[j] == '23'):
                returnedWord = True
            elif a[i] == '18' and (a[j] == '12' or a[j] == '13' or a[j] == '14' or a[j] == '17' or a[j] == '19' or a[j] == '22' or a[j] == '23' or a[j] == '24'):
                returnedWord = True
            elif a[i] == '19' and (a[j] == '13' or a[j] == '14' or a[j] == '15' or a[j] == '18' or a[j] == '20' or a[j] == '23' or a[j] == '24' or a[j] == '25'):
                returnedWord = True
            elif a[i] == '20' and (a[j] == '14' or a[j] == '15' or a[j] == '19' or a[j] == '24' or a[j] == '25'):
                returnedWord = True
            elif a[i] == '21' and (a[j] == '16' or a[j] == '17' or a[j] == '22'):
                returnedWord = True
            elif a[i] == '22' and (a[j] == '16' or a[j] == '17' or a[j] == '18' or a[j] == '21' or a[j] == '23'):
                returnedWord = True
            elif a[i] == '23' and (a[j] == '17' or a[j] == '18' or a[j] == '19' or a[j] == '22' or a[j] == '24'):
                returnedWord = True
            elif a[i] == '24' and (a[j] == '18' or a[j] == '19' or a[j] == '20' or a[j] == '23' or a[j] == '25'):
                returnedWord = True
            elif a[i] == '25' and (a[j] == '19' or a[j] == '20' or a[j] == '24'):
                returnedWord = True
            else:
                return False
                break
        return returnedWord


words = getDict()

puzzleSize = int(input())
puzzle = []
letters = []
for i in range(puzzleSize):
    puzzle.append(input().split())

for i in range(puzzleSize):
    for j in range(puzzleSize):
        letters.append(puzzle[i][j])

print("eliminating extraneous characters")

printedWords = []
for i in range(len(words)):
    if set(words[i]).issubset(letters):
        printedWords.append(words[i])

printedWords = [*set(printedWords)]

print("eliminating doubles")

noDoubles = []
for i in range(len(printedWords)):
    validLetters = letters[:]
    leftoverCount = 0
    wordLetters = []
    word = printedWords[i]
    for j in range(len(printedWords[i])):
        wordLetters.append(printedWords[i][j])
    for k in range(len(wordLetters)):
        for o in range(len(validLetters)):
            if wordLetters[k] == validLetters[o]:
                wordLetters[k] = "_"
                validLetters[o] = "-"
    for L in range(len(wordLetters)):
        if wordLetters[L] != "_":
            leftoverCount += 1
    if leftoverCount == 0:
        noDoubles.append(printedWords[i])
wordList = noDoubles[:]
wordList = [*set(wordList)]
print("eliminating repeated squares")

finalList = []
wordlist2 = []
wordlist3 = []
for i in range(len(wordList)):
    word = indexWord(wordList[i])
    for j in range(len(word)):
        if hasNoDuplicates(word[j]) is not None:
            wordlist3.append(hasNoDuplicates(word[j]))
    wordlist2.append(wordlist3)
wordList = wordlist2

print("done making word list, testing adjacency")
try:
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            if (isAdjacent(wordList[i][j])) is True:
                finalList.append(stripIndex(wordList[i][j]))
                if len(wordList) > 1:
                    del wordList[i]
                if len(finalList) % 1000 == 0:
                    print("working " + str(len(wordList) - i))
                    print(finalList[-1])
except:
    finalList = [*set(finalList)]
    finalList.sort(reverse=True)
    printWordList(finalList)
