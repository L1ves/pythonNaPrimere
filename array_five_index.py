from array import *
#array_five_index.py

"""
Выведите массив из пяти чи-
сел. Предложите пользователю
выбрать одно из них. После
того как число будет выбрано,
выведите его позицию в мас-
сиве. Если пользователь вве-
дет значение, отсутствующее
в массиве, предложите ему
выбрать снова, пока не будет
выбрано допустимое значение.
"""
true_digit = True
array_data = array("i",[1,2,3,4,5])
#for i in nums:
#print(i)
print(array_data)
user_input = int(input("Input a digit from array: "))


while true_digit == True:
	if user_input in array_data:
		print(array_data.index(user_input))
		true_digit = False
		user_input = int(input("Wrong choice. Input a digit from array: "))
	else: