import random
from array import *
import math

"""
Создайте массив из пяти чисел от 10 до 100,
каждое из которых содержит два знака в дроб-
ной части. Предложите пользователю ввести
целое число от 2 до 5. Если пользователь введет
значение, выходящее за границы диапазона, вы-
ведите сообщение об ошибке и предложите вы-
брать снова, пока не будет введено допустимое
значение. Разделите каждое из чисел в массиве
на число, введенное пользователем, и выведите
ответы с точностью до двух знаков.
"""
num1 = array("f",[34.75, 27.23, 99.58, 45.26, 28.65])
try_again = True
while try_again == True:
	user_input = int(input("Enter a number between 2 and 5: "))
	if user_input < 2 or user_input > 5:
		print("Try again! :")
	else:
		try_again = False

for i in range(0,5):
	result = num1[i] / user_input
	print(round(result, 2))
