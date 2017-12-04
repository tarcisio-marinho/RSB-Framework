#include "lib/include.h"


int main(){
    
    int new_socket, bytes_read;
    char buffer[size] = {0};
    new_socket = listen_forever();
    while(1){
        bytes_read = recv( new_socket , buffer, size, 0);
        if(bytes_read == 0 || bytes_read == -1){
            printf("Client Disconnected\n");
            exit(-1);
        }
        printf("%d - %s\n", bytes_read, buffer );
        memset(buffer , 0, sizeof(buffer));
    }
    return 0;
}