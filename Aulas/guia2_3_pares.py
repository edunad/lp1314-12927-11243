# -*- coding: utf -8-*-

import random

# criação de uma lista de 20 numeros inteiros aleatorios
# distribuidos uniformemente entre 0 e 99

# abordagem imperativa

l1 = list()
N = 20
k = 0
while k < N:
    l1.append (random.randint( 0,99) )
    k += 1
    pass

# lista dos numeros pares
l2 = list ()
for x in l1:
    if not (x % 2):
        l2.append(x)
        pass
    pass
#abordagem funcional
# criação da lita de dados por uso de uma compreensão de lista
l1 = [random.randint(0,99) for k in range (N) ]

#uso de um filtro com expresões lambda
l2 = filter (lambda x: not (x % 2 ) , l1)
print l2;
