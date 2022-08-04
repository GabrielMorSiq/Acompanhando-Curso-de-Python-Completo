"""""
#Tipos de dados
str - string - textos
int - inteiro - 123456 0 -12
float - real/ ponto flutuante - 10.50 -10.10
bool - booleano/logico - True/False - 10==10 retorns TRUE

#A partir do código python interpreta o tipo de dado. Se ler luiz, sabe que é string
"""""


print('Luiz', type("Luiz"))
print( 10, type(10))  #aspas com numeros o torna string
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))

print('Luiz', type('Luiz'), bool('Luiz'))
"""""
bool vai retornar uma string como falsa...
-Tivermos string vazia " "
-Zero
-Zero de ponto Flutuante
-Dicionário, listas afins vazias
Qualquer outro valor de uma string convertido para booleano retorna verdadeiro
"""""
print('10', type (int('10')))  #conversão de string para inteiro

#print('luiz', int("luiz"))  NÃO PODE
print ("\n\n\n")
print(float(10.5))

print('10' + '10')
print (10 + 10)
#print(10 + '10')
