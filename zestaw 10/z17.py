class statictics():
    
    def __init__(self, num_set):
        self.num_set = num_set

    def add_number(self, number):
        self.num_set.append(number)

    def display_numbers(self):
        for self.number in self.num_set:
            print(self.number, end=" ")
        print("\n")
    
    def maximum(self):
        return max(self.num_set)

    def minimum(self):
        return min(self.num_set)

    def arythmetic_mean(self):
        self.sum = 0
        for self.number in self.num_set:
            self.sum += self.number

        return self.sum / len(self.num_set)

    def median(self):
        self.num_set = sorted(self.num_set)
        #odd ammount of numbers
        if len(self.num_set) % 2 != 0:
            return self.num_set[len(self.num_set)//2]
        else:
            # even ammount of number
            return (self.num_set[len(self.num_set)//2] + self.num_set[(len(self.num_set)//2)-1]) / 2 

    def display_statistics(self):
        print(f"Maximum: {self.maximum()}")
        print(f"Minimum: {self.minimum()}")
        print(f"Arythmetic mean: {self.arythmetic_mean()}")
        print(f"Median: {self.median()}")


data_set = statictics([5, 4, 3, 2])

data_set.display_numbers()
data_set.display_statistics()
