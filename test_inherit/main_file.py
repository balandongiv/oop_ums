# main.py
import pclass
import dogclass
from pclass import Arithmetic
from dogclass import Dog

# Create an instance of the Arithmetic class
mclass = Arithmetic(1, 1)

# Create an instance of the Dog class with the Arithmetic instance
dog1 = Dog(mclass)

# Calculate and print results
result1 = dog1.calculate()
result2 = dog1.another_cal()

print(result1)
print(result2)