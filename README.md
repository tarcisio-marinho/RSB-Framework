# RSB Framework

Reverse Shell Backdoor is a framework to control infected machines with some cool interactions.
It's capable of send files, run programs in the background, screenshot and shit.

There are two versions of the code, the C and Python. If you want to learn about
sockets and reverse connection, you should check it out.


[![Travis branch](https://img.shields.io/travis/rust-lang/rust/master.svg)](https://github.com/tarcisio-marinho/RSB-Framework)
[![Travis branch](https://img.shields.io/cran/l/devtools.svg)](https://github.com/tarcisio-marinho/RSB-Framework/blob/master/LICENSE)
[![Travis branch](https://img.shields.io/badge/made%20with-%3C3-red.svg)](https://github.com/tarcisio-marinho/RSB-Framework)
[![Travis branch](https://img.shields.io/github/stars/tarcisio-marinho/RSB-Framework.svg)](https://github.com/tarcisio-marinho/RSB-Framework/stargazers)

# Disclaimer

This Framework musn't be used to harm/threat/hurt other person's computer.

It's purpose is only to share knowledge and awareness about Computer virus/Operating Sistems/Programming,  made for learning and awareness about secutiry.

The program isn't complete nor all the funcionalities are working.


# What's a backdoor ?

Backdoor is a computer virus popular known as trojan horse. It work's as a reverse shell to victim computer. So the attacker maintains access to victim computer after the bridge with some 
system vulnerability exploitation.



# How to use ? 
 
First the victim should run the backdoor compiled in the computer. 
Then when the attacker run the servidor.py he shall get a reverse connection to the victim comuter.
    
**Victim:**
    
    python backdoor.py
    
**Attacker:**
    
    python servidor.py
    
    
 
 # Uses 
 - It can be used to control the victim computer with a reverse shell.
 - Also you can be used to controll your own computer without being home!
 - Send and download files, run programs.
     
     
# Backdoor features : 
- [x] Remote connection.
- [x] Download files from the victim machine.
- [x] Send files to victim machine.
- [x] Persistence.
- [x] Screenshot of the victim screen.
- [x] Execute other programs in the victim computer.
- [ ] Backdoor complete (Only when all features ready).


# Instalation

If you want to run **Python** version you need to install all the dependecies


**linux**:

    ~$ sudo pip install -r requeriments.txt
**windows**:

    pip install -r requeriments.txt
    
If you want to run **C** code version you dont need to install any dependecies.
    

# Compiling

The **Python code** needs to be compiled or be executed as a script (not recommended).

**linux:**

    pyinstaller -F --clean -w backdoor.py -n backdoor


**windows:**

    pyinstaller -F --clean -w backdoor.py -i icon.png

The **C code** needs to be compiled.

	~$ chmod +x comp.sh
    ~$ sh comp.sh
    
or

	~$ gcc backdoor.c lib/communication.c  lib/commands.c -o bin/client
	~$ gcc server.c lib/communication.c lib/commands.c -o bin/server
