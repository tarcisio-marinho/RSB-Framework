#include "struct.h"


void set_ip(Conn connection, char *ip){
    strcpy(connection.ip, ip);
}

void set_port(Conn connection, int port){
    connection.port = port;
}