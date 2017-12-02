#include "commands.h"

void cd(char *path){

}

void upload(char *path){

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

void help(char * command){
    
    if(strcmp(command, "default")){
        printf("Commands: \n");
        printf("Upload\nHelp");

    }
    else if(strcmp(command, "help") == 0){
        printf("This command display information about other commands\n");
        printf("Usage:\nhelp <command>");
    }
    else if(strcmp(command, "upload")){
        printf("Upload command is used to send file to victim machine\n");
        printf("Usage:\nupload <path/to/file>");
    }
}