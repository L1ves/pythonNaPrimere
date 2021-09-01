#strings_favourite_school_discipline.py
"""
Предложите пользователю ввести его любимый школьный предмет.
Выведите его так, чтобы после каждой буквы следовал дефис —
например, S-p-a-n-i-s-h-.
"""

discipline = input("Введите любимый школьный предмет: \n")

for i in discipline:
	print(i,end="-")