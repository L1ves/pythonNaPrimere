import random
"""
Напишите математическую игру, в которой пользователь 
должен ответить на пять вопросов. Каждый вопрос строит-
ся из двух случайно сгенерированных целых чисел (напри-
мер, [num1] + [num2]). Предложите пользователю ввести
ответ. Если пользователь ввел правильный ответ, добавьте
одно очко в его пользу. В конце игры сообщите пользовате-
лю количество правильных ответов.
"""
#5question
print("Hello and welcome in the game! Please answer to our questions. Play and win!")
score = 0

for point in range(1,6):
	answ1 = random.randomint(1,555)
	answ2 = random.randomint(1,555)
	correct = answ1 + answ2
	answer = int(input("Сколько будет ", answ1 "+ " ,answ2, " ?"))
	print(answer)
	if answer == correct:
		score = score + 1
print("You score is : ", score)
