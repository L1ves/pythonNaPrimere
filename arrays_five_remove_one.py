from array import *
import random
#arrays_five_remove_one.py
"""
Предложите пользователю
ввести пять чисел. Отсор­
тируйте их и выведите для
пользователя. Предложите вы-
брать одно из чисел. Удалите
выбранное число из исходного
массива и сохраните его
в новом.
"""

array_data = array("i",[])

print("Input five digits!: ")



for i in range(0,5):
	user_input = int(input("Введи число! "))
	array_data.append(user_input)
array_data = sorted(array_data)
print(array_data)

del_number = int(input("Please input a digit for delete: "))
if del_number in array_data:
	array_data.remove(del_number)
	array_data2 = array("i",[])
	array_data2.append(del_number)
	print("Остаточек --> ",array_data)
	print("This digit was delete --> ",array_data2)
else:
	print("That is not a value in the array")