import re

def Add(numberString):
    if not numberString:
        return 0
    if numberString.startswith('//'):
        splitString = numberString.split('\n')
        delimiter = createDelimiter(splitString[0][2:])
        numberList = re.split(delimiter, splitString[1])
    else:
        numberList = numberString.split(',')

    numberList = list(map(int, numberList))
    if any(x < 0 for x in numberList):
        raise Exception('Negatives not allowed')

    numberList = removeNumbersOverLimit(numberList)

    return sum(numberList)

def removeNumbersOverLimit(numberList):
    for number in numberList:
        if number > 1000:
            numberList.remove(number)
    return numberList

def createDelimiter(delimiter):
    # re.split works well for splitting with multiple given characters, but has issues with special characters.
    # Added this code to manage them
    specialChars = ['.', '^', '$', '*', '+', '?', '{', '}', '[', ']', '|', '(', ')']
    for char in specialChars:
        if char in delimiter:
            delimiter = delimiter.replace(char, '\\' + char)

    # ensures the comma is used to separate delimiters, and is not the delimiter itself.
    if len(delimiter) > 1:
        delimiter = delimiter.replace(',', '|')
    return delimiter
