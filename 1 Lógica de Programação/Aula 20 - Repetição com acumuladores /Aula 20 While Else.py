contador = 1
acumulador = 1


"""
Acontecerá um break sem que a condição do laço seja falsa. 
Atingir o else do while com tal verdadeiro... 
Ele não é executado, só seria quando tal fosse falso 
"""
while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
    # Note que o 6 será impresso, pois tal ocorre antes que ocorra o brean
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no Else mas não executo')


