
n = 2
nn = 2
expressao = (n == nn)
print(expressao)

#== igualdade
# > maior que
# >= maior ou igual que
# < menor que
# <= menor que ou igual a
# "= diferente


idade = input('Qual a sua idade?'
              '')
idade=int(idade)

if idade >= 0 and idade < 18:
    print('Criança')
elif idade >= 18 and idade < 56:
    print('Adulto')
elif idade > 55 and idade < 70:
    print('Idoso')
else:
    print('Velho demais')
