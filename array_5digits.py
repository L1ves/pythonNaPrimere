#array_5digits.py
"""
Предложите пользователю ввести пять
целых чисел и сохраните их в массиве.
Отсортируйте список и выведите его со-
держимое в обратном порядке.
"""

from array import *

digits = array("i",[])

for i in range(0,5):
	digits_from_user = int(input("Input 5 digits! "))
	digits.append(digits_from_user)

digits = sorted(digits)
digits.reverse()

print(digits)
