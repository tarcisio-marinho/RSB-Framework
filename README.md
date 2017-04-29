# SSH
servidor e cliente ssh
Protocolo RSA para troca de chaves publica

Não foi feito para ser eficiente ou seguro suficiente para ser usado em aplicação real.

Feito apenas por diversão e aprendizado.

Não use para nada importante
# Primeira vez rodando
    **Em um terminal**
    ~$ python servidor.py
    ~$ configure a senha do servidor para o cliente conectar ao servidor
    **Outro terminal**
    ~$ python cliente.py
- a senha é salva no arquivo senha.txt em forma de hash SHA1
- na pasta logs são salvos os arquivos 

- historico.txt -> guarda os comandos digitados pelo cliente
- conectados.txt -> guarda os IP's conectados no servidor

**Para saber mais sobre o algoritmo usado na criptografia:**


https://github.com/tarcisio-marinho/SSH/blob/master/RSA/README.md
