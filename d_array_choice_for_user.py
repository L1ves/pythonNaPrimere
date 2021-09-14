from array import *
"""
Используя двумерный список из задачи 096, пред-
ложите пользователю выбрать строку и столбец и вы-
ведите выбранное значение.
"""

double_array = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row = int(input("Choice string: "))
col = int(input("Choice col: "))
print("result",double_array[row][col])