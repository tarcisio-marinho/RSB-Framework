#ifndef COMMANDS_H
#define COMMANDS_H
#include "include.h"


int cd(char *path);
char * upload(char *path);
void help(char * command);
char * execute(char * command);

#endif