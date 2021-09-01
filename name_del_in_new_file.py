"""С помощью созданного ранее файла Names.txt выведите список имен в Python.
Попросите пользователя ввести одно из имен, а затем сохраните все,кроме
выбранного в новом файле, под названием Names2.txt ."""

file = open("Names.txt","r")
print(file.read())
file.close()

file = open("Names.txt","r")
del_name = input("Please input one name: ")
del_name = del_name + "\n"
for raw in file:
    if raw != del_name:
        file = open("Names2.txt","a")
        file.write(raw)
        file.close()
file.close()

