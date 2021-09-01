#d_array_append_string.py
"""
Используя двумерный список из задачи 096, пред-
ложите пользователю выбрать строку и выведите
только ее. Предложите ввести новое значение, до-
бавьте его в конец строки, после чего снова выведите
измененную строку.
"""

double_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

print(double_array)
user_input = int(input("Input string: "))
print(double_array[user_input])
new_value_user = int(input("Input new string: "))
double_array[user_input].append([new_value_user])
print(double_array[user_input])

