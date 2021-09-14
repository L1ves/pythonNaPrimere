#strings_post_index.py
"""
Предложите пользователю
ввести его почтовый индекс.
Выведите первые две буквы
слова в верхнем регистре 1 .
"""

postAdress = input("Введите почтовый адрес: ")
start = postAdress[0:2]
print(start.upper())
#print(postAdress[0:2].upper()+""+ postAdress[2:])