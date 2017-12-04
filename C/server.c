#include "lib/include.h"

#define PORT 8080
#define size 100

int main(){
    
    int new_socket, valread;
    char buffer[size] = {0};
    new_socket = listen_forever();
    while(1){
        valread = recv( new_socket , buffer, size, 0);
        if(valread == 0 || valread == -1){
            printf("Client Disconnected\n");
            exit(-1);
        }
        printf("%d - %s\n", valread, buffer );
        memset(buffer , 0, sizeof(buffer));
    }
    return 0;
}