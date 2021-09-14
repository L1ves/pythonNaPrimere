#Предложите пользователю ввести число от 10 до 20.
#Если введенное значение меньше 10, выведите сообщение «Too low» и предложите повторить попытку. 
#Если введенное значение больше 20, выведите сообщение «Too high» и предложите повторить попытку.
#Повторяйте до тех пор, пока не будет введено значение из диапазона от 10 до 20, 
#после чего выведите сообщение «Thank you».

digit = int(input("Input digit please man! between 10 and 20: "))
while digit > 20 or digit < 10:
	if digit > 20:
		print("Too high ")
	else:
		print("Too low ")
	digit = int(input("Try again: "))
print("Thank you man!")
