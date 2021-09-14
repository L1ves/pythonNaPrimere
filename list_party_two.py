 #list_party_two.py

name1 = input("Input name: ")
name2 = input("Input name: ")
name3 = input("Input name: ")

party = [name1,name2,name3]

another_name = input("Хотите ввести еще имя? (y/n)  ")
while another_name == "y":
	party.append(input("Input name again:  "))
	another_name = input("Хотите ввести еще имя? (y/n)  ")
	print("На вечеринку приглашено ", len(party), "друзей!  ")
print(party)

still = input("Введите имя и я покажу вам каким в списке этот гость. ")

print(party.index(still))

still_user = input("Хотите ли вы чтобы я удалил этого человека из списка? (yes/no)  ")
if still_user == "yes":
	party.remove(still)
print(party)