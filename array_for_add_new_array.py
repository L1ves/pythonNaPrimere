import random
from array import *
"""
Создайте массив для хранения целых чисел. Сгенери-
руйте пять случайных чисел и сохраните их в массиве.
Выведите массив (каждый элемент должен выводить-
ся в отдельной строке).
"""

stored_data = array("i",[])
for i in range(0,5):
	new_stored_data = random.randint(1,100)
	stored_data.append(new_stored_data)
print(stored_data)
for i in stored_data:
	print(i)