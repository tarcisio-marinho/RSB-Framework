#include "lib/include.h"

  
int main(){
    
    int sock;
    int bytes_read, bytes_sent;
    char *output;

    while(1){
        
        sock = connect_forever();

        /* Connected */
        bytes_sent = send(sock , ":)" , strlen(":)") , 0);

        output = recv_message(sock);
        if(output != NULL){
            bytes_sent = send(sock, output, strlen(output), 0);
        }
    }
    
    return 0;
}