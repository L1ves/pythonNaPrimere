#!/usr/env/python3
"""
user_input = input()
month = ""
january = 30
february = 31
march = 30
april = 31
may = 30
june = 31
july = 30
augest = 30
semptember = 31
november = 30
december = 31

if user_input == "january":
	month = "30"
elif user_input == "february":
	month = "28 or 29"
elif user_input == "march":
	month = "30"
elif user_input == "april":
	month = "31"
elif user_input == "may":
	month = "30"
elif user_input == "june":
	month = "31"
elif user_input == "july":
	month = "30"
elif user_input == "august":
	month = "31"
elif user_input == "semptember":
	month = "30"
elif user_input == "october":
	month = "31"
elif user_input == "november":
	month = "30"
elif user_input == "december":
	month = "31"
if month == " ":
	print("WRONG")
else:
	print("Count days in this month equal: ", month)
"""
month = input()

days = 31

if month == "january" or month == "march" or month == "may" or month == "july" or month == "semptember" \
or month == "november":
	days == 30
elif month == "february":
	days = "28 or 29"

print("Количество дней в месяце", month, "равно", days)