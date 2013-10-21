# -*- coding: utf-8 -*-
# @author : Rui Rebola
# @date : 6 de outubro de 2013
# obs : conversão de complexos em coordenadas polares

# esta declaração declara publico na aplicação
# o espaço de nomes math
import math

# declarção de um numero complexo
# com parte rel := 3
# e parte imaginaria igual :=6

c = 3 +6j

print c
print c.imag , c.real

a = c.real
b = c.imag

# modulo do numero complexo
r = math.sqrt( a ** 2 + b ** 2)
print " modulo = {0} " . format(r)

# calculo alternativo do modulo
r= (a**2 + b**2) ** 0.5
print " modulo = 0 {0}" . format(r)

# calculo do argumento theta
t = math.atan2(b ,a )

# conversão de radianos par graus
print t * 180.0 / math.pi

#verificação das diferenças entre atan2() e atan()
print math.atan2(-2,-2) , math.atan2( 2 , 2)
print math .atan (-2/ -2), math.atan (2/2)
