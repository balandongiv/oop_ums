# from childclass import Dog
# from __future__ import annotations
#
# from typing import ForwardRef
#
# Dog: ForwardRef = 'Dog'
# Arithmetic: ForwardRef = 'Arithmetic'
# Parent class
class Arithmetic:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
        self.some_random_number = 10

    def calculate(self):
        result = self.operand1 + self.operand2
        return f"{self.operand1} + {self.operand2} = {result}"

