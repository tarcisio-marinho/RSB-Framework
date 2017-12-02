#include"struct.h"
#include <stdio.h>
#include <stdlib.h>

#ifndef COMUNICATION_H
#define COMUNICATION_H

void connect(Conn connection);
void error(char * er);
void send_message(Conn connection, char *msg);
void shell(Conn connection, char *msg);
char * execute(char * command);
#endif 
