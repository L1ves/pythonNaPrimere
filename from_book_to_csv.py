"""Импортируйте данные из файла Books.csv в список. Выведите список, пред-
ложите пользователю выбрать, какую строку он хочет исключить, и удалите ее.
Спросите пользователя, какие данные он хочет изменить, и предоставьте ему
соответствующую возможность. Запишите данные обратно в файл .csv с заме-
ной существующих."""
import csv

file = list(csv.reader(open("Book.csv")))

tmp = []

for row in file:
    tmp.append(row)
print(tmp)
x = 0
for i in tmp:
    string_for_del = "Номер строки --> " + str(x) + "\n" + "Содержание строки --> " + str(i)
    print(string_for_del)
    x += 1
user_input = int(input("Какую строку вы хотите исключить?: Введите строку"))
del tmp[user_input]

x = 0
for i in tmp:
    string_for_del = "Номер строки --> " + str(x) + "\n" + "Содержание строки --> " + str(i)
    print(string_for_del)
    x += 1
alter = int(input("Какие данные в строке вы хотите изменить?: Введите строку"))
x = 0
for row in tmp[alter]:
        display = x, tmp[alter][x]
        print(display)
        x += 1
part = int(input("Which part do you want to change? "))
newdata = input("Enter new data: ")
tmp[alter][part] = newdata
print(tmp[alter])

file = open("Book.csv", "w")
x = 0
for row in tmp:
    newRec = tmp[x][0] + ", " + tmp[x][1] + ", " + tmp[x][2] + "\n"
    file.write(newRec)
    x += 1
file.close()




