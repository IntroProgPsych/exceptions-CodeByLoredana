# 1.try 2.except 3.else 4.finally 
1/0
try:
    number = int(input("Type in a number: "))
except ZeroDivisionError:
    print("You can't divide by zero.")
except:
    print("There's something wrong.")
else:
    print("There were no errors")
finally:
    print("This is the end")