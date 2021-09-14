import random
"""Выведите названия пяти цветов, случайным образом выберите один и пред-
ложите сделать то же пользователю. Если пользователь выберет тот же
цвет, который выбрала программа, выведите сообщение «Well done»; в про-
тивном случае выведите ответ, в котором скрывается намек на правильный
цвет. Предложите пользователю повторить попытку; если пользователь и на
этот раз не угадает, снова выведите ту же подсказку и предложите выбрать
цвет (и так далее, пока пользователь не выдаст правильный ответ).
"""

#colors = ["red", "orange", "yellow", "green", "blue"]
import random
colour = random.choice(["red", "blue", "green", "white", "pink"])
print("Select from red, blue, green, white or pink")
tryagain = True
while tryagain == True:
	theirchoice = input("Enter a colour: ")
	theirchoice = theirchoice.lower()
	if colour == theirchoice:
		print("Well done")
		tryagain = False
	else:
		if colour == "red":
			print("I bet you are seeing RED right now!")
		elif colour == "blue":
			print("Don’t feel BLUE.")
		elif colour == "green":
			print("I bet you are GREEN with envy right now.")
		elif colour == "white":
			print("Are you WHITE as a sheet, as you didn’t guess correctly?")
		elif colour == "pink":
			print("Some of you are not feeling in the PINK, as you got it wrong!")