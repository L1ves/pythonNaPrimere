#!/usr/env/bin python
# -*- coding: utf-8 -*-
import csv
"""Используя файл Books.csv , предложите поль-
зователю ввести начальный и конечный год.
Выведите все книги, выпущенные в заданном
промежутке времени."""

# предлагаю ввести
year_before = int(input("Please input year from ... to ...: ex. 1891 1900   :"))
year_after = int(input("Please input year from ... to ...: ex. 1891 1900   :"))

# открываю для поиска и добавления в новый список книг которые найду
file = list(csv.reader(open("Book.csv")))
# открываю для поиска и добавления в новый список книг которые найду
tmp = []
# ищу совпадения по годам от и до
for row in file:
    tmp.append(row)
print(tmp)
x = 0
for row in tmp:
    if int(tmp[x][2]) <= year_before and int(tmp[x][2]) >= year_after:
        print(tmp[x])
    x = x + 1
# добавляю в новый список и вывожу на печать
