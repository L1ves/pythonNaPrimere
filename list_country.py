"""
Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа. Предложите
пользователю ввести название одной из этих стран и выведите индекс (то есть позицию в списке)
этого элемента кортежа.
"""
country = input("Insert country and i print your choice with index: ")

lists = ["Russia", "USA", "China","UK","OAO"]

print(lists)

#if country in lists:
print(lists.index(country))



