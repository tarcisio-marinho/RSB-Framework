#ifndef COMMANDS_H
#define COMMANDS_H
#include "include.h"


void cd(char *path, int sock);
void upload(char *path, int sock);
void help(char * command);
char * execute(char * command, int sock);

#endif