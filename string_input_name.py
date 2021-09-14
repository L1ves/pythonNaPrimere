#string_input_name.py
"""
Предложите пользователю ввести имя,
а затем сообщите, сколько в нем глас-
ных букв.
"""
vovels_in_name = []
name = input("input youre name: ")
name = name.lower()

vovels = ["a", "e", "u","i","y","o"]

for i in name:
	if i in vovels:
		vovels_in_name.append(i)
print("Vovels = ", len(vovels_in_name))


