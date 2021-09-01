"""Создайте новый файл с именем Names.txt . Добавьте в него пять имен,
отображающихся на разных строках. После запуска программы найдите
папку, в которой располагается ваша программа; убедитесь в том, что файл
был создан."""

file  = open("Names.txt","w")
file.write("Lydmila\n")
file.write("Katya\n")
file.write("Irina\n")
file.write("Natasha\n")
file.write("Nina\n")
file.close()