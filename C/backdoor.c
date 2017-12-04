#include "lib/include.h"

  
int main(){
    
    int sock;
    
    sock = connect_forever();
    
    
    char msg[100];
    char buffer[1024] = {0};
    int sock, bytes_read, bytes_sent;
    sock = connection();

    while(1){
        fgets(msg, 100, stdin);
        bytes_sent = send(sock , msg , strlen(msg) , 0 );
        printf("%d", bytes_sent);
        

        bytes_read = recv(sock , buffer, size, 0);
        if(bytes_read == 0 || bytes_read == -1){
            printf("Server Disconnected\n");
            exit(-1);
        }
        printf("%s\n",buffer);
    }
    
    return 0;
}