A - A ideia principal do projeto é ser feito um jogo de adivinhação de números onde
o computador gera um numero aleatório e o usuário tenta adivinhar em determinadas tentativas
que número é esse, com o decorrer do projeto também foi implementado um esquema de pontuação.

B - import random - Para geração de um número randomico
    import speech_recognition as sr - Para reconhecimento de voz
   
   As bibliotecas a baixo utilizadas, são para a criação da interface ou seja nosso front
   from PyQt5 import QtCore, QtGui, QtWidgets 
   from PyQt5.QtGui import QColor 
    
C - Tanto para o back quanto para o front foi usado o python, por ser utilizado o python 
usamos sua propria interface o que facilitou pois podiamos tanto executar localmente
ou gerar um executavel

D - Como comentado acima foi utilizado o python para o front quanto o back ou seja apenas tivemos um arquivo nele foi possível fazer tudo que queriamos desde a criação de sua interface até a logica do jogo. Porém vale ressaltar que para rodar é necessário executar um comando um roda localmente e com outro comando é possivel fazer a criação de um executavel
com a criação do executavel ele cria outra pasta adicionando o executavel nela. 

E - Tanto o back quanto o front foi utilizado o python, ele possui uma propria interface o que possibilita criar um front usando somente ele usando a biblioteca PyQt5 para a criação dessa interface. Com tudo isso foi possivel ir apenas desenhando a tela de acordo com a logica do jogo no caso apenas adicionando interface para cada ação do jogo

F - Bom primeiro começamos definindo as variaveis que precisariamos o score chances e number
depois chamamos a função initUI para inicializar o jogo, atribuimos Estilos a pagina inicial
setamos o icone da janela, depois partimos para a logica do jogo, ela funciona da sequinte maneira o computador gera um número aleatório e o usuário por meio da fala tenta adivinhar o numero. Na logica atribuimos a questão de chances ou seja o usuário tem 10 chances para acertar. O jogo ajudará dizendo se o numero é maior ou menor do que o usuário falou, caso ele acerte o numero aparece uma mensagem falando que ele acertou e mostra seu score desablitando o botão de jogar e possibiltando o usuário a reiniciar o jogo. e caso acabe suas tentativas aparece a mensagem que ele perdeu, ele perde caso suas chances chegarem a 0. Também na mensagem é mostrado o número correto. Caso o computador não entenda ou o usuário fale algo diferente de um número ele cai em um expect e aparece mensagem de acordo com problema. Também é feito um esquema de pontuação onde a pontuação é o número de chances que o usuário possui. E assim ela vai se acumulando, ou seja, se o usuario acertar o numero com 8 tentativas ele tem 8 pontos na proxima rodada ele acertar com 5 tentativas ele tem 13 pontos mas caso o usuário não acerte sua pontuação não é somada ou seja continua como está. Depois disso apenas é apenas chamando as funções necessárias e para a execução do projeto.