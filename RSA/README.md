# Este diretorio contém o código gerador das chaves publicas e privada
O método de criação delas não segue nenhum padrão do algoritmo RSA
foi algo criado por mim mesmo, seguindo algumas instruções básicas de criação 

O algoritmo de geração das chaves é o seguinte:


**Geração da Chave Pública:**
- gera o número P aleatório, P tem que ser primo
- gera o número Q também aleatório e também primo
- calcula N, sendo a multiplicação de P por Q
- N = P*Q
- calcula o totiente de N, phi(N), sendo Q-1 * P-1, pois eles são primos
- phi(N)= (Q-1)*(P-1)
- gera o número E, aleatório também, tendo que satisfazer a igualdade 1 < E < phi(N)
- depois de gerado E, o mdc entre E e phi(N) tem que ser igual a 1
- mdc(phi(N), E) == 1, se não satisfazer a isso, terá que ser gerado outro número aleatório E
- A chave pública é composta por N e E


**Geração da Chave Privada:**
- para encontrar o D, precisa satisfazer a igualdade mod(D^E, phi(N)) == 1
- a função modular se dá pelo resto de divisão entre D^E e phi(N)
- se for igual a 1, achou o D, se não, o D é incrementado até satisfazer a condição


**Criptografar texto:**
- A chave privada é guardada pelo servidor, e a pública é enviada para o cliente
- O cliente possuí o E e o N
- Para o cliente criptografar o conteúdo que será enviado para o servidor ele tem que seguir o seguinte algoritmo:
- para cada caracter na string que será enviada:
- o valor da letra em ascii é elevado a E, ex: 111^E
- o resultado é utilizado na função modular
- mod(111^E, N) -> o resultado vai ser o valor criptografado e que será enviado para o servidor
- esse processo se repete para todos os caracteres da string que será enviada


**Descriptografar:**
- Para o servidor descriptografar o texto cifrado, ele deve seguir o seguinte algoritmo:
- para o valor cifrado de cada caracter -> valor^D -> sendo D a chave privada
- o resultado ele utiliza na função modular, mod(resultado, N) -> retornando ao valor 111
- que deverá ser convertido para ascii
- o processo repete para todos os caracteres criptografados do texto cifrado
