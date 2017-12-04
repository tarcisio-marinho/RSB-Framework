#ifndef INCLUDE_H
#define INCLUDE_H

/* Basic operations */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

/* Socket interface */
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

/* Local Library*/
#include "communication.h"
#include "commands.h"

/* Defines */

#define PORT 8080
#define size 100
#define IP "127.0.0.1"

#endif