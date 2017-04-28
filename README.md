# SSH
servidor e cliente ssh
Protocolo RSA para troca de chaves publica

Não foi feito para ser eficiente ou seguro suficiente para ser usado em aplicação real
Feito apenas por diversão e aprendizado
Não use para nada importante
# Primeira vez rodando
    ~$ python servidor.py
    ~$ insira a senha para o cliente entrar no servidor
    ~$ python cliente.py
- a senha é salva no arquivo senha.txt em forma de hash SHA1
- na pasta logs são salvos os arquivos 

    historico.txt -> guarda os comandos digitados pelo cliente
    conectados.txt -> guarda os IP's conectados no servidor
