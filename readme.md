# Quebrando cifra XOR com chave de 1 caractere

1) Ao trabalhar com cifras, é importante sempre operar sobre bytes "raw", não codificados em strings. Usaremos hexadecimal ou Base64 para impressão somente ("pretty printing"). Abaixo temos um exemplo, a string em Base64, quando decodificada e convertida para hexadecimal dá o seguinte resultado:
Base64     : QWNvcmRhUGVkcmluaG9RdWVob2pldGVtY2FtcGVvbmF0bw==
hexadecimal: 41636f72646150656472696e686f517565686f6a6574656d63616d70656f6e61746f

Mas lembre-se, todas as operações sobre esta string devem usar os valores não codificados (use vetores char ou int).
Nesta primeira parte, faça funções para codificar/decodificar entre "raw", Base64 e hexadecimal.

criado módulo `convert` com várias funções de conversão entre bytes, base64, hexadecimal e ascii (ascii para facilitar a interpretação também em alguns casos)

2) Faça uma função que recebe dois buffers de mesmo tamanho e realiza uma cifra simples do tipo XOR. Por exemplo, fazendo XOR bit-a-bit do plaintext abaixo com a chave, obtem-se o ciphertext a seguir.
plaintext : 41636f72646150656472696e686f517565686f6a6574656d63616d70656f6e61746f
chave     : 0b021e0701003e0a0d060c0807063d1a0b0f0e060a1a020c0f0e03170403010f130e
ciphertext: 4a61717565616e6f697465666f696c6f6e67616c6f6e67616c6f6e67616c6f6e6761

criado módulo `xor_cipher` com uma função que aplica xor entre uma chave e um valor previamente definidos

3) O ciphertext abaixo foi encriptado usando-se XOR bit-a-bit com uma chave de um único caracter. Encontre a chave e decifre a mensagem. É possível fazer isto com o código da parte 2, testando todas as letras do alfabeto e analisando visualmente as saidas para descobrir a chave correta. Porém, não faça isto. Crie uma forma automatizada de encontrar a chave (a Estatística é sua amiga)

072c232c223d2c3e3e2c2328232538202e2c3f3f223d223f2c3c3824072c232c223d2c3e3e2c2328232538202b24212028232c191b1b222e283c382828233f22212c2238393f222e242a2c3f3f223d223f2c2408232c22292c2f22212c3d3f223c38283b2c242c2e222339282e283f002c243e38203d22382e2228202c243e38203e282e38212239283f2024232c002c3e38202122382e223d222928393f222e22232c283e3c3824232c19382922243e3e22272c2b2c373d2c3f3928292c3f223924232c082c3f223924232c272c2b2c373d2c3f392829283b222e281c3828392820242928242c3e392c22202229283f232c3e082220283e202225222028203c38283b243b242c232c3e2e2c3b283f232c3e

criado módulo `break_hex_cipher` com uma função que recebe uma string hex, testa todas as chaves de caracteres existentes, para cada tentativa, verifica se o resultado inclui caracteres não printaveis, e atribui uma pontuação baseada na frequência de caracteres

Feito em python versão 3.10.11