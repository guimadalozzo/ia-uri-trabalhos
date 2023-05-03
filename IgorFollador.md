### A) Qual é a ideia geral do projeto?
R: A ideia eh criar um aplicativo capaz de auxiliar o usuario a criar e gerenciar notas transcritas atraves de audios. O algoritmo deve ser capaz de transcrever audio em texto e categoriar o texto entre algumas categorias (Trabalho, Casa, Estudo e Ideias).

### B) Qual as tecnologias utilizadas, e porque?
R: As tecnologias utilizadas foram Node.js e React, ambas utilizam a linguagem Javascript que foi o possibilitador para que entregassemos a aplicacao no prazo, visto que sao techs de amplo conhecimento da dupla de desenvolvimento e possuem otimas comundiades para retirada de duvidas, as quais possuiam bibliotecas como a `natural`, que foi a responsavel por treinar o algoritmo de deteccao de categorias. Juntamente com o ChatGPT que foi a IA generativa de texto responsavel por gerar os dados q utilizamos para treinar a biblioteca citada acima.

### C) Qual a arquitetura do software? Quem é o back, o front, como se comunicam, etc.
R: A arquitetura utilizada foi a de de monolito para ambas as partes. Tanto o back quanto o front possuem servidores dedicados usando o Express. O backend eh uma API REST responsavel por toda a logica de fluxo dos dados, autenticacao e comunicacao com o banco de dados MySQL. O frontend foi feito em React e por mais q ele possua um servidor dedicada para entrega das telas, o mesmo consome todas suas funcionalides de endpoints disponibilizados pela API REST.

### D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.
R: Dentro da API existe o diretorio src q contem todo o projeto da mesma, la ele possui um diretorio de rotas q possui de forma subdividida a rota de cada controlador, (autenticacao e conversas), e possui um arquivo index q mescla as duas rotas, tambem existe um arquivo exclusivo de rotas publicas (q dispensam autenticacao). Temos tambem a pasta controllers que possuem todos os controladores da aplicacao, cada um com suas funcoes de CRUD no banco. A pasta services que possuem servicos que sao consumidos pelas funcoes dos controladores e eh dentro de um arquivo do services q possui a funcao/lib responsavel por categoriar as conversas. Tambem existem as pastas de models, migrations e seeders q servem para representacao das tabelas do banco, realizacao de alteracoes e mockups na base de dados, respectivamente.
Dentro do frontend existe tambem uma pasta src que contem todos os assets (estilos, imagens e afins) utilizados pela aplicacao, a pasta components q possui os componentes criados pra montagem das telas, a pasta pages que possui dentro dela de forma dividida em subpastas conforme cada tela desenvolvida na aplicacao e a pasta services que contem a configuracao base utilizada pela lib Axios para configuracao da URL base da API. Fora da pasta src existe tambem uma pasta nomeade de public que contem arquivos base do proprio React.

### E) Explicar o código dos principais arquivos do projeto. Ex: No backend, de for python/dart/js, explicar os métodos e funcionalidades. No frontend, de for flutter/html/react, explicar os principais componentes.
R: Backend: O principal trecho de codigo encontrasse no metodo criado no arquivo `audioNotes-nodeApi/src/services/ConversationService.js`. Nesta funcao existe a criacao dos Classifiers que sao as nossas categorias possiveis de conversas, ali sao definidas quais sao as categorias base e seus sinonimos, e logo abaixo o algoritmo eh treinado com base em um json montado pelo CHAT GPT com frases e suas respectivas categorias. Apos o treinamento o texto que queremos classificar eh submetido ao algoritmo e nos eh retornada a categoria classificada para aquele texto. Abaixo desta funcao existe outra q apenas cria a estrutura de dados para salvar na model da conversa realizando a troca do nome da categoria pelo seu respectivo ID do banco de dados.
No frontend seu principal componente se encontra em `audioNotes-frontend/src/pages/Home/index.js` que eh o componente resposavel pela transcricao do audio, neste componente existe a importacao da lib `react-speech-recognition` que eh a lib que realiza de fato a transcricao de audios, tambem eh neste arquivo na linha 22 que eh definido o array de comandos validos pela nossa IA.

### F) Por fim, explicar o passo-a-passo para a execução do projeto.
R:
#### Backend:
 - Entre no diretorio `audioNotes-nodeApi`
 - Execute o comando `npm i` para instalar as dependencias
 - Execute no terminal `cp .env.example .env` e preencha com credenciais validas do seu banco de dados MySQL
 - Execute `npx sequelize db:create` para criacao da base da dados
 - Execute `npx sequelize db:migrate` para criar as tabelas da base de dados
 - (Passo opcional) Execute `npx sequelize db:seed:all` para popular o banco
 - Execute o comando `npm run start` para execucao normal ou `npm run dev` para execucao com hot reload

#### Frontend:
 - Entre no diretorio `audioNotes-frontend`
 - Execute o comando `npm i` para instalacao das dependencias
 - Execute o comando `npm start` para subir o servidor

Com os dois servers em funcionamento abra o navegador em `https://localhost:${portaDefinida}`
