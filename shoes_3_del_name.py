"""После получения имени, возраста и размера обуви для четырех человек
запросите у пользователя имя человека для удаления из списка. Удалите
эту строку и выведите остальные данные с разбивкой по строкам."""

shoes = {}

for i in range(0,4):
    name = input("Name")
    age = int(input("Age"))
    size = int(input("Size"))
    shoes[name] = {"Age": age, "Name": name}
delete = input("delete name")
del shoes[delete]
for key, value in shoes.items():
    print(key, value)

# for name in list:
# print((name), list[name]["Age"], list[name]["Shoe size"])