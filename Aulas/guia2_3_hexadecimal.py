# -*- coding: utf-8 -*-
# author : Rui Rebola e Eduardo Fernandes
# date : 6 de outubro de 2013
# obs : somasoma de um par de hexadec imais

# ddeclaração de duas variavis do tipo ’ str ’

a = '0xa' # representação correspondente ao numero inteiro 10
b = '0xb' # representação correspondente ao numero inteiro 11

# conversão da representação em termos de ’ str ’ em inteiro
# escolhendo a base hexadecimal 16

base = 16
a_int = int(a , base) 
b_int = int(b , base)

# soma dos inteiros resultantes
c_int = a_int + b_int

# conversão na representação hexadecimal em termos de ’ str ’
c = hex ( c_int )

# impressao no ecran do resultado
print c

# representação do numeero binario correspondete a "b"
b = '11110001'

# conversão para hexadecimal e impressao no ecran
print hex ( int (b ,2 ))
