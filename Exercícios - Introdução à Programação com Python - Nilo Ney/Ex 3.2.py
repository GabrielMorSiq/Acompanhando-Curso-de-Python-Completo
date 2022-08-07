"""
Complete a tabela a seguir, respondendo True ou False. Considere a = 4, b = 10, c = 5.0, d = 1 e f = 5.

Expressão Resultado        Expressão Resultado
a == c    ○ True ○ False   b > a     ○ True ○ False
a < b     ○ True ○ False   c >= f    ○ True ○ False
d > b     ○ True ○ False   f >= c    ○ True ○ False
c != f    ○ True ○ False   c <= c    ○ True ○ False
a == b    ○ True ○ False   c <= f    ○ True ○ False
c < d     ○ True ○ False
"""
a = 4
b = 10
c = 5.0
d = 1
f = 5

print(bool(a == c))
print(bool(a < b))
print(bool(d > b))
print(bool(c != f))
print(bool(a == b))
print(bool(c < d))
print(bool(b > a))
print(bool(c >= f))
print(bool(f >= c))
print(bool(c <= c))
print(bool(c <= f))