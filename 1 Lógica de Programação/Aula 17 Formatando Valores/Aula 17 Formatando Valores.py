"""
Formatar valores com modificadores

:s  Texto
:d Inteiros
:f Float
:.(número)f quantidade-casas-decimais-float
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)
> esquerda
< direita
^ centro

"""

num1 = 10
num2 = 3
divisao = num1 / num2
print(
    f'{divisao:.2f}')  # (:) indica para o interpretador. (.2) = duas casas decimais, f por ser numero de ponto flutuante

# tenho o número 1, quero que tenha 10 casas decimais

num = 1
print(f'{num:0>10}')  # dois pontos, quero preencher com 0 a esquerda, um total de 10 zeros
