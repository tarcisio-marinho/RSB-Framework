#ifndef COMUNICATION_H
#define COMUNICATION_H
#include "include.h"

int connect();
int listen_forever();
void error(char * er);
void send_message();
void identifier(char * command);


#endif 
