# Sempre ler documentação
# Não posso converter 'a' em inteiro. E se em um int.(entrada) o utilizador inserir 'a'?
# Checar se pode entrada pode ser convertida
# Funções de ‘strings’ > checar se número pode ser convertido em inteiro
# isnumeric isdigit isdecimal

# ao pedir número, saber se string pode ser convertida em número inteiro
# isnumeric > true se todos os caracteres da string são numéricos (ex: 12.3 é F, ponto flutuante)
# # isnumeric >

num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

print(num1.isnumeric())

if num1.isnumeric and num2.isnumeric:
    print(num1 + num2)
else:
    print("Não consegui converter")

# ou

try:
    num1 = float(num1)
    num2 = float(num1)
    print(num1 + num2)
except:
    print("Error")
