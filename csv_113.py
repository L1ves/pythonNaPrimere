"""Используя файл Books.csv , спросите пользователя, сколь-
ко записей он хочет добавить в список, и предоставьте
ему такую возможность. После того как данные будут до-
бавлены, запросите автора и выведите все книги указан-
ного автора из списка. Если в списке нет ни одной книги
этого автора, выведите соответствующее сообщение."""

import csv

file = open("Book.csv","a")
user_input = int(input("How many strings do you want to add? input:  "))
for i in range(0,user_input):
    title = input("Please input a title: ")
    author = input("Please input a author: ")
    year = input("Please input a year: ")
    add_in_file = title + ", " + author + ", " + year + "\n"
    file.write(str(add_in_file))
file.close()
user_author = input("Input author: ")
file = open("Book.csv","r")
count = 0
for i in file:
    if user_author in str(i):
        print(i)
        count = count + 1
if count == 0:
        print("Sorry i have not this book")
file.close()