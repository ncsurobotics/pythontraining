class ReverseWords:

    def __init__(self, sentence):
        self.sentence = sentence

    def reverse(self):
        return " ".join(reversed(self.sentence.split(" ")))

