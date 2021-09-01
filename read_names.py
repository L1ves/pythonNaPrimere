"""Откройте файл Names.txt
и выведите данные из кода Python"""
file  = open("Names.txt","w")
file.write("Lydmila\n")
file.write("Katya\n")
file.write("Irina\n")
file.write("Natasha\n")
file.write("Nina\n")
file.close()

file = open("Names.txt","r")
print(file.read())
