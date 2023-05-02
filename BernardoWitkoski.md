Jogo de Adivinhação

A) Um jogo de adivinhação de um número aleatório em Python, utilizando detecção de voz


B) Python para o backend, utilizando bibliotecas como Random (para gerarmos o número aleatório) SpeechRecognition
(para detectarmos a voz do usuário e seu palpite), para a interface gráfica foi utilizado o PyQT5, (temos também
uma biblioteca para gerar um executável da aplicação, PyInstall, mas é opcional gerar o executável).

C) A aplicação foi escrita em Python, tanto para front quanto para o back, 
e se encontra em um só arquivo .py, onde temos as funções do backend para 
iniciar o jogo, atualizar placar, chances e o mais importante, detectar o palpite do usuário e verificar 
se o usuário acertou. Na parte do frontend, temos as funções do PyQT5, que vai desenhar a tela (uma janela) 
e seus botões, textos e placares.
A comunicação entre back e front acontece quando os elementos da interface são utilizados, como um botão
por exemplo, ao apertar o botão falar, chamamos a função de detectar a fala do usuário (speak), onde também 
se encontra a lógica do jogo.

D) O código possui apenas um arquivo .py, uma imagem do ícone da aplicação, em formato PNG, o código pode ser
executado localmente com o comando python <nome-do-arquivo.py> ou podemos criar um executável da aplicação,
isso irá gerar uma pasta chamada build e outra chamda "dist" onde se encontrará o .exe 
(a pasta dist só é criada ao executar o comando de build, utilizando um comando da biblioteca PyInstall).

E) O código da aplicação inteira se encontra em um só arquivo .py, onde temos tanto a lógico do back (funções
do jogo de adivinhação em python) quanto a do front (PyQT5 para desenhar a tela, botões, textos e placares).
Temos as funções de desenhar a tela (initUI), que se baseia
em comandos dados em uma camada de estilo, onde é definido cores, fontes, tamanhos e posições. Além de desenhar a
tela, ainda temos os botões que foram utilizados para o jogo, como o botão "Falar" e "Reiniciar", neles temos
chamadas de funções backend, como speak e restart_game, além disso temos funções para atualizar a pontuação do
usuário e suas chances, isso é feito nas funções update_score_label e update_chances_label.

F) A ideial inicial era fazer esse mesmo jogo de adivinhação em uma aplicação Web, utilizando Flask, porém, como
precisávamos atualizar o número dito pelo usuário toda a vez que ele dizia, tivemos algumas complicações para
trabalhar com isso. Então optamos por desenvolver um executável local, utilizando o PyQT5 para produzir a interface,
já que a lógica do jogo e da fala já estava pronta, com isso, conseguimos utilizar o comando 
python <nome-do-arquivo.py> e a janela do jogo abriria localmente.


