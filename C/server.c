#include "lib/include.h"


int main(int argc, char *argv[]){
    
    int new_socket, error_output;
    char buffer[size] = {0};
    char output[MAX_TERMINAL_OUTPUT] = {0};

    while(1){
        printf("Trying to connect\n");
        new_socket = listen_forever();
        printf("Connected!\n");

        while(1){
            send_message(new_socket);

            error_output = recv_client_message(new_socket);
            if(error_output == err){
                break;
            }
        }
    }
    return 0;
}