while True:
    num1 = input("Enter one number: ")
    what = input('Action sign: (+, -, *, /): ')
    num2 = input('Enter two number: ')
    if what == '+':
        print(int(num1) + int(num2))
        break
    elif what == "-":
        print(int(num1) - int(num2))
        break
    elif what == '*':
        print(int(num1) * int(num2))
        break
    elif what == '/':
        print(int(num1) / int(num2))
        break
    else:
        print('ERROR :(')