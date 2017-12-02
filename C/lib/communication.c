#include "struct.h"
#include "communication.h"
#include "commands.h"

void connect(Conn connection){
    
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
