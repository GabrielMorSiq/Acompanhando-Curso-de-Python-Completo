"""
and / or / not / in / not in
"""

nome = input('Digite seu nome:')
idade = int(input('Digite a idade:'))

if nome == 'Lucas' and idade == 30:
    print('Lucas')
elif nome == 'Tim' or nome == 'Jô':
    print('Prazer')
if not nome == "Gustavo":
    print('Gustavo')
else:
    print('esqueça')

NNOME = input('Digite seu nome:')

if 'c' not in NNOME:
    print("Não Existe")
