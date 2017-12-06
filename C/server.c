#include "lib/include.h"


int main(){
    
    int new_socket, bytes_read, bytes_sent;
    char buffer[size] = {0};
    new_socket = listen_forever();

    while(1){
        fgets(buffer, 100, stdin);
        bytes_sent = send(new_socket, buffer, size, 0);
        bytes_read = recv( new_socket , buffer, size, 0);
        if(bytes_read == 0 || bytes_read == -1){
            printf("Client Disconnected\n");
            exit(-1);
        }else{
            printf("%s\n", buffer );
            memset(buffer , 0, sizeof(buffer));
        }
    }
    return 0;
}