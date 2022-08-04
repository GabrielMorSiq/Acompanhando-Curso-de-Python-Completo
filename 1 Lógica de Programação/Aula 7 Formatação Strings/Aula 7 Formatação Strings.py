nome = 'Luiz Otávio'
idade = 32
altura = 1.80
peso = 80
imc = peso / altura**2
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))