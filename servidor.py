#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# programas padrao
# ls
# mkdir
# upload
# copiar arquivos
# copiar pasta

import os
import datetime
import time
import socket
import sha
import subprocess
import sys


# cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def conexao(meuIP):
    while True:
        porta=1025
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
        socket_obj.bind((meuIP, porta))
        socket_obj.listen(1) # escutando conexões
        print('{0}[+] Aguardando conexões...{1}').format(GREEN, END)
    	conexao,endereco=socket_obj.accept()
    	print('\033[1;32m[+]servidor conectado por', endereco[0])


        recebido=conexao.recv(1024)
        recebido=recebido.split(',')
        print(recebido)

        # ACERTOU A SENHA -> ENTRA NO SERVIDOR
            #envia o nome de usuario que a pessoa esta logada
        logado = subprocess.check_output('whoami', shell=True)
        logado=logado.replace('\n','')
        criptografado=cipher(logado,int(chave_publica_cliente[0]),int(chave_publica_cliente[1]))
        string=str(criptografado)
        string=string.replace('[',' ').replace(']',' ').replace(' ','')
        conexao.send(string)

        # recebe dados enviados pelo cliente
        while True:
            # CRIA AS LISTAS QUE VÃO GUARDAR
            novo_descriptografado=[] # O PEDIDO DO CLIENTE DESCRIPTOGRAFADO -> COM STRING CORRETA
            novo_recebido=[] # O PEDIDO DO CLIENTE ORIGINAL
            historico=[] # HISTORICO DOS PEDIDOS DO CLIENTE

            try:
                recebido = conexao.recv(1024) # recebe o que o cliente mandou
            except socket.error as erro:
                print('erro '+ str(e)+', Usuario saiu\n Erro causado por PS AUX\n')
                break
                continue
            recebido=recebido.split(',') # separa em uma lista

            # tenta abrir e escrever os clientes que foram conectados
            hora=datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')
            historico.append(str(descriptografado).replace(']','').replace('[','').replace("'","").replace(',',''))# HISTORICO DO QUE FOI ENVIADO PELO CLIENTE
            try:
                arq=open('logs/historico.txt','a')
            except:
                os.mkdir('logs')
                arq=open('logs/historico.txt','w') # cria arquivo
            arq.write(str(historico)+' - ' + str(hora)+'\n')

            # pega a pergunta e executa no servidor
            tam=len(novo_descriptografado)
            print(novo_descriptografado)
            # se o usuario digitar exit
            if(str(novo_descriptografado).replace(']','').replace('[','').replace("'","").replace(',','')=='exit'):
                conexao.send('exit')
                conexao.close()
                print('\nusuario escolheu sair\n')
                break
                continue



            comando = ' '.join([str(novo) for novo in novo_descriptografado])
            try:
                a = subprocess.check_output(comando, shell=True)
                conexao.send(a)
            except subprocess.CalledProcessError as e:
                print(e)
                conexao.send(str(e))


        conexao.close()

meuIP='127.0.0.1' # USUARIO QUE TEM QUE CONFIGURAR O IP -> PRIMEIRA VEZ RODANDO -> IFCONFIG -> INSERIR IP MANUALMENTE
conexao(meuIP)
