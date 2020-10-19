# Comments: Exercise 1
# Dan Hayduk; Supersenior; Electrical Engineering and International Studies

from __future__ import print_function
import random

# Classes: Exercise 1
class RomanNumeral:
      def __init__(self, integer=1):
            self.integer = integer
            self.romanString = ""

            self.runConversion()

      def changeInteger(self, newInteger):
            self.integer = newInteger
            self.runConversion()

      def getRomanNumeral(self):
            return self.romanString

      def runConversion(self):
            # Convert the integer to a roman numeral
            # This function is called from __init__ and whenever the number is updated

            self.romanString = ""
            leftToAdd = self.integer

            while leftToAdd >= 1000:
                  self.romanString += "M"
                  leftToAdd -= 1000

            if leftToAdd >= 900:
                  self.romanString += "CM"
                  leftToAdd -= 900
            
            if leftToAdd >= 500:
                  self.romanString += "D"
                  leftToAdd -= 500

            if leftToAdd >= 400:
                  self.romanString += "CD"
                  leftToAdd -= 400
            
            while leftToAdd >= 100:
                  self.romanString += "C"
                  leftToAdd -= 100

            if leftToAdd >= 90:
                  self.romanString += "XC"
                  leftToAdd -= 90

            if leftToAdd >= 50:
                  self.romanString += "L"
                  leftToAdd -= 50

            if leftToAdd >= 40:
                  self.romanString += "XL"
                  leftToAdd -= 40

            while leftToAdd >= 10:
                  self.romanString += "X"
                  leftToAdd -= 10

            if leftToAdd >= 9:
                  self.romanString += "IX"
                  leftToAdd -= 9

            if leftToAdd >= 5:
                  self.romanString += "V"
                  leftToAdd -= 5
            
            if leftToAdd >= 4:
                  self.romanString += "IV"
                  leftToAdd -= 4

            while leftToAdd >= 1:
                  self.romanString += "I"
                  leftToAdd -= 1

# Classes: Exercise 2
class SetWithThreeZeroSummingNums:
      def __init__(self, startingSet=set()):
            self.setOfNums = startingSet
            self.setOfZeroSummingNums = set()

            self.runConversion()

      def changeSet(self, newSet):
            self.setOfNums = newSet
            self.runConversion()

      def getZeroSummingNums(self):
            return self.setOfZeroSummingNums
      
      def runConversion(self):
            # Look in the set for the first three numbers whose sum is zero
            # Create a set of these three numbers and store them in self.setOfZeroSummingNums
            #
            # If there aren't three numbers whose sum is zero, set self.setOfZeroSummingNums
            # to an empty set

            if len(self.setOfNums) < 3:
                  # If the length of the set is less than 3, there cannot be three numbers
                  # that add to zero
                  self.setOfZeroSummingNums = set()
                  return

            for eachNumI in self.setOfNums:
                  for eachNumJ in self.setOfNums:
                        if eachNumI != eachNumJ:
                              for eachNumK in self.setOfNums:
                                    if eachNumK != eachNumI and eachNumK != eachNumJ and eachNumI + eachNumJ + eachNumK == 0:
                                          self.setOfZeroSummingNums = {eachNumI, eachNumJ, eachNumK}
                                          return

            self.setOfZeroSummingNums = set()

# Classes: Exercise 3
class StringReversedByWord:
      def __init__(self, startingString=""):
            self.forwardString = startingString
            self.backwardString = ""

            self.runConversion()
      
      def changeString(self, newString):
            self.forwardString = newString
            self.runConversion()

      def getReversedString(self):
            return self.backwardString

      def runConversion(self):
            # Parse through the string looking for spaces, then prepend each word
            # to the beginning of the reversed string
            self.backwardString = ""
            wordToAdd = ""

            for eachChar in self.forwardString:
                  if eachChar == " " and self.backwardString == "":
                        self.backwardString = wordToAdd
                        wordToAdd = ""
                  elif eachChar == " ":
                        self.backwardString = wordToAdd + " " + self.backwardString
                        wordToAdd = ""
                  else:
                        wordToAdd += eachChar

            # Add the last word at the end if the last character wasn't a space
            if wordToAdd != "":
                 self.backwardString = wordToAdd + " " + self.backwardString

# Classes: Exercise 4
class ListWithTwoCustomSummingNums:
      def __init__(self, startingList=[], target=0):
            self.listOfNums = startingList
            self.listOfTargetSummingIndices = []
            self.target = target

            self.runConversion()

      def changeList(self, newList):
            self.listOfNums = newList
            self.runConversion()

      def changeTarget(self, newTarget):
            self.target = newTarget
            self.runConversion()

      def getTargetSummingIndices(self):
            return self.listOfTargetSummingIndices
      
      def runConversion(self):
            # Look in the list for the first two numbers whose sum is the target
            # Create a list of the indicies of these two numbers and store them 
            # in self.listOfTargetSummingIndices
            #
            # If there aren't two numbers whose sum is the target, 
            # set self.listOfTargetSummingIndices to an empty list

            if len(self.listOfNums) < 2:
                  # If the length of the list is less than 2, there cannot be two numbers
                  # that add to the target
                  self.listOfTargetSummingIndices = []
                  return

            for i in range(len(self.listOfNums)):
                  for j in range(i+1, len(self.listOfNums)):
                        if self.listOfNums[i] + self.listOfNums[j] == self.target:
                              self.listOfTargetSummingIndices = [i, j]
                              return

            self.listOfTargetSummingIndices = []


# Functions: Exercise 1
def sumList(list):
      sum = 0
      for i in list:
            sum += i

      return sum

def multiplyList(list):
      product = 1
      for i in list:
            product *= i
      
      return product

def subtractList(list):
      # Assumed specification: return 0 - (all numbers in list)
      # as opposed to (item at index 0) - (all other numbers in list)
      
      difference = 0
      for i in list:
            difference -= i
      
      return difference

# Functions: Exercise 2
def reverseString(theString):
      reversedString = ""
      i = len(theString) - 1
      while i >= 0:
            reversedString += theString[i]
            i -= 1
      
      return reversedString

# Functions: Exercise 3
def capitalizeFirstLetter(theString):
      capitalizedString = ""
      prevCharWasSpaceOrBeginning = True
      for eachLetter in theString:
            if prevCharWasSpaceOrBeginning:
                  capitalizedString += eachLetter.upper()
                  prevCharWasSpaceOrBeginning = False
            elif eachLetter == " ":
                  prevCharWasSpaceOrBeginning = True
                  capitalizedString += eachLetter
            else:
                  capitalizedString += eachLetter    

      return capitalizedString

# Functions: Exercise 4
def numLetters(theString):
      i = 0
      for eachChar in theString:
            if 'A' <= eachChar <= 'Z' or 'a' <= eachChar <= 'z':
                  i += 1
      return i


# Printing: Exercise 1
print("Hello SeaWolf VIII")

# Printing: Exercise 2
howItsDoing = str(raw_input("How are you doing?\n"))
print("You are doing " + howItsDoing + "? Great!")

# Printing: Exercise 3
print("I am doing great.")
print("I am a new member of the software team and will be working with you in the future.")
print("We are going to place well in RoboSub.")

# Printing: Exercise 4
print("I am doing great.\nI am a new member of the software team and will be working with you in the future.\n"
      +"We are going to place well in RoboSub.")


# Variables: Exercise 1
clubName1 = "NCSU"
clubName2 = "Underwater"
clubName3 = "Robotics"
clubName4 = "Club"

fullClubName = clubName1 + " " + clubName2 + " " + clubName3 + " " + clubName4
print(fullClubName)

# Variables: Exercise 2
four = 4
three = 3
sum = four + three
print("The sum of " + str(four) + " and " + str(three) + " is " + str(sum) + ".")

# Variables: Exercise 3
product = four * three
print("The product of " + str(four) + " and " + str(three) + " is " + str(product) + ".")

# Variables: Exercise 4
difference = four - three
print("The difference between " + str(four) + " and " + str(three) + " is " + str(difference) + ".")

# Variables: Exercise 5
dividend = four / three
print("The result of dividing " + str(four) + " and " + str(three) + " is " + str(dividend) + ".")


# Lists: Exercise 1
ncStateColors = ["red", "white", "black"]

# Lists: Exercise 2
print(*ncStateColors, sep="\n")

# Lists: Exercise 3
ncStateColors.insert(ncStateColors.index("red"), "Sea")
ncStateColors.remove("red")
ncStateColors.insert(ncStateColors.index("white"), "Wolf")
ncStateColors.remove("white")
ncStateColors.insert(ncStateColors.index("black"), "VIII")
ncStateColors.remove("black")

print(*ncStateColors)

# Lists: Exercise 4
ncStateColors.insert(0, "Robotics")
ncStateColors.insert(0, "Underwater")
ncStateColors.insert(0, "State")
ncStateColors.insert(0, "NC")

print(*ncStateColors)

# Lists: Exercise 5
ncStateColors.remove("VIII")
print(*ncStateColors)


# Functions: Exercise 1
print(sumList([4,6,7,8,10]))
print(multiplyList([4,6,7,8,10]))
print(subtractList([4,6,7,8,10]))

# Functions: Exercise 2
print(reverseString("NCSURobotics"))

# Functions: Exercise 3
stringToCapitalize = str(raw_input("Type an improperly capitalized string and we'll fix it for you!\n"))
print(capitalizeFirstLetter(stringToCapitalize))

# Functions: Exercise 4
stringToCountLetters = str(raw_input("Now type in a string and we'll calculate how many letters are in it!\n"))
print(numLetters(stringToCountLetters))


# Conditional Statements and Loops: Exercise 1
i = 1
while i <= 10:
      print(i)
      i += 1

# Conditional Statements and Loops: Exercise 2
for i in range(1, 6):
      j = i
      stringToPrint = str(j)
      while j > 1:
            j -= 1
            stringToPrint = str(j) + " " + stringToPrint
      print(stringToPrint)

# Conditional Statements and Loops: Exercise 3
seaWolfList = ["SW I", "SW II", "SW III", "SW IV", "SW V", "SW VI", "SW VII", "SW VIII"]
newList = []
for eachItem in seaWolfList:
      newList.insert(0, eachItem)
seaWolfList = newList
print(*seaWolfList)

# Conditional Statements and Loops: Exercise 4
for i in range(0, 11):
      if i != 4 and i != 8 and i != 10:
            print(i)

# Conditional Statements and Loops: Exercise 5
stringToMeasure15 = str(raw_input("Enter a string to determine whether its length is 15.\n"))
stringLength = 0
for eachChar in stringToMeasure15:
      stringLength += 1
if (stringLength == 15):
      print(True)
else:
      print(False)


# Classes: Exercise 1

# This code demonstrates the RomanNumeral class's ability to represent 
# numbers 1 to 1000, in the form of the numerals that will be used for 
# the 1000 Star Wars Episodes that will eventually come out.
starWarsEpisode = RomanNumeral(1)
for i in range(1, 1001):
      starWarsEpisode.changeInteger(i)
      print(starWarsEpisode.getRomanNumeral())

# Classes: Exercise 2

# This code demonstrates that the SetWithThreeZeroSummingNums class 
# can hold a set of numbers and keep track of the first three numbers 
# that add up to zero. Ten sets of ten random numbers are generated,
# and their resulting sets of three zero-summing numbers are printed
# alongside them. Since a set cannot have repeating elements, some sets
# have fewer than ten elements, but they are still acceptable for this
# demonstration.
setOfSomeNums = SetWithThreeZeroSummingNums()

for _ in range(10):
      setToUpdateTo = set()

      for _ in range(10):
            setToUpdateTo.add(random.randrange(-10, 10))
      
      setOfSomeNums.changeSet(setToUpdateTo)
      print(str(setToUpdateTo) + ": " + str(setOfSomeNums.getZeroSummingNums()))

# Classes: Exercise 3

# This code demonstrates the working StringReversedByWord class
# with the (probably, maybe) proper titles of the games in the Kingdom 
# Hearts franchise. The object contains the original string and the string 
# properly reversed after it has been created/updated.
stringToReverse = StringReversedByWord("Kingdom Hearts")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts: Chain of Memories")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts: 358/2 Days")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts II")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts: Birth By Sleep")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts Re: Coded")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts: Dream Drop Distance")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts: 0.2 Birth By Sleep - A Fragmentary Passage")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts: Back Cover")
print(stringToReverse.getReversedString())
stringToReverse.changeString("Kingdom Hearts III")
print(stringToReverse.getReversedString())

# Classes: Exercise 4

# This code demonstrates that the ListWithTwoCustomSummingNums class 
# can hold a set of numbers and keep track of the first two numbers 
# that add up to the specified target. Ten lists of ten random numbers 
# are generated, along with a random target. The resulting sets of two 
# target-summing numbers' indices are printed alongside the lists, along
# with what the target was.
listOfSomeNums = ListWithTwoCustomSummingNums()

for _ in range(10):
      listToUpdateTo = []

      for _ in range(10):
            listToUpdateTo.append(random.randrange(-10, 10))

      targetToUse = random.randrange(-10, 10)
      
      listOfSomeNums.changeList(listToUpdateTo)
      listOfSomeNums.changeTarget(targetToUse)
      print(str(listToUpdateTo) + ": " + str(listOfSomeNums.getTargetSummingIndices()) + "; Target = " + str(targetToUse))
