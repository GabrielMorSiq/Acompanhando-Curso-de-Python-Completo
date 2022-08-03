while True:
    want = input("Do you want to use the calculator? [y/n]: ")
    if want != 'y':
        break

    num1 = input("Enter an integer: ")
    num2 = input("Enter another integer: ")
    oper = input("Enter an operator (+ - * /): ")

    try: # Preciso aprimorar o código. Input de não números quebra a execução código. Mas agora já se aceita nº negativos
        if '-' in num1:
            num3 = num1.replace("-", "")

        if '-' in num2:
            num4 = num2.replace("_", "")

        if not num3.isdecimal() or not num4.isdecimal():
            print("Invalid number(s)")
            break
    except:
        pass

    num1 = int(num1)
    num2 = int(num2)
    if oper != '+' and oper != '-' and oper != '*' and oper != '/':
        print("Invalid Operator")
        continue

    if oper == '+':
        print(f'The sum of {num1} and {num2} is {num1 + num2}')
    elif oper == '-':
        print(f'The difference of {num1} and {num2} is {num1 - num2}')
    elif oper == '*':
        print(f'The multiplication of {num1} and {num2} is {num1 * num2}')
    else:
        if num2 == 0:
            print("Undefined")
            continue
        print(f'The division of {num1} and {num2} is {num1 / num2:.3}')

print("Thank you!")
