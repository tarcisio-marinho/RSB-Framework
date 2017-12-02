#ifndef COMUNICATION_H
#define COMUNICATION_H
#include "struct.h"
#include "commands.h"
#include <stdio.h>
#include <stdlib.h>

void connect(Conn connection);
void error(char * er);
void send_message();
void identifier(char * command);


#endif 
