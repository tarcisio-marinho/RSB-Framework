#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include<sys/unistd.h>
#include<arpa/inet.h>

#include "lib/communication.h"
#include "lib/commands.h"

#define PORT 8080
#define IP "127.0.0.1"
  
int main(){
    
    int sock;
    
    sock = connect();
    
    
    return 0;
}