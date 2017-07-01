#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# código do cliente
# se cair -> reconecta
# ao reiniciar o pc -> reconecta



import socket
import os

def conecta(serverHost):
    PORT=1025
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.connect((serverHost, PORT))
    except socket.error as erro:
        print('Erro ocorrido: '+str(erro))
        exit()

    while True:
        try:
            frase=raw_input()
        except KeyboardInterrupt:
            print('\nVocê escolheu sair\n')
            exit()

        # criptografou o texto
        criptografado=cipher(frase,int(chave_publica[0]),int(chave_publica[1]))
        string=str(criptografado)
        string=string.replace('[',' ').replace(']',' ').replace(' ','')
        mensagem=b'%s' %(string)
        # enviou para o servidor em forma de string o texto
        socket_obj.send(mensagem)

        # DESCRIPTOGRAFAR RETORNO DO SERVIDOR
        retorno_servidor=socket_obj.recv(1024)

        if(retorno_servidor=='exit'):
            print('saindo...')
            exit()
        print(retorno_servidor)


serverHost='127.0.0.1' # CLIENTE TEM QUE INSERIR O IP DO HOST QUE ELE QUER SE CONECTAR
conecta(serverHost)
