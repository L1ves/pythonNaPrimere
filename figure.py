#!/usr/env/python3
#def get_value(input(int())
"""
quiz = input()
figure = {"3":"Triangle","4":"Square","5":"Trapecia","6":"6 korn","7":"7 korn","8":"8 korn","9":"9 korn", "10":"10 korns"}
result_figure = ""
for i in quiz:
	if i in figure.keys():
		result_figure += figure[i]
		print(result_figure)
	else:
		print("ERROR")

"""
nsides = int(input("Введите количество сторон фигуры: "))

name = ""
if nsides == 3:
	name = "треугольник"
elif nsides == 4:
	name = "прямоугольник"
elif nsides == 5:
	name = "пятиугольник"
elif nsides == 6:
	name = "шестиугольник"
elif nsides == 7:
	name = "семиугольник"
elif nsides == 8:
	name = "восьмиугольник"
elif nsides == 9:
	name = "девятиугольник"
elif nsides == 10:
	name = "десятиугольник"
# Выводим ошибку ввода
if name == "":
	print("Введенное количество сторон не поддерживается программой.")
else:
	print("Эта фигура:", name)