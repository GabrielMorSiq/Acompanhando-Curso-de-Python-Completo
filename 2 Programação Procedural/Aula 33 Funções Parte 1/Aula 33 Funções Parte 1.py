# Funções - def
# print() é uma função
# posso definir minha própria função! Evitar repetições

def function():
    print('Hello World!')
    # 'Hello World!' é um parâmetro/ argumento


function()

"""
Quando funcao recebe 'Mensagem' como parâmtro, a função print é executada
Quando se chama a função e a variável msg não recebe parâmetro.. 
Se imprime o que? Não tem como. Traceback

def function(msg):
    print('Hello World!')

funtion('Oi')
funtion()
"""


def oi(msg, nome):
    print(msg, nome)


oi('Oi,', "Eu sou o Goku")
oi('Oi,', "Eu sou a Betina")


# Mensagem padrão se não ouver valores
def cha(sal='acelera'):
    print(sal)


cha()
cha('Freie')
