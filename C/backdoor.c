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
    
    
    char msg[100];
    char buffer[1024] = {0};
    int sock, valread, valsend;
    sock = connection();

    while(1){
        fgets(msg, 100, stdin);
        valsend = send(sock , msg , strlen(msg) , 0 );
        printf("%d", valsend);
        

        valread = recv(sock , buffer, size, 0);
        if(valread == 0 || valread == -1){
            printf("Server Disconnected\n");
            exit(-1);
        }
        printf("%s\n",buffer );
    }
    
    return 0;
}