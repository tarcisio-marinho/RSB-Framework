#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho


## CODIGO DO CLIENTE
from descriptografa import *

def mod(a,b):
    if(a<b):
        return a
    else:
        c=a%b
        return c

def cipher(words,n,e):
    tam=len(words)
    i=0
    lista=[]
    while(i<tam):
        letter=words[i]
        k=ord(letter)
        k=k**e
        d=mod(k,n)
        lista.append(d)
        i=i+1
    return lista

# VAI RECEBER PELA CONEXÃO OS VALORES DE E , N
