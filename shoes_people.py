"""Измените программу
102, чтобы она выво-
дила имя и возраст для
всех людей в списке, но
не их размер обуви.
"""

shoes = {}

for i in range(0,4):
    name = input("Name")
    age = int(input("Age"))
    size = int(input("Size"))
    shoes[name] = {"Age": age, "Name": name}
for name in shoes:
    print(name,shoes[name]["Age"])

