count = 0
#Создайте переменную с именем compnum и присвойте ей значение 50.
compnum = 50
#Предложите пользователю ввести число
#number = int(input("Введи число хакер!: "))
#Пока предположение не совпадает со значением compnum, сообщите, больше оно или меньше 
#compnum, и предложите ввести другое число. 
while number != compnum:
	number = int(input("Введи число хакер!: "))
	if number == compnum:
		count = count + 1
		print("Well done, you took",count "attempts")
		elif number < 50:
			print("число не совпадает со значением compnum SORRY")
			print("Ваше число меньше загадки")
		elif number > 50:
			print("число не совпадает со значением compnum SORRY")
			print("Ваше число больше загадки")
"""Если введенное
значение совпадет с compnum,
выведите сообщение «Well done,
you took [попытки] attempts».
"""