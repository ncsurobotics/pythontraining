
# Xingjian Li, 2024, CSC Intent (prob switch to EE or CPE)

# Print.1
print("Hello SeaWolf VIII.")
# Print.2
seawolf_status = input("How SeaWolf is doing?")
# Print.3
print("I am doing great.")
print("I am a new member of the software team and will be working with you in the future.")
print("We are going to place well in RoboSub.")
# Print.4
print("I am doing great.\nI am a new member of the software team and will be working with you in the future.\nWe are going to place well in RoboSub")

# Variables.1
ncsu_var = "NCSU"
underwater_var = "Underwater"
robotics_var = "Robotics"
club_var = "Club"
print(ncsu_var + " " + underwater_var + " " + robotics_var + " " + club_var)
# Variables.2
four = 4
three = 3
sum_var = four + three
print("sum of three and four is: " + str(sum_var))
# Variables.3
product_var = four * three
print("product of three and four is: " + str(product_var))
# Variables.4
difference_var = abs(four - three)
print("difference between three and four is: " + str(difference_var))
# Variables.5
dividend_var = four/three
print("dividend of three and four is: " + str(dividend_var))

# Lists.1
ncstate_colors = ["red", "white", "black"]
# Lists.2
# set interpreter to 3.x if sep isn't working
print(ncstate_colors[0], ncstate_colors[1], ncstate_colors[2], sep=' ')
# Lists.3
ncstate_colors[0] = "Sea"
ncstate_colors[1] = "Wolf"
ncstate_colors[2] = "VIII"
# List.4
ncstate_colors.insert(0,"NC")
ncstate_colors.insert(1,"State")
ncstate_colors.insert(2,"Underwater")
ncstate_colors.insert(3,"Robotics")
print(ncstate_colors)
# List.5
ncstate_colors.remove("VIII")
print(ncstate_colors)

# Functions.1
def calculate_the_number(l):
      #the number = sum of all numbers * all numbers - all numbers
      the_number = sum(l)
      for i in l:
            the_number *= i
      the_number -= sum(l)
      return the_number

list_func = [4,6,7,8,10]
print(calculate_the_number(list_func))
# Function.2
def reverse_string(s):
      reversed_str = s[::-1]
      return reversed_str

string_func = "NCSURobotics"
print(reverse_string(string_func))
# Function.3
def capitalize_first_letter(s):
      word_list = s.split(' ')
      for i, word in enumerate(word_list):
            word_list[i] = word.capitalize()
      return ' '.join(word_list)

sentence_func = "capitalize every word in this sentence."
print(capitalize_first_letter(sentence_func))
# Function.4
def count_letters(s):
      count = 0
      for letter in s:
            if letter.isalpha():
                  count+=1
      return count
sentence_func = "The number of letters in this sentence should be 40."
print(count_letters(sentence_func)) 
                  
# Loop.1
natural_num = 1
while(natural_num < 11):
      print(natural_num)
      natural_num += 1
# Loop.2
pattern = ""
for i in range(1,6):
      pattern = pattern + str(i)
      print(pattern)
      pattern += ' '
# Loop.3
seaWolfList = ["SW I", "SW II", "SW III", "SW IV", "SW V", "SW VI", "SW VII", "SW III"]
half_point = int(len(seaWolfList)/2)
for i in range(half_point):
      ## Swap
      seaWolfList[i], seaWolfList[len(seaWolfList)-(i+1)] = seaWolfList[len(seaWolfList)-(i+1)], seaWolfList[i]
print(seaWolfList) 
# Loop.4
for i in range(11):
      if i != 4 and i != 8 and i != 10:
            print(i)
# Loop.5
def check_length(s):
      if len(s) == 15:
            return True
      return False
length_15 = "123451234512345"
print(check_length(sentence_func))
print(check_length(length_15))

# Class.1
class IntToNumeral:
      numeral_list = [0,0,0,0,0,0,0] ## ones, fives, tens ...
      numeral_letters = ['I','V','X','L','C','D','M']
      ## receive input
      def __init__(self, i):
            self.integer = i
      
      ## sets the number of each roman numeral letters
      def set_numerals(self):
            current = self.integer
            self.numeral_list[6] = current//1000
            current = current % 1000
            self.numeral_list[5] = current//500
            current = current % 500
            self.numeral_list[4] = current//100
            current = current % 100
            self.numeral_list[3] = current//50
            current = current % 50
            self.numeral_list[2] = current//10
            current = current % 10
            self.numeral_list[1] = current//5
            current = current % 5
            self.numeral_list[0] = current

      ## does the conversion from list of letters into one string
      def int_to_numeral(self):
            self.set_numerals()
            numeral = ""
            skip = False
            for i in range(len(self.numeral_list))[::-1]:
                  n = self.numeral_list[i]
                  ## Rules of roman numerals
                  if n % 2 == 0 and self.numeral_list[i-1] == 4 and i % 2 == 1:
                        numeral += self.numeral_letters[i-1] + self.numeral_letters[i]
                        skip = True
                  elif n % 2 == 1 and self.numeral_list[i-1] == 4 and i % 2 == 1:
                        numeral += self.numeral_letters[i-1] + self.numeral_letters[i+1]
                        skip = True
                  elif skip == True:
                        skip = False
                  else:
                        numeral += self.numeral_letters[i] * int(n)
            return numeral                  
                  
numeral = IntToNumeral(1389)
print(numeral.int_to_numeral())

# Class.2
class ZeroSumInThree:
      def __init__(self,set):
            self.set = set
      def findTriplet(self):
            for i in self.set[:-2]:
                  for j in self.set[i+1:-1]:
                        for k in self.set[j+1:]:
                              if (i+j+k) == 0:
                                    return [i,j,k]
            return "No triplets sums to zero."
set = [1,2,3,4,5,-5,-4,-3,-2,-1]
triplets = ZeroSumInThree(set)
print(triplets.findTriplet())

# Class.3
class ReverseSentence:
      def __init__(self,s):
            self.sentence = s
      def reverse_words(self):
            word_list = self.sentence.split(' ')
            half_point = int(len(word_list)/2)
            for i in range(half_point):
                  ## Swap
                  word_list[i], word_list[-(i+1)] = word_list[-(i+1)], word_list[i]
            return ' '.join(word_list)
sentence_before = "Write a class to reverse a string word by word"
reversal = ReverseSentence(sentence_before)
print(reversal.reverse_words())

# Class.4
class FindPair:
      def __init__(self,arr,target_num):
            self.arr = arr
            self.target = target_num
      def search_indices(self):
            for i in range(len(self.arr)-1):
                  for j in range(i+1,len(self.arr)):
                        if self.arr[i] + self.arr[j] == self.target:
                              return "Two indices sums to target at " + str(i) + " and "+ str(j)
            return "No pair matches the target."
set = [1,2,3,4,5,6,7,8,9,0]
target_num = 1
pair = FindPair(set,target_num)
print(pair.search_indices())
