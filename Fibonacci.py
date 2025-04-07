class Fibonacci:

    """
    A class to generate Fibonacci numbers up to a specified limit.

    This class implements an iterator that generates Fibonacci numbers
    until a specified limit is reached.

    """

    def __init__(self, limit):
        self.limit = limit
    
    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        return self
    def __next__(self):
        if self.num1 <= self.limit: 
            next_value = self.num1
            self.num1 = self.num2
            self.num2 = self.num1 + next_value 
            return next_value
        if self.num1 > self.limit: 
            raise StopIteration


# a = Fibonacci(1975)        
# print(list(a))

b = Fibonacci(9)
print(list(b))