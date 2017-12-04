#ifndef COMUNICATION_H
#define COMUNICATION_H
#include "commands.h"
#include <stdio.h>
#include <stdlib.h>

int connect();
int listen();
void error(char * er);
void send_message();
void identifier(char * command);


#endif 
