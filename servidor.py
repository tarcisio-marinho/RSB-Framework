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

    #conexao.close()

if __name__ == '__main__':
    meuIP='127.0.0.1'
    conecta(meuIP)
