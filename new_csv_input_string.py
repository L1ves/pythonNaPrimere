"""Используя файл Books.csv из про-
граммы 111, предложите пользо-
вателю ввести новую запись и до-
бавьте ее в конец файла. Выведите
каждую строку файла .csv в отдель-
ной строке."""

import csv
file = open("Book.csv", "a")
title = input("Please input a title: ")
author = input("Please input a author: ")
year = input("Please input a year: ")
newrecords = title + ", " + author + ", "  + year + "\n"
file.write(newrecords)
file.close()

file = open("Book.csv", "r")
for row in file:
    print(row)

file.close()