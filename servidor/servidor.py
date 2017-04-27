#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import os
import datetime
import time
import socket
import sha
import subprocess
import sys

sys.path.append('../')
from RSA.gera_chaves import *
from RSA.descriptografa import *
from RSA.criptografa import *


# AES para criptografar a senha privada
def conexao(meuIP):
    # servidor
    try:
        senha=open('senha.txt','r')
        hash_senha=senha.readline() # nova senha -> senha ja escolhida -> SHA1
    except:
        senha=open('senha.txt','w')
        nova_senha=raw_input('Digite sua senha: ') # criou nova senha para o servidor
        hash_senha=sha.new(nova_senha).hexdigest() # SHA1 da senha
        senha.write(hash_senha)
        os.system("clear")

    while True:
        porta=6064

        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
        socket_obj.bind((meuIP, porta))
        socket_obj.listen(1) # escuta apenas 1 cliente
        print('Servidor rodando')


        b=0 # se o cara acertar a senha -> b=1
    	conexao,endereco=socket_obj.accept()
        hora=datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S') # hora de conexão -> unix timestamp
    	print('servidor conectado por', endereco[0],hora)
        print('gerando as chaves... ')
        while True: # TESTE PARA GERAR CHAVES CORRETAS
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
        # FIM DO TESTE -> achou as chaves corretas

        arquivo1=open('chave_publica.txt','r')
        n=arquivo1.readline()
        n=int(n)
        e=arquivo1.readline()
        e=int(e)
        conexao.send(b'' + str(n) +','+ str(e)) # envia pro cliente a chave publica
        # RECEBE A SENHA PARA SE CONECTAR AO SERVDIRO

        recebido=conexao.recv(1024)
        recebido=recebido.split(',')
        print(recebido)

        # DESCRIPTOGRAFA
        senha_descriptografada=[]
        novo_recebido=[]
        for caracter in recebido: # remove o L, que tem no fim dos caracteres
            caracter=caracter.replace('L','')
            novo_recebido.append(caracter) # adiciona na nova lista
        descriptografado=descifra(novo_recebido,n)
        descriptografado=str(descriptografado).replace(']','').replace('[','').replace("'","").replace(',','')
        descriptografado=descriptografado.split('  ')
        for palavra in descriptografado:
            palavra=palavra.replace(' ','')
            senha_descriptografada.append(palavra)
        # FIM DESCRIPTOGRAFA

        print(senha_descriptografada)
        senha_descriptografada=str(senha_descriptografada).replace('[','').replace(']','').replace("'","")
        print(senha_descriptografada)
        hash_senha_descriptografada=sha.new(senha_descriptografada).hexdigest()

        if(hash_senha_descriptografada==hash_senha):
            conexao.send('1') # acertou a senha, pode entrar
            b=1

        else:
            print('senhas diferentes, nao pode entrar')
            conexao.send('-1') # errou a senha
            conexao.close()


        # ACERTOU A SENHA -> ENTRA NO SERVIDOR
        if(b==1):
            print('IP '+str(endereco[0])+' conectou ao servidor')
            try: # tenta abrir e escrever os clientes que foram conectados
                arq=open('conectados.txt','a')
            except:
                arq=open('conectados.txt','w') # cria arquivo
            arq.write(str(endereco[0])+' - '+str(hora)+'\n') # escreve no arquivo dos hosts conectados

            #envia o nome de usuario que a pessoa esta logada
            a = subprocess.check_output('whoami', shell=True)
            conexao.send(a)

            # recebe dados enviados pelo cliente
            while True:
                # CRIA AS LISTAS QUE VÃO GUARDAR
                novo_descriptografado=[] # O PEDIDO DO CLIENTE DESCRIPTOGRAFADO -> COM STRING CORRETA
                novo_recebido=[] # O PEDIDO DO CLIENTE ORIGINAL
                historico=[] # HISTORICO DOS PEDIDOS DO CLIENTE

                recebido = conexao.recv(1024) # recebe o que o cliente mandou
                recebido=recebido.split(',') # separa em uma lista

                # DESCRIPTOGRAFA
                for caracter in recebido: # remove o L, que tem no fim dos caracteres
                    caracter=caracter.replace('L','')
                    novo_recebido.append(caracter) # adiciona na nova lista
                descriptografado=descifra(novo_recebido,n)
                descriptografado=str(descriptografado).replace(']','').replace('[','').replace("'","").replace(',','')
                descriptografado=descriptografado.split('  ')
                for palavra in descriptografado:
                    palavra=palavra.replace(' ','')
                    novo_descriptografado.append(palavra)
                # FIM DESCRIPTOGRAFA

                # tenta abrir e escrever os clientes que foram conectados
                hora=datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S')
                historico.append(str(descriptografado).replace(']','').replace('[','').replace("'","").replace(',',''))# HISTORICO DO QUE FOI ENVIADO PELO CLIENTE
                try:
                    arq=open('historico.txt','a')
                except:
                    arq=open('historico.txt','w') # cria arquivo
                arq.write(str(historico)+' - ' + str(hora)+'\n')

                # pega a pergunta e executa no servidor
                tam=len(novo_descriptografado)
                print(novo_descriptografado)
                # se o usuario digitar exit
                if(str(novo_descriptografado).replace(']','').replace('[','').replace("'","").replace(',','')=='exit'):
                    print('saindo\n')
                    conexao.send('exit')
                    conexao.close()
                    exit()

                if(tam==1):
                    comando = novo_descriptografado[0]

                elif(tam==2):
                    comando = str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])

                elif(tam==3):
                    comando = str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])+' '+str(novo_descriptografado[2])

                elif(tam==4):
                    comando = str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])+' '+str(novo_descriptografado[2])+' '+str(novo_descriptografado[3])

                elif(tam==5):
                    comando = str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])+' '+str(novo_descriptografado[2])+' '+str(novo_descriptografado[3])+' '+str(novo_descriptografado[4])

                elif(tam==6):
                    comando = str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])+' '+str(novo_descriptografado[2])+' '+str(novo_descriptografado[3])+' '+str(novo_descriptografado[4])+' '+str(novo_descriptografado[5])

                elif(tam==7):
                    comando=str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])+' '+str(novo_descriptografado[2])+' '+str(novo_descriptografado[3])+' '+str(novo_descriptografado[4])+' '+str(novo_descriptografado[5])+' '+str(novo_descriptografado[6])

                elif(tam==8):
                    comando = str(novo_descriptografado[0])+' '+str(novo_descriptografado[1])+' '+str(novo_descriptografado[2])+' '+str(novo_descriptografado[3])+' '+str(novo_descriptografado[4])+' '+str(novo_descriptografado[5])+' '+str(novo_descriptografado[6])+' '+str(novo_descriptografado[7])

                try:
                    a = subprocess.check_output(comando, shell=True)
                    conexao.send(str(a)) # envia o retorno -> 0 == comando correto
                except subprocess.CalledProcessError as e:
                    print(e)
                    conexao.send(str(e))


        conexao.close()

meuIP='127.0.0.1' # USUARIO QUE TEM QUE CONFIGURAR O IP -> PRIMEIRA VEZ RODANDO -> IFCONFIG -> INSERIR IP MANUALMENTE
conexao(meuIP)
