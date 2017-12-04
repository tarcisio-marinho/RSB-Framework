#include "lib/include.h"

#define PORT 8080
#define IP "127.0.0.1"
#define size 100
  
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