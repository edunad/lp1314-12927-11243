# -*- coding: utf-8 -*-

s = "Mas que belo dia"
x = "q"

if x in s: print "a letra 'q' encontra-se em s"

t = " em amsterdao"
print s + t
print 3 * t

#    0123456789
s = "abcdefghijklmnopkrstv"
print s[5], s[5:8], s[5:12:2]

print len(s)
print min(s),max(s)
print "vezes que aparece o a =", t.count('a')

print "#############################"

l = """Alma minha gentil , que te partiste
Alma minha gentil , que te partiste
Tao cedo desta vida , descontente ,
Repousa la no Ceu eternamente
E viva eu ca na terrasempre triste .
""" .splitlines()

print l
print "#############################"

f = open ("teste.txt" , "w")
s = "TEST"

for k in range(10): f.write(s + " - " + str(k) + "\n") # de 0 a 10 imprime TEST - numero (k)
f.close() #Fechar o writer

f = open("teste.txt","r")

print "o seek encontra-se em " + str(f.tell()) ## diz onde esta o seek
print f.read(5) ## le o 5 paragrafo
print "=========="
print f.read() ## le o ficheiro inteiro

print "#############################"

import pickle ## grava objectos

class Test:
    def __init__(self,x,y): ## construtor
        self.x = x
        self.y = y
    pass
pass


obj = Test(10,50) ## cria um novo objecto com o x = 10 e y = 50

f = open("teste.dat","w") # grava um ficheiro .dat
p = pickle.dump(obj,f) # converte o objector para .dat
f.close() # fecha o reader

del obj # apaga o objector anterior para voltar a ser usado

obj = pickle.load(open("teste.dat","r")) # abre o ficheiro e faz "parse" do objecto
print obj.x,obj.y # imprime o que foi guardado no objecto

print "#############################"

import csv

with open('notas.csv','wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Programação 1",17])
    writer.writerow(["Programação 2",15])

with open('notas.csv','rb') as csvfile:
    leitor = csv.reader(csvfile)
    for linha in leitor:
        print " , ".join(linha)

print "#############################"

