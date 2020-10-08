class SumOfThree:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_to_zero(self):
        output = []
        if len(self.numbers) < 3:
            return output
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                for k in range(j + 1, len(self.numbers)):
                    to_sum = [self.numbers[i], self.numbers[j], self.numbers[k]]
                    if sum(to_sum) == 0 and to_sum not in output:
                        output.append(to_sum)
        return output
