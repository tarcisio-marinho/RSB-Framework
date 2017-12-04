#include "communication.h"
#include "commands.h"

int connect(){
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

int listen(){
    
}

void send_message(){
    char *input = (char *)malloc(sizeof(char) * 100);

    while(1){
        printf("> ");
        fgets(input, 100 ,stdin);
        identifier(input);
    }
}


void identifier(char * command){

    char *output, copy[100], *part;
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

    }else if(strcmp(part, "help") == 0){
        part = strtok(NULL, " ");
        help(part);
    
    }else if(strcmp(command, "help") == 0){
        help("default");

    }else if(strcmp(command, "exit") == 0){
        printf("Exiting...");
        exit(0);
    
    }else{
        output = execute(command);
        printf("%s", output);
    }
}

void error(char * er){
    printf("Error: %s\n", er);
    exit(-1);
}
