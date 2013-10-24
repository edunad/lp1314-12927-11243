# -*- coding: utf-8 -*-
# autor : Eduardo Fernandes e Rui Rebola
# data : 30 Setembro 2013
# obs. : Primeira AUla / PRograma 2

print type(1), type(3.4), type((3+3j))
print type("treta"), type(True and False)
a = "1"
b = "Uma"
print type(a), type(b)
print type([1,2,3,[1,2]]), type((1,2,3))

class Test:
    pass

print type(Test)

obj = Test()
print type(obj)

def func():
    return 3

print type(func)

print type(range(0,10))
print type(xrange(0,10))
print type(a > 10 if 10 else 2)
print type(a) == type("string") if "uma string" else "nao sei"

print type((3+3j)+ 2)
