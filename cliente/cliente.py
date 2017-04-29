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

# inicia as cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
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



    try:
        senha=raw_input('Digite a senha para conectar ao servidor: ')
    except KeyboardInterrupt:
        print('\nVocê escolheu sair...\n')
        exit()

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

    # envia pro servidor a chave publica
    socket_obj.send(str(n) +','+ str(e))


    # Recebe o nome de usuario conectado
    #DESCRIPTOGRAFA
    recebido=socket_obj.recv(1024)
    recebido=recebido.split(',')
    usuario_conectado=[]
    novo_recebido=[]
    for caracter in recebido:
        caracter=caracter.replace('L','')
        novo_recebido.append(caracter) # adiciona na nova lista
    descriptografado=descifra(novo_recebido,n)
    descriptografado=str(descriptografado).replace(']','').replace('[','').replace("'","").replace(',','')
    descriptografado=descriptografado.split('  ')
    for palavra in descriptografado:
        palavra=palavra.replace(' ','')
        usuario_conectado.append(palavra)
    # FIM DESCRIPTOGRAFA
    usuario_conectado=str(usuario_conectado).replace('[','').replace(']','').replace("'","")



    while True:
        # texto a ser criptografado e enviado
        print('{0}'+usuario_conectado+'@'+serverHost+'{1}:~$ {2}').format(GREEN,BLUE,END)
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
