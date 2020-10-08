from RomanNumerals import RomanNumerals
from SumOfThree import SumOfThree
from ReverseWords import ReverseWords
from FindPairs import FindPairs

# Name: Roman Peace ~*~ Year: Freshman ~*~ Major: Computer Science

# Printing
print("Hello Seawolf VIII")

input("How is Seawolf doing? ")

print("I am doing great.")
print("I am a new member of the software team and will be working with you in the future.")
print("We are going to place well in RoboSub.")

print("""I am doing great.
I am a new member of the software team and will be working with you in the future.
We are going to place well in RoboSub.
""")

# Variables
a = "NCSU"
b = "Underwater"
c = "Robotics"
d = "Club"
print(a, b, c, d, sep=" ")

four = 4
three = 3
sum = three + four
print(sum)

product = three * four
print(product)

difference = four - three
print(difference)

dividend = three / four
print(dividend)

# Lists
colors = ["Red", "Black", "White"]

print(colors, sep=" ")

colors[0] = "Sea"
colors[1] = "Wolf"
colors[2] = "VIII"
print(colors)

colors = ["NC", "State", "Underwater", "Robotics"] + colors
print(colors)

colors.remove("VIII")
print(colors)


# Functions

# I wasn't entirely sure what to do on this one,
# so I just summed, multiplied, and subtracted starting with the first
# number and iterating through the list


def operations(numlist):
    list_sum = 0
    for num in numlist:
        list_sum += num
    list_product = 1
    for num in numlist:
        list_product *= num
    list_subtraction = numlist[0]
    for i in range(1, len(numlist)):
        list_subtraction -= numlist[i]
    return list_sum, list_product, list_subtraction


print(operations([4, 6, 7, 8, 10]))


def reverse_string(strng):
    return strng[len(strng) - 1::-1]


print(reverse_string("NCSURobotics"))


def capitalize(strng):
    words = strng.split(" ")
    for i, word in enumerate(words):
        words[i] = word[0].upper() + word[1:]
    return " ".join(words)


print(capitalize("this is a string to test the function"))


def letter_count(strng):
    count = 0
    for char in strng:
        if char.isalpha():
            count += 1
    return count


print(letter_count("h0w mAny l3tt3rs ar3 1n th1s s3ntenc3????"))

# Conditional Statements and Loops
num = 1
while num <= 10:
    print(num)
    num += 1
print()

output = []
for i in range(1, 6):
    output.append(str(i))
    print(" ".join(output))
print()

seaWolfList = ["SW I", "SW II", "SW III", "SW IV", "SW V", "SW VI", "SW VII", "SW VIII"]
seaWolf_reversed = []
for i in range(len(seaWolfList) - 1, -1, -1):
    seaWolf_reversed.append(seaWolfList[i])
seaWolfList = seaWolf_reversed
print(seaWolfList)

for n in range(0, 10):
    if n != 4 and n != 8:
        print(n)


def len15(strng):
    return len(strng) == 15


print(len15("qwertyuiopasdfg"))

# Classes
# Tests Below
number1 = RomanNumerals(69)
print(number1.convert())

list1 = SumOfThree([-1, -3, 4, 7, -2, 3, 1])
print(list1.sum_to_zero())

sentence1 = ReverseWords("Hi I am Roman")
print(sentence1.reverse())

list2 = FindPairs([1, 4, 3, 6, 9, 2, 5])
print(list2.find_pairs(11))
print(list2.find_values())
