# For in
# While — não sei o fim
# For — coisas finitas

texto = 'Python'
for letra in texto:
    print(letra)

texto2 = 'Java'
for n, letra2 in enumerate(texto2):
    print(n, letra2)

# range é independente do laço
# range, argumentos: (start = 0, stop, step=1)
for n in range(10):
    print(n)

#  múltiplos de 8 entre 0 e 100
for n in range(0, 100, 8):
    print(n)
# ou
for n in range (100):
    if n % 8 == 0:
        print(n)

# continue - pula para próximo laço
# break acaba com o laço como um todo