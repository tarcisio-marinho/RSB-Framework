#include "lib/include.h"


int main(){
    
    int new_socket, bytes_read, bytes_sent;
    char buffer[size] = {0};
    char output[MAX_TERMINAL_OUTPUT] = {0};
    new_socket = listen_forever();

    while(1){
        printf(">>> ");
        fgets(buffer, 100, stdin);
        bytes_sent = send(new_socket, buffer, size, 0);
        bytes_read = recv( new_socket , output, MAX_TERMINAL_OUTPUT, 0);
        if(bytes_read == 0 || bytes_read == -1){
            printf("Client Disconnected\n");
            exit(-1);
        }else{
            printf("%s\n", output );
            memset(output , 0, sizeof(output));
        }
    }
    return 0;
}