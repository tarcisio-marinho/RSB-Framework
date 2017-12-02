#ifndef COMMANDS_H
#define COMMANDS_H
#include "communication.h"
#include "struct.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void cd(char *path);
void upload(char *path);
void help(char * command);
char * execute(char * command);

#endif