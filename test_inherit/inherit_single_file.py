# Parent class
class Arithmetic:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        self.some_random_number=10

    def calculate(self):
        result = self.operand1 + self.operand2
        self.just_new_number=(self.operand1 + self.operand2)*3
        return f"{self.operand1} + {self.operand2} = {result}"

# Child class inheriting from Arithmetic
class Dog(Arithmetic):
    def __init__(self, arithmetic_instance):
        super().__init__(arithmetic_instance.operand1, arithmetic_instance.operand2)
    def another_cal(self):
        hh=1
        print(f'another_cal: {self.some_random_number}')
        print(f'This is new:{self.just_new_number}')

# Create instances of the Dog class with inherited operands
mclass=Arithmetic(3, 100)
dog1 = Dog(mclass)


# Calculate and print results
result1 = dog1.calculate()
result2 = dog1.another_cal()

print(result1)
print(result2)