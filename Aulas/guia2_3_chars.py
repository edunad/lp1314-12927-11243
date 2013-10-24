# -*- coding: utf-8 -*-
# @author: Rui Rebola
# @date: 4 de outubro de 2013
# @obs: conversao de caracteres

l1 = [ 2 , 2 , 3 , 4 ]
l2 = [ " sjfdlkjsdljf " , "kjslfdsj " ]
l3 = [ l1 , l2 ]
l4 = list ( "Uma carrada de errres " )


print l4

#eliminação dos erres de l4 e conversão da string s5
# tecninca n1
# programação imperativa

s5 = ""

for x in l4:
    if x == "r":
        pass
    else:
        s5 += x
        pass
    pass
print s5

#tecnina n2
#programação funcional

s6 = reduce (lambda x, y: x + y, filter(lambda x: x!= "r" , l4))

print s6
