#strings_len_name.py

"""
Предложите пользователю
ввести свое имя, а затем
выведите длину имени.
Запросите фамилию и вы-
ведите длину фамилии.
Соедините имя с фамили-
ей, разделив их пробелом,
и выведите результат. Нако-
нец, выведите длину полно-
го имени (включая пробел).
"""

len_name = input("Введите свое имя: ")
print(len(len_name))
len_surname = input("Введите свою фамилию: ")
print(len(len_surname))

print("Ваше имя и фамилия: ", len_name, " ", len_surname)
fullName = len_name + " " + len_surname
print(len(fullName))