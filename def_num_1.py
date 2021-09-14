#!/usr/bin/env python
"""Определите подпрограмму, которая предлагает пользо-
вателю ввести число и сохраняет его в переменной num.
Определите другую подпрограмму, которая использует
значение num и проводит отсчет от 1 до этого числа."""
def digit():
	num = int(input('Enter the digit : '))
	return num

def growUp(num):
	for i in range(0,num):
		print(i)

def main():
	num = digit()
	growUp(num)
main()
