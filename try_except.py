try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("0 division")
except ValueError as err:
    print(err)