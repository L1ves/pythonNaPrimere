def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
        # throws NameError if a >= 4
        print(3)

try:
    fun(3)
    fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError Occured and Handled")
except SyntaxError:
    print("Yeah baby SyntaxError: EOL while scanning string literal")
