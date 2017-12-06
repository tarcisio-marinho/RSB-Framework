#include "include.h"

/* Client functions */

int connect_forever(){
   
    struct sockaddr_in address;
    int sock = 0;
    struct sockaddr_in serv_addr;
    while(1){
        int rest = 0;
        if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        {
            printf("\n Socket creation error \n");
            rest = 1;
        }
    
        memset(&serv_addr, '0', sizeof(serv_addr));
    
        serv_addr.sin_family = AF_INET;
        serv_addr.sin_port = htons(PORT);
        
        // Convert IPv4 and IPv6 addresses from text to binary form
        if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0) 
        {
            printf("\nInvalid address/ Address not supported \n");
            rest = 1;
        }
    
        if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
        {
            printf("\nConnection Failed \n");
            rest = 1;
        }
        if(rest == 1){
            printf("Dormindo por 5 segundos");
            sleep(5);
            continue;
        }
        return sock;
    }
}

char * interpreter(char * command){
    
    char *output, copy[size], *part;
    int cd_output;

    strcpy(copy, command);

    part = strtok(copy, " ");

    if(strcmp(part, "cd") == 0){
        part = strtok(NULL, " ");
        cd(part);
        
    }else if(strcmp(command, "cd") == 0){
        cd("home");

    }else if(strcmp(part, "upload") == 0){
        part = strtok(NULL, " ");
        upload(part);

    }else{
        output = execute(command);
    }
    
    return output;
}

char * recv_message(int sock){

    char command[size] = {0}, *output;
    int bytes_read;

    bytes_read = recv(sock , command, size, 0);

    if(bytes_read == 0 || bytes_read == -1){
        /* Server disconnected */
        return NULL;
    }

    output = interpreter(command);
    return output;
}


/* Server functions*/
int listen_forever(){
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[size] = {0};        
    while(1){

        // Creating socket file descriptor
        if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0){
            error("socket failed");
        }
        
        // Forcefully attaching socket to the port 8080
        if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                                                    &opt, sizeof(opt))){
            error("setsockopt");
        }

        address.sin_family = AF_INET;
        address.sin_addr.s_addr = INADDR_ANY;
        address.sin_port = htons( PORT );
        
        // Forcefully attaching socket to the port 8080
        if (bind(server_fd, (struct sockaddr *)&address, 
                                    sizeof(address))<0){
            error("bind failed");
        }

        if (listen(server_fd, 3) < 0){
            error("listen");
        }

        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, 
                        (socklen_t*)&addrlen))<0){
            error("accept");
        }
        
        return new_socket;
    }
}

void send_message(int sock){
    char *input = (char *)malloc(sizeof(char) * size);

    printf(">>> ");
    fgets(input, size ,stdin);
    identifier(input, sock);
    
}

void recv_client_message(int sock, int *isalive){
    
    int bytes_read;
    char output[MAX_TERMINAL_OUTPUT];

    bytes_read = recv( sock , output, MAX_TERMINAL_OUTPUT, 0);
    if(bytes_read == 0 || bytes_read == -1){
        printf("Client Disconnected\n");
        *isalive = 0;

    }else{
        printf("%s\n", output );
        memset(output , 0, sizeof(output));

    }
}

void identifier(char * command, int sock){

    char *output, copy[100], *part;

    strcpy(copy, command);
    part = strtok(copy, " ");

    if(strcmp(part, "upload") == 0){
        part = strtok(NULL, " ");
        upload(part);

    }else if(strcmp(part, "help") == 0){
        part = strtok(NULL, " ");
        help(part);
    
    }else if(strcmp(command, "help") == 0){
        help("default");

    }else if(strcmp(command, "exit") == 0){
        printf("Exiting...");
        exit(0);
    
    }else{
        send(sock, command, size, 0);
    }
}

void error(char * er){
    printf("Error: %s\n", er);
    exit(-1);
}
