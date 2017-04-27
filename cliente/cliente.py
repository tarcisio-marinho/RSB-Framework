#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import socket
import sys
sys.path.append('../')
from RSA.criptografa import *


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
    # chave publica
    data = socket_obj.recv(1024) # recebeu do servidor a chave publica
    chave_publica=data.split(',') # separou a chave -> N e E

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
