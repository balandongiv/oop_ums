# Parent class
class Arithmetic:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        self.some_random_number = 10

    def calculate(self):
        result = self.operand1 + self.operand2
        return f"{self.operand1} + {self.operand2} = {result}"

# Child class inheriting from Arithmetic
class Dog(Arithmetic):
    def __init__(self, arithmetic_instance):
        super().__init__(arithmetic_instance.operand1, arithmetic_instance.operand2)

    def another_cal(self):
        hh = 1
        print(f'another_cal: {self.some_random_number}')
        return hh

# Create an instance of the Arithmetic class
mclass = Arithmetic(1, 1)

# Create an instance of the Dog class with the Arithmetic instance
dog1 = Dog(mclass)

# Calculate and print results
result1 = dog1.calculate()
result2 = dog1.another_cal()

print(result1)
print(result2)
