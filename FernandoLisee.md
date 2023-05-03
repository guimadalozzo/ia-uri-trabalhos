A) Qual é a ideia geral do projeto?

	A ideia do projeto consiste em criar cards de lembretes onde o usuario clicasse em um botão e acionaria o microfone para ser falado primeiramente o assunto do card e após isso o lembrete a ser adicionado no card, onde se o usuario clicasse novamente no botão de ativação ele poderia adicionar um novo assunto, assim criando uma tela interativa com os cards um do lado do outro.

B) Qual as tecnologias utilizadas, e porque?

	As tecnologias utilizadas foram Python, NodeJS, JS, HTML5, CSS, (Flask), Ajax

C) Qual a arquitetura do software? Quem é o back, o front, como se comunicam, etc

	Utilizamos do NodeJS para o backend do projeto, e o Python também roda no back com as bibliotecas do speech writer, utilizamos o flask server e o node para rodar o projeto em um localhost, o node faz a comunicação com o front que foi utilizado HTML como base, CSS para utlização básica do projeto e JS para chamar as funções do Python.

D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.

	Na pasta Flask server está armazenado o arquivo Python, responsavel por rodar no backend aguardando o front com nodejs chamar a função do speech writer, a pasta node é onde está armazenado todo o projeto front rodando em um localhost e dentro dela temos pasta images, pasta public onde contém a estilização do projeto e as principais animações e avisos criados com JS, também contém as funções de manipular o front para criar os novos cards visuais dentro do container para ser exibido na tela. Na pasta views temos o arquivo index.html com a tela principal em html e css que foi criada apenas com o intuito de exibir as regras para utilização do projeto na prática, a pasta layouts contém o arquivo base.html que é onde está com caminhos de alguns frameworks utilizados como o Ajax e arquivos do projeto.

E) Explicar o código dos principais arquivos do projeto. Ex: No backend, de for python/dart/js, explicar os métodos e funcionalidades. No frontend, de for flutter/html/react, explicar os principais componentes.

	No backend o arquivo está com o código de speech recognition basicamente o mesmo que foi utilizado na aula, foi importado a biblioteca flask para utilizar o python em um "localhost" onde o nodejs tem a função de chamar este arquivo com o método getWords. Dentro do Node usando o axios conseguimos chamar a função getwords para exibir as palavras que foram reconhecidas pelo código python e transcrever para o front do projeto exibindo na view e poder manipular com ajax, basicamente JS, assim com a função createNewCard é onde está criando um novo card de um novo assunto na tela, adicionando um índice para cada assunto novo criado, populatedCurrentCard responsavel para exibir as palavras geradas pelo python dentro do card atual, populatePreviousCard caso troque o assunto que é mapeado pelo índice é o responsável por transcrever o texto. Com a função do axios  ele está aguardando as palavras do python server registradas para na getWords para serem exibidas nos cards, o método getInfo é o que garante se o back está funcionando corretamente e se estão se comunicando um com o outro.

F) Por fim, explicar o passo-a-passo para a execução do projeto.

Primeiramente deve ter todas a bibliotecas na máquina.

Após isso rodar o projeto python e manter o mesmo aberto, que irá funcionar como "back do back"

Rodar a aplicação node e acessar o localhost:5000/getwords

Na tela será exibido as regras de como utlizar o projeto para o usuário

Clicar no botão para falar, primeiramente falar a palavra "Assunto" e após o nome do assunto a ser adicionado.

Após isso falar o "lembrete" a ser adicionado no card, exemplo "Assunto academia, hoje vou treinar perna"

Para adicionar um novo card basta repetir o passo número 5 e será adicionado um novo card na tela.

Para alterar o assunto e voltar para um já criado, basta clicar no botão de falar e dizer o assunto anterior, e logo depois o que quer que seja adicionado no card anterior.

