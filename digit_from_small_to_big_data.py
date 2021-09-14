#!/usr/bin/env python
import random
"""Определите подпрограмму,которая предлагает поль-
зователю выбрать большоеи маленькое число, а затем
генерирует случайное числоиз этого диапазона и сохра-
няет его в переменной с име-нем comp_num.Определите другую подпро-
грамму, которая выводитсообщение «I am thinking of a number...», после чего пред-
лагает пользователю угадать загаданное число.
Определите третью подпро-грамму, которая проверяет,совпадает ли comp_num
с предположением пользо-вателя. Если совпадает, то
подпрограмма выводит со-
общение «Correct, you win»;в противном случае цикл
продолжается, а подпрограм-ма сообщает, больше или
меньше их предположениезагаданного числа, и предла-
гает сделать новую попытку до тех пор, пока пользова-
тель его не угадает."""

def big_and_small_digit():
	small_digit = int(input("Enter a small digit: "))
	big_digit = int(input("Enter a big digit: "))
	comp_num = random.randint(small_digit, big_digit)
	return comp_num

def message():
	print("I am thinking of a number... ")
	user_input = int(input("Guess the digit: "))
	return user_input

def check_answer(comp_num,user_input):
	tryAgain = True
	while tryAgain == True:
		if comp_num == user_input:
			print("Correct you win! ")
			tryAgain = False
		elif comp_num > user_input:
			user_input = int(input("Too low, try again: "))
		else:
			user_input = int(input("Too high, try again: "))

def main():
	comp_num = big_and_small_digit()
	user_input = message()
	check_answer(comp_num, user_input)

main()




