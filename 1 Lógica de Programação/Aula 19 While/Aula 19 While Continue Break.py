# loop infinito
# condição sempre verdadeira
# sem condição de parada
"""
while True:
    print('Hi')

print("Essa função nunca será execuda")
"""

# Imprimir números de 0 até 20
x = 0
while x < 21:
    print(x)
    x = x + 1

# continue: pular linhas posteriores
# imprimir de 1000 até 1010, exceto 1005
print("output from continue example")
y = 1000
while y < 1011:
    if y == 1005:
        y = y + 1
        continue
    print(y)
    y = y + 1

# break: sair do laço por inteiro, não apenas pula interação
print("output from break example")
z = 1000
while z < 1011:
    if z == 1005:
        z = z + 1
        break
    print(z)
    z = z + 1

print(""
      "Output While Aninhado:")
"""
Obter saída com loop alinhado
    A vale 1 e B vale 0
    A vale 1 e B vale 1
    A vale 2 e B vale 0
    A vale 2 e B vale 1
    A vale 3 e B vale 0
    A vale 3 e B vale 1
"""
A = 1
B = 0

while A < 4:
    B = 0
    while B < 2:
        print(f'A vale {A} e B vale {B} ')
        B += 1
    A = A + 1
