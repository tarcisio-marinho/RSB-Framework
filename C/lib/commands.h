#ifndef COMMANDS_H
#define COMMANDS_H
#include "include.h"


void cd(char *path);
void upload(char *path);
void help(char * command);
char * execute(char * command);

#endif