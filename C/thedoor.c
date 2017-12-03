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
    
    int connection = 0, valread;
    struct sockaddr_in serv_addr;
    char *hello = "Hello from infected";
    char buffer[1024] = {0};
    
    if ((connection = socket(AF_INET, SOCK_STREAM, 0)) < 0){
        /* Socket creation error */
    }
  
    memset(&serv_addr, '0', sizeof(serv_addr));
    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
      
    // Convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, IP, &serv_addr.sin_addr)<=0) 
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }
  
    if (connect(connection, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0){
        /* Connection Failed */
        
    }
    send(connection , hello , strlen(hello) , 0 );
    
    valread = read(connection, buffer, 1024);
    printf("%s\n",buffer );
    return 0;
}