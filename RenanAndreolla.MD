## Atividade final do Trabalho 1.

#A) Qual é a ideia geral do projeto?
  > A ideia inicial do projeto é a criação de um programa que identifique a voz do usuário para a criação de um bloco de notas dinâmico, onde o usuário pode adicionar vários assuntos e navegar entre eles utilizando a voz.

#B) Qual as tecnologias utilizadas, e porque?
  > Em um geral, foram utilizadas as tecnologias: HTML, CSS, Javascript, Node.js, Ajax, jQuery e Python.
  > O HTML e CSS foram utilizados para a criação das telas e estilização das mesmas.
  > O Node.js foi utilizado para fazer o backend da aplicação WEB o qual integra com uma API criada com Pyhton. A escolha do Node.js se deve a fácil utilização, por ser um ambiente WEB e pela minha facilidade em sua utilização.
  > O Python foi utilizado para fazer o servidor que retorna as informações que o usuário fala quando a aplicação está rodando. Sua escolha se deve por causa das aulas e por ter o código parcialmente pronto, fornecido pelo professor.
  > O Ajax fiu utilizado para fazer a chamada da rota de comunicação com API através do arquivo JS da camada de front.
  > O jQuery foi utilizado para facilitar a captura de elementos HTML.
  > O Javascript foi utilizado pois é a linguagem de programação que o navegador interpreta e a qual o Node.js utiliza, além da minha facilidade em sua utilização.

#C) Qual a arquitetura do software?
  > A aplicação WEB é formada por um HTML, um CSS e Javascript, que funcionam graças a um template engine chamado Nunjucks, formando o FRONTEND. O BACKEND da aplicação WEB roda em Node.js, o qual faz a comunicação entre a aplicação WEB e o servidor Pyhton.
  > O servidor Pyhton foi criado com flask e ele é chamado sempre que o usuário chama um gatilho ao apertar o botão de "Record", com isso o código Pyhton roda e a IA captura a voz do usuário.
  > A comunicação da aplicação WEB e o servidor Pyhton funciona da seguinte forma: Dentro do HTML existe um botão atrelado a um evento de "onclick", quando esse evento é disparado executa uma função chamada "getTexts", dentro do javascript da camada de front. Após isso, utilizando AJAX, chama-se uma rota chamada de "getInfo" que fica no BACKEND Node.js que por sua vez faz um request utilizando a biblioteca NPM do Axios para chamar o servidor Python(que roda localhost) através do endpoint "http://localhost:5000/getWords". Por fim, a rota "getWords" do servidor é chamada, o arquivo roda, interpreta as falas do usuário e retorna o texto para ser exibido.

#D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.
  > Dentro da raíz do projeto, temos uma pasta "flask-server", uma pasta "node" e um arquivo .gitignore.
  > .gitignore:
    > Nesse arquivo temos as pastas que não precisam subir para o repositório GIT.
  
  > flask-server:
    > A pasta "flask-server" é onde fica o arquivo "server.py", responsável por captar a voz do usuário quando sua rota é chamada e retornar informações para a aplicação WEB.
  
  > node:
    > A pasta "node" é onde fica toda a aplicação WEB, dentro dela temos o arquivo "index.js" que é o principal e primeiro arquivo a ser executado. 
    > O arquivo "package.json" é o responsável pelas configurações de projeto assim como as bibliotecas NPM utilizadas.
    > A pasta "views" é onde ficam todos os arquivos HTML responsáveis pelas telas do projeto. Obs: Dentro dela existe uma pasta "layouts" que é onde fica o arquivo padrão configurado com o Nunjucks.
    > A pasta "public" é onde ficam os arquivos públicos, ou seja, o javascript da aplicação e os arquivos CSS responsáveis pela estilização.
    > A pasta "images" é onde ficam as imagens utilizadas no projeto.

#E) Explicar o código dos principais arquivos do projeto. Ex:
  > Nesse projeto, podemos evidenciar 3 arquivos principais que fazem o sistema funcionar, que são eles:
    > "./node/index.js": Esse arquivo é o principal da aplicação WEB, ele cria o servidor Node e possui a rota de comunicação com o servidor Python.  
    > "./node/public/js/index.js": Esse arquivo é o que gera todas as informações em tela. Esse arquivo recebe informações do BACKEND Node e cria todos os cards com os textos em tela através de Javascript puro + Jquery. Nele também ficam as lógicas de troca de assuntos e todos os fluxos possíveis do usuário, ou seja, tudo que aparece em tela durante o funcionamento é criado com javascript puro + jQuery.
    > "./flask-server/server.py": Esse é o arquivo que contém o código do servidor Python, o qual possui uma rota GET "/getWords" que é chamada pelo Node. Esse código captura a voz do usuário através do microfone e retorna o que foi dito para o BACKEND Node e por sua vez para o front, onde é exibido.

#F) Por fim, explicar o passo-a-passo para a execução do projeto.
  > Para executar o projeto, é necessário realizar o download do Node.js e download do Pyhton, basicamente.
  > Após fazer o download do Node, é necessário instalar suas dependências. Abra um terminal de comando dentro da pasta "node" basta executar o comando $npm install para que as dependências NPM sejam instaladas.
  > Após isso, no mesmo terminal, basta executar o comando $npm start para rodar o projeto. Para visualizar a tela abra seu navegador em "localhost:3000".
  > Após isso, é necessário configurar o flask. Abra um outro terminal dentro da pasta "flask-server" (existem 2 comandos para rodar mas não lembro).
  > Depois de rodar esses comandos, basta excutar o comando $python server.py para que o server python inicialize.
  > Por fim, basta clicar em "Record" na tela inicial da aplicação e utilizá-la.
