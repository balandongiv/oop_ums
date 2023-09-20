# from __future__ import annotations
#
# from typing import ForwardRef
#
# Dog: ForwardRef = 'Dog'
# Arithmetic: ForwardRef = 'Arithmetic'

from pclass import Arithmetic

class Dog(Arithmetic):
    def __init__(self, arithmetic_instance):
        super().__init__(arithmetic_instance.operand1, arithmetic_instance.operand2)

    def another_cal(self):
        hh = 1
        print(f'another_cal: {self.some_random_number}')
        return hh