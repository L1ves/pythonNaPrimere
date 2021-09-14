from array import *

"""Измените программу из задачи 098.
Предложите пользователю выбрать стро-
ку и выведите только ее. Предложите вы-
брать столбец из выведенной строки и вы-
ведите только хранящееся там значение.
Спросите, хочет ли пользователь изменить
его. Если ответ будет положительным,
предложите ввести новое значение и из-
мените данные. Наконец, снова выведите
измененную строку.
"""

double_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(double_array)
raw = int(input("CHoice the raw: "))
print(double_array[raw])
column = int(input("Choice the value in column: "))
print(double_array[raw][column])
ask = input("Do you want edit the value?:  y/n ")
if ask == "y":
	choice = int(input("Input new data: "))
	double_array[raw][column] = choice
print(double_array[raw])


