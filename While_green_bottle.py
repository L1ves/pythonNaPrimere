#Выведите строки «There are [счетчик] green bottles hanging on the wall, [счетчик] green bottles
num = 10

while num > 0:
	print("There are",num, "green bottles hanging on the wall", num, "green bottles hanging on the wall, \
		and if 1 green bottle should accidentally fall")
	num = num - 1
#Затем выведите вопрос: «how many green bottles will be hanging on the wall?». 
	answer = int(input("how many green bottles will be hanging on the wall?"))
	if answer = num:
		print("There will be",num "green bottles hanging on the wall")
	else:
		while answer != num:
			answer = int(input("Nope.Try again"))
print("There are no more green bottles hanging on the wall")


#Если пользователь ответит правильно, выведите сообщение «There will be [счетчик] green bottles hanging on the wall». 
#Если пользователь ответит неправильно, выведите сообщение «No, try again», пока не будет дан правильный ответ. 
#Когда счетчик уменьшится до 0, выведите сообщение «There are no more green bottles hanging on the wall».