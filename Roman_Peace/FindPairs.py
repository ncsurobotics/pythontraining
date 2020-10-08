class FindPairs:
    def __init__(self, numbers):
        self.numbers = numbers
        self.pairs = []
        self.values = []

    def find_pairs(self, target):
        output = []
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                to_sum = [self.numbers[i], self.numbers[j]]
                if sum(to_sum) == target and to_sum not in output:
                    output.append([i, j])
        self.pairs = output
        return output

    def find_values(self):
        output = []
        for pair in self.pairs:
            output.append([self.numbers[pair[0]], self.numbers[pair[1]]])
        return output
