# Len retorna int - Quantidade de caracteres

# Não funciona em tipos numéricos

usuario = input('Digite seu usuario')
qttd_caracteres = len(usuario)

if qttd_caracteres < 6:
    print('Caracteres insuficientes')
else:
    print('Cadastrado')
print(usuario, qttd_caracteres, type(qttd_caracteres))


# conta espaços
# oq é retornado via len não precisa ser convertido

string1 = input('Digite algo: ')
string2 = input('Digite algo: ')
print(f'A quatidade total de caracteres digitados foi {len(string1) + len(string2)}')
