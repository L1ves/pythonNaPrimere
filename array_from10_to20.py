from array import *
#array_from10_to20.py
"""
Предложите пользователю вводить целые числа. Если поль-
зователь вводит число от 10 до 20, сохраните его в массиве;
в противном случае выведите сообщение «Outside the range».
После того как пять чисел будут успешно добавлены в массив,
выведите сообщение «Thank you» и выведите массив, каждый
элемент которого находился бы на отдельной строке.
"""
five_digits = array("i",[])
count = 0

while count < 5:
	ask_digits = int(input("Input 5 digits from 10 to 20: "))
	if 10 < ask_digits and ask_digits < 20:
		five_digits.append(ask_digits)
		count = count + 1
	else:
		print("Outside the range")
print("Thank you!")
for i in five_digits:
	print("Digits which you inputed is: ",i)