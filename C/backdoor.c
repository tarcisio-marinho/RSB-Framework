#include "lib/include.h"

  
int main(){
    
    int sock;
    int bytes_read, bytes_sent;
    char *output;

while(1){

        /* Create socket and start new communication */
        sock = connect_forever();
        
        while(1){
            /* Connected */
            
            output = recv_message(sock);
            if(output != NULL){
                /* Still needs to check if connection is alive */
                bytes_sent = send(sock, output, strlen(output), 0);
            
            }else{
                /* Connection finished, try reconect */
                break;
            }
        }
    }    
    return 0;
}