texto = 'Python s2'
# índices   [012345678] positivos
# índices  -[987654321] negativos
print(texto[2])  # imprimir letra t

url = "www.google.com.br/"  # imprimir a barra; último caractere via índice
print(url[-1])

#fatiamento de strings
texto2 = texto[2:6]  # imprimir thon
texto3 = texto[:6] # imprimir Python
texto4 = texto[7:] # imprimir thon
texto5 = texto[-9:-3]
print(texto2, texto3, texto4, texto5)

nome = "Paralelepipedo Vermelho"

#imprimir de 2 em 2
print(nome[0::2])
print(nome[0:len(nome):2])
