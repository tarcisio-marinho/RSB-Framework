#include "struct.h"
#include "communication.h"

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


void cd(char *path){

}

void upload(char *path){

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

    }else if(strcmp(command, "exit") == 0){
        printf("Exiting...");
        exit(0);
    
    }else{
        output = execute(command);
        printf("%s", output);
    }
}

char * execute(char * command){
    FILE *fpipe;
    char line[256];
    char *output;
    
    output = (char *)malloc(sizeof(char) * 50000);
    memset(output, 0, 50000);

    if (!(fpipe = (FILE*)popen(command,"r"))){
        error("Pipe error");
    }

    while ( fgets( line, 256, fpipe)){
        strcat(output, line);
    }
    pclose(fpipe);
    return output;
}

void error(char * er){
    printf("Error: %s\n", er);
    exit(-1);
}
