#include "lib/include.h"


int main(int argc, char *argv[]){
    
    int new_socket, error_output;
    char buffer[size] = {0};
    char output[MAX_TERMINAL_OUTPUT] = {0};
    int isalive;

    while(1){
        printf("Trying to connect\n");
        new_socket = listen_forever();
        printf("Connected!\n");

        while(1){
            isalive = 1;
            send_message(new_socket);
            recv_client_message(new_socket, &isalive);
            if(isalive == 0){
                break;
            }
            
        }
    }
    return 0;
}