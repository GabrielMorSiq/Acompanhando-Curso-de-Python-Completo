# Solicite nome do usuário. Menos que 4 letras, retornar "Nome curto".
# Entre 5 e 6, "Nome normal", maior que 6, "Nome enorme".

nome = input('Seu nome:')
tamanho = len(nome)

if tamanho <= 4:
    print('Nome curto')
elif 5 <= tamanho <= 6:
    print('Nome normal')
elif tamanho > 6:
    print('Nome enorme')
else:
    ...