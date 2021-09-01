from array import *
import random
#two_arrays
"""
Создайте два массива:
один будет содержать три
числа, введенных пользо-
вателем, а другой — пять
случайных чисел. Объ-
едините эти два массива
в один большой. Отсорти-
руйте и выведите его, при
этом каждое число должно
выводиться в отдельной
строке.
"""
count = 0
num1 = array("i",[])
num2 = array("i",[])

print("Введите 3 числа! ")
for i in range(0,3):
	user_input = int(input("Введите число! "))
	num1.append(user_input)
print("Пользователь ввел: ",num1)
#while count < 5:
#	random_int = random.randint(0,100)
for i in range(0,5):
	random_int = random.randint(0,100)
	num2.append(random_int)
	#count = count +1
num_big = num2 + num1
print("Объединенный массив:  ",num_big)

num_big = sorted(num_big)

for i in num_big:
	print("В массиве есть число !",i)