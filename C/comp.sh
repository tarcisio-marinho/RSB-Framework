gcc backdoor.c lib/communication.c  lib/commands.c -o bin/client
gcc server.c lib/communication.c lib/commands.c -o bin/server


