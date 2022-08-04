# Informar se input é par ou ímpar, e alertar se não for inteiro

num = input("Número Inteiro: ")
teste = num.isnumeric()
try:
    num = int(num)
    if num % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
except:
    teste == False
    print('Error: Número inteiro e válido somente')
