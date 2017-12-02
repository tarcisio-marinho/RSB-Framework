#include "struct.h"
#include "communication.h"

void connect(Conn connection){
    
}

void error(char * er){
    printf("Error: %s\n", er);
    exit(-1);
}

void send_message(Conn connection, char *msg){
    char *command = (char *)malloc(sizeof(char) * 100);
    char *output;
    while(1){
        printf("> ");
        fgets(command, 100 ,stdin);
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