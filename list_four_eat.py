eat = {}
#Просим ввести 4 блюда
food1 = input("Enter a food you like: ")
eat[1] = food1

food2 = input("Enter a food you like: ")
eat[2] = food2

food3 = input("Enter a food you like: ")
eat[3] = food3

food4 = input("Enter a food you like: ")
eat[4] = food4

print(eat)
#просим удалить элемент по номеру
delete_element =  int(input("Какой элемент ты хочешь удалить? "))
del eat[delete_element] #del element
sorted(eat) #sorted list
print(eat) #print sorted list
#print(sorted(eat.values()))  second variant


