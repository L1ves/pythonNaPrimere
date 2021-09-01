"""Выведите следующее меню:
1) Create a new file
2) Display the file
3) Add a new item to the file
Make a selection 1, 2 or 3:
Предложите пользователю выбрать один из вариантов.
Если пользователь введет что-либо, кроме 1, 2 и 3, про-
грамма должна вывести соответствующее сообщение об
ошибке.
Если пользователь выберет 1, предложите ему ввести на-
звание школьного предмета и сохраните его в новом файле
с именем Subject.txt . Существующий файл с таким именем
должен быть заменен новым файлом.
Если пользователь выберет 2, выводится содержимое фай-
ла Subject.txt .
Если пользователь выберет 3, предложите пользователю
ввести новый предмет, сохраните его в файле, а затем вы-
ведите все его содержимое.
Запустите программу несколько раз, чтобы протестировать
разные команды"""
print("Please make youre choice: ")
user_input = int(input("1) Create a new file: \n2) Display the file: \n3) Add a new item to the file: "))
# second = int(input("2) Display the file: "))
# third = int(input("3) Add a new item to the file: "))

if user_input == 1:
    discipline = input("Input name your school discipline: \n")
    file = open("Subject.txt", "w")
    file.write(discipline + "\n")
    file.close()
elif user_input == 2:
    file = open("Subject.txt", "r")
    print(file.read())
elif user_input == 3:
    new_discipline = input("Input name your new school discipline: \n")
    file = open("Subject.txt", "a")
    file.write(new_discipline + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("Wrong input")
