#list_three_digits.py
"""
Создайте список из четырех трех-
значных чисел. Выведите содер-
жимое списка, при этом каждый
элемент должен выводиться на
отдельной строке. Предложите
пользователю ввести число из трех
цифр. Если введенное число со-
впадает с одним из чисел в списке,
выведите позицию этого числа;
в противном случае выведите со-
общение «That is not in the list».
"""

four_digits = [123,456,789,963]

for i in four_digits:
	print(i)
from_user = int(input("Please input three digit: "))
if from_user in four_digits:
	print(from_user," is in position ", four_digits.index(from_user))
else:
	print("That is not in the list")