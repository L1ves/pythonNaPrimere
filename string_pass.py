#string_pass.py
"""
Предложите пользователю ввести пароль, а затем
предложите ввести его повторно. Если два пароля со-
впадут, выведите сообщение «Thank you». Если буквы
введены правильно, но различаются регистром, вы-
ведите сообщение «They must be in the same case»;
в противном случае выводится сообщение «Incorrect».
"""

#passwd = "SecretPass"

user_passwd1  = input("Input youre password: ")
user_passwd2  = input("Input youre password again: ")
if user_passwd1 == user_passwd2:
	print("Thank you! ")
elif user_passwd1.lower() == user_passwd2.lower():
	print("They must be in the same case! ")
else:
	print("Incorrect password, try again! ")
