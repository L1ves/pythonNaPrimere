#strings_all_vocubulars.py
"""
Предложите пользователю ввести слово в верхнем регистре. Если
не все буквы слова будут указаны в верхнем регистре, попросите
ввести слово заново. Повторяйте попытки, пока пользователь не
введет сообщение в верхнем регистре.
"""

wordUpper = input("Введите слово в верхнем регистре: ")
"""
if wordUpper.isupper():
	print("Ok!")
else:
	print("Try again! ")


upper = wordUpper.upper()

while wordUpper is not upper:
	input("Введите слово в верхнем регистре: ")
	if wordUpper.isupper:
		print("ok")
"""

wrong  = False

while wrong == False:
	if wordUpper.isupper():
		print("it's ok!")
		wrong = True
	else:
		print("Try again! ")
		wordUpper = input("Введите слово в верхнем регистре: ")