from array import *
import random
#array_two_repeat.py
"""
Создайте массив, содержащий
пять чисел (два из которых
должны повторяться). Выве-
дите весь массив. Предложите
пользователю ввести одно из
чисел массива, после чего вы-
ведите сообщение, в котором
указано, сколько раз число
встречается в этом массиве.


two_repeat = array("i",[3,3,15,16,1])
for i in two_repeat:
	print(i)

user_input = int(input("Input a digit from array: "))
for user_input in two_repeat:
	if two_repeat.count(user_input) == 1:
		print("Число ", user_input, "Встречается один раз ")
	else:
		print("Число ",user_input," встречается ",two_repeat.count(user_input)," раз")
"""

two_repeat = array("i",[3,3,15,16,1])
for i in two_repeat:
	print(i)
user_input = int(input("Input a digit from array: "))

if two_repeat.count(user_input) == 1:
	print("Число ", user_input, "Встречается один раз ")
else:
	print("Число ",user_input," встречается ",two_repeat.count(user_input)," раз")