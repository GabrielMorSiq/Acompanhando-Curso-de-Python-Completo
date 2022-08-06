#       Índices
#       01234............................33
frase = "o rato roeu a roupa do rei de roma"
tamanho_frase = len(frase)
nova_frase = ""
# pecorrer cada caractere via índices e os adicionar em string vazia

contador = 0

while contador < tamanho_frase:
    nova_frase += frase[contador]
    print(nova_frase) # ver construção da string
    contador += 1

print(nova_frase)