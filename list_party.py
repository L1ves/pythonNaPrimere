#list_party.py
"""
Предложите пользователю ввести имена трех людей, которых он хочет
пригласить на вечеринку, и сохраните их в списке. После того как будут
введены все три числа, спросите, хочет ли пользователь добавить еще
одно имя. Если ответ будет положительным, предложите ему добавлять
имена, пока не получите ответ «no». После ответа «no» выведите количе-
ство людей, приглашенных на вечеринку.
"""

name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1, name2, name3]

another = input("Would you like add another people? (y/n)")

while another == "y":
	newname = party.append(input("Enter another name: "))
	another = input("Would you like add another people? (y/n)")
print("you have ", len(party), " friends")
