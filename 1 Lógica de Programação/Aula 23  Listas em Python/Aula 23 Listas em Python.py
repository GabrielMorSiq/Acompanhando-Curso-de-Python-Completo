"""
Variável tem um valor. Listas... Vários.
lista = [1, 2, "Luiz"]

"""

# índices
#         0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 'E']
#       -5    -4   -3   -2   -1

lista2 = [1, 10.5, "Agua"]
# Mudar string para Coca
lista2[2]='Coca'
print(lista2)

# Imprimir índices do 1 ao 4, a cada 2
lista3 = ['A', 'B', 'C', 'D', 'E']
print(lista3[1:4:2])

# Inverter string
print("#####")
lista4 = ['A', 'B', 'C', 'D', 'E']
print(lista4[::-1])

# concatenar
print("#####")
l1 = [1, 2, 3]
l2 = [3, 4, 5]
l3 = l1 + l2
l1.extend(l2)
l2.extend(('a'))

print(l3)
print(l1)
print(l2)

print("#####")
l5 = [1, 2, 3]
# Adicionar string e +1 índice com append; inserir elemento
l5.append("Último")
l5.insert(1, 'segundo')
l5.pop(0)
print(l5)

print("#####")
l10 = [1, 2, 3, 4, 5, 6, 7]
# remover 2, 3, 4, 5
del(l10[1:4])
print(l10)

# lista com múltiplos de 8; imprimir
print("#####")
lista15 = list(range(0,100,8))
print(max(lista15))
print(min(lista15))

# soma de valoress
print("#####")
lista20 = list(range(0,101,10))
soma = 0
for item in lista20:
    print(soma + item)
