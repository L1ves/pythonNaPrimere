#string_hello_world.py
"""
Предложите пользователю ввести слово, а затем
выведите буквы слова в обратном порядке в разных
строках. Например, если пользователь ввел строку
«Hello», результат должен выглядеть так:
Enter a word: Hello
o
l
l
e
H
"""
#word = input("Введите слово: ")
#for i in word[::-1]:
#	print(i)


word = input("Enter a word: ")
length = len(word)
num = 1

for x in word:
	position = length - num
	letter = word[position]
	print(letter)
	num = num + 1