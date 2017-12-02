CC=gcc
CFLAGS=-lcrypto 
OUTPUT=bin/thedoor
RM=rm


main: thedoor.c 
	$(CC) -c thedoor.c 

communication: lib/communication.c lib/communication.h
	$(CC) -c lib/communication.c

struct: lib/struct.c lib/struct.h
	$(CC) -c lib/struct.c

out: thedoor.o lib/communication.o lib/struct.o 
	$(CC) thedoor.o lib/communication.o lib/struct.o -o $(OUTPUT) $(CFLAGS) 

clean:
	$(RM) *.o bin/thedoor lib/*.o