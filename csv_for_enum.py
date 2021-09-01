import csv

file = open("Book.csv", "r")
x = 0
for row in file:
    display = "Row: " + str(x) + " - " + row + "\n"
    x += 1
    print(display)
