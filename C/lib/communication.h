#ifndef COMUNICATION_H
#define COMUNICATION_H
#include "include.h"

/* Client functions */
int connect_forever();
char * interpreter(char * command);
char * recv_message(int sock);

/* Server functions */
int listen_forever();
void send_message(int sock);
void recv_client_message(int sock, int *isalive);
void identifier(char * command, int sock);
void error(char * er);


#endif 
