"""Предложите пользователю вве-
сти сначала одно число, а за-
тем другое. Сложите два числа
и спросите, хочет ли он приба-
вить еще одно. Если он введет
«y», предложите ввести еще одно
число; это продолжается до тех
пор, пока пользователь не введет
ответ «y». После того как цикл
остановится, выведите сумму.
"""

num = int(input("Insert first digit now!: "))
total == num
again = "Y"
while again == "Y":
	num2 = int(input("Insert second digit now!: "))
	total =+ num2
	again = input("Do you want to add another number? (y/n) ")
print("The total is ",total)


