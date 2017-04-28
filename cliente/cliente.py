#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import socket
import sys
sys.path.append('../')
from RSA.criptografa import *
from RSA.descriptografa import *
from RSA.gera_chaves import *


# CLIENTE TAMBEM TEM QUE GERAR AS CHAVES PUBLICAS E PRIVADAS
# AES para salvar as senhas privadas e publicas
def conecta(serverHost):
    porta=6064
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.connect((serverHost, porta))
    except socket.error as erro:
        print('Erro ocorrido: '+str(erro))
        exit()
    # chave publica do servidor
    data = socket_obj.recv(1024) # recebeu do servidor a chave publica
    chave_publica=data.split(',') # separou a chave -> N e E

    # TESTE PARA GERAR CHAVES CORRETAS do cliente
    while True:
        try:
            palavra_teste='oi'
            gerador()
            arquivo1=open('chave_publica.txt','r')
            n=arquivo1.readline()
            n=int(n)
            e=arquivo1.readline()
            e=int(e)
            criptografado=cipher(palavra_teste,n,e)
            descriptografado=descifra(criptografado,n)
            novo=str(descriptografado)
            novo=novo.replace(']','').replace('[','').replace("'","").replace(',','').replace(' ','')
            if(novo==palavra_teste): # achou as chaves corretas -> para e vai para a conexão
                break
            else:
                continua_while=0
        except ValueError as e:
            print('Erro '+str(e) +'tentando proxima chave')
    # GEROU A CHAVE
    

    senha=raw_input('Digite a senha para conectar ao servidor: ')

    criptografado=cipher(senha,int(chave_publica[0]),int(chave_publica[1])) # criptografou o texto
    string=str(criptografado)
    string=string.replace('[',' ').replace(']',' ').replace(' ','')
    mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
    socket_obj.send(mensagem)

    confirmacao=socket_obj.recv(1024)
    if(confirmacao=='1'):
        print('Conectado ao servidor\nConexão criptografada\n')
    elif(confirmacao=='-1'):
        print('Senha incorreta\nSaindo...')
        exit()
    else:
        print('deu algum erro\nSaindo...')
        exit()

    # Recebe o nome de usuario conectado
    usuario_conectado=socket_obj.recv(1024)
    usuario_conectado=usuario_conectado.replace('\n','')

    while True:
        frase=raw_input(usuario_conectado+'@'+serverHost+':~$ ') # texto a ser criptografado e enviado
        criptografado=cipher(frase,int(chave_publica[0]),int(chave_publica[1])) # criptografou o texto
        string=str(criptografado)
        string=string.replace('[',' ').replace(']',' ').replace(' ','')
        mensagem=b'%s' %(string) # enviou para o servidor em forma de string o texto
        socket_obj.send(mensagem)
        retorno_servidor=socket_obj.recv(1024)
        if(retorno_servidor=='exit'):
            print('saindo...')
            exit()
        print(retorno_servidor)


serverHost='127.0.0.1' # CLIENTE TEM QUE INSERIR O IP DO HOST QUE ELE QUER SE CONECTAR
conecta(serverHost)
