while True:
    try:
        number = int(input("Enter the number: \n"))
        print(18 / number)
        break 
    except ValueError:
        print("Make sure to enter a valid number.")
    except ZeroDivisionError:
        print("dont enter the value zero")