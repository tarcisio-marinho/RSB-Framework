#ifndef COMUNICATION_H
#define COMUNICATION_H
#include "include.h"

int connect_forever();
int listen_forever();
void error(char * er);
void send_message(int sock);
void identifier(char * command);


#endif 
