"""Предложите пользователю ввести имя, возраст и размер обуви для че-
тырех человек. Запросите имя одного из них в списке и выведите зна-
чения его возраста и размера обуви."""

shoes = {}

for i in range(0,4):
    name = input("Name")
    age = int(input("Age"))
    size = int(input("Size"))
    shoes[name] = {"Age": age, "Shoes": size}
ask = input("Input name: ")
print(shoes[ask])
