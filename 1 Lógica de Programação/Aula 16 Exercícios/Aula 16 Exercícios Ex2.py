# Pergunte a hora.
# Retorne conforme a hora: bom dia (0-11) boa tarde (12-17) boa noite (18-23)

num = input('Digite as horas (0-23): ')
teste = num.isnumeric()

if teste:
    num = int(num)
    if 0 <= num <= 11:
        print('Bom dia')
    elif 12 <= num <= 17:
        print('Boa tarde')
    elif 18 <= num <= 23:
        print('Boa noite')
    else:
        print('Favor digitar hora válida.')
else:
    print('Error: Invalid input format. Try again')
