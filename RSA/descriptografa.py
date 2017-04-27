#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

#CODIGO SERVIDOR
from gera_chaves import *

# TEM ACESSO A GERAÇÃO DAS CHAVES
def descifra(cifra,n):
    arquivo2=open('chave_privada.txt','r')
    d=arquivo2.readline()
    d=int(d)

    lista=[]
    i=0
    tamanho=len(cifra)
    # texto=cifra ^ d mod n
    while i<tamanho:
        cifra[i]=int(cifra[i])
        result=cifra[i]**d
        texto=mod(result,n)
        letra=chr(texto)
        lista.append(letra)
        i=i+1
    return lista
