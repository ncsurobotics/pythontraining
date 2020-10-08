class RomanNumerals:
    def __init__(self, number):
        self.number = number

    def convert(self):
        converted = ""
        if self.number//1000 > 0:
            converted += "M"*(self.number//1000)
            self.number %= 1000

        if self.number//500 > 0:
            converted += "D"*(self.number//500)
            self.number %= 500

        if self.number//100 > 0:
            converted += "C"*(self.number//100)
            self.number %= 100

        if self.number//50 > 0:
            converted += "L"*(self.number//50)
            self.number %= 50

        if self.number//10 > 0:
            converted += "X" * (self.number // 10)
            self.number %= 10

        if self.number//5 > 0:
            converted += "V"*(self.number//5)
            self.number %= 5
        converted += "I"*self.number

        converted = converted.replace("DCCCC", "CM")
        converted = converted.replace("CCCC", "CD")
        converted = converted.replace("LXXXX", "XC")
        converted = converted.replace("XXXX", "XL")
        converted = converted.replace("VIIII", "IX")
        converted = converted.replace("IIII", "IV")
        return converted

