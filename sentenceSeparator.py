# @author: Sophia Canja
# CS 320
# February 9, 2021
# Program 1 : Regular Expressions
    # This program finds the FANBOYS in a compound sentence,
    # and prints out the individual sentences.

import re

try:
    fileName = input("Enter file name: ")                   # Checks if file does not exist
    fh = open(fileName, 'r')
    inputStr = fh.read()
    fh.close()

except:                                                     # Throws error
    print("Cannot find the file named: " + fileName)

else:
    print("Contents of File:\n" + inputStr)

    pattern = re.compile(r",\s(for|and|nor|but|or|yet|so)") # finds fanboys within the file
    matches = pattern.finditer(inputStr)                    # stores results
            
    newStartIndex = 0
    lastNum = -1
    
    for num,match in enumerate(matches,1):                  # goes through list
        if num == 1:                                        # prints first sentence in number order
            print(num, ":  " + inputStr[:match.start()]+ ".")
            newStartIndex = match.end()

        else:
            print(num, ":", inputStr[newStartIndex: match.start()] + ".")
            newStartIndex = match.end()                     # updates index to move down the sentence
            lastNum = num+1

            
    print(str(lastNum) + " : " + inputStr[newStartIndex:])  # prints last sentence
    

    



