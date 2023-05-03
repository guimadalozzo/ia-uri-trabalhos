# Atividade final do Trabalho 1.

A) Qual é a ideia geral do projeto?

> A ideia geral do projeto produzido é uma ferramenta de construção de exercícios de inglês, em que é apresentada uma frase incompleta e quatro opções de alternativas para resposta, onde somente uma é a correta. Para fazer a detecção da resposta, este projeto usa Speech to Text (Pronuncia para Texto). 

> Dessa forma, a resposta deve ser pronunciada em voz alta usando o microfone do computador, e a ferramenta mostrará o status de resposta (Acertou, Errou, Falhou em identificar). Se acertar, o jogador ganha 1 ponto, se errar não ganha nenhum ponto, e se houver falha na identificação, o jogador deverá repetir a palavra que acha certa novamente. Após 5 frases, o jogo termina e o sistema mostra a pontuação final do jogador (Entre 0/5 e 5/5 acertos).

B) Qual as tecnologias utilizadas, e porque?

> Linguagem Python como API Backend do sistema. Com a utilização da biblioteca Flask, é possível criar rotas HTTP para trafegar dados com outras partes do sistema. A utilização de bibliotecas como a SpeechRecognition foram usadas para fazer detecção de texto dentro de arquivos de áudio. E com a biblioteca NLTK foi coletado sinônimos e antônimos da palavra certa. A utilização do python foi necessária para conseguir usufruir dessas bibliotecas citadas acima.

> Framework Vue.JS para produzir um front-end bonito e fácil de manusear. Com ele foi construído toda a base HTML do sistema e apresentar os dados provenientes da API python.

> Banco de dados Postgres foi necessário para armazenar todas as frases e também as alternativas corretas. Foi hospedado em um serviço de cloud chamado ElephantSQL.

C) Qual a arquitetura do software?
   Quem é o back, o front, como se comunicam, etc

> O back-end se resume em um arquivo python localizado dentro de ./src/python/main.py. Neste arquivo há duas rotas de API: /api/question e /api/recognition. A primeira citada não recebe nenhum parâmetro e retorna um json com um exercício aleatório junto das opções disponíveis. A rota de recognition serve para receber como parâmetro um arquivo .webm (arquivo de áudio) e retornar um json com possíveis textos que se aproximam do áudio passado.

> O front-end é basicamente toda a estrutura externa, o arquivo que mais possui comunicações com o back-end fica dentro de ./src/components/WordSpeech.vue. Seu papel é chamar a rota de API python via Ajax, onde após as opções serem retornadas, sua informação é convertida em uma tela apresentável para o usuário. Ele vai chamar a API duas vezes: uma para construir a questão e gerar as alternativas, e a segunda para fazer a detecção do texto. Nesta última, é passado para a API um arquivo .webm que foi construído usando uma gravação em tempo real produzida no front-end com a biblioteca RecordRTC.

D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.

> ./public -> Pasta padrão que foi criada com um novo projeto vue. Não foi utilizada.

> ./src -> Pasta onde contém toda a lógica necessária da aplicação. Nela há os arquivos iniciais, o front-end (arquivos .js para construção do template) e o back-end

> ./src/assets -> Pasta necessária para armazenadas imagem. A única imagem realmente utilizada neste projeto foi a de um microfone.

> ./src/components -> Pasta para armazenar os componentes do Vue. Por ser um projeto menor, foi utilizado somente um componente, que é o WordSpeech.vue. Seu conteúdo é o template padrão das questões e alternativas. Nesse arquivo também fica a lógica de identificação da palavra correta.

> ./src/python -> Pasta para armazenar o arquivo main.py que contém o back-end. Foi colocado dentro do ./src para uma melhor organização interna do grupo. Além do arquivo python, há um arquivo .txt onde contém 10000 palavras em inglês mais comuns. Esse arquivo auxilia para gerar alternativas mais comuns na API

E) Explicar o código dos principais arquivos do projeto. Ex:
   No backend, de for python/dart/js, explicar os métodos e funcionalidades.
   No frontend, de for flutter/html/react, explicar os principais componentes.

> Back-end com python: Dentro do arquivo python é feita a conexão com o banco de dados, a construção das duas rotas de API citadas anteriormente e também uma função auxiliar para construir alternativas mais simples para as questões.

> Front-end com Vue.Js: O arquivo main.js contém um javascript global. Porém foi apenas utilizado para carregar o arquivo App.vue. O arquivo App.vue é o arquivo principal do projeto. Ele carrega três opções de template: Tela de bem-vindo, o componente do jogo e a tela de parabéns. O componente do jogo se encontra dentro de ./src/components. Com lógicas simples de if-else foi possível trocar o template atual sem que houvesse a troca de rota no navegador.

F) Por fim, explicar o passo-a-passo para a execução do projeto.

> Para iniciar, os servidores, digita-se 'npm run dev' (Vue) e 'python ./src/python/main.py' (API python).

> Após aberto os servidores do vue.js e do python, o projeto inicialmente executa no localhost com o ./src/App.vue em que carrega a tela de bem-vindo. Na detecção deste botão, o template atual é trocado por outro que é carregado dentro de ./src/components/WordSpeech.vue. A primeira coisa que o componente faz é construir um layout padrão e depois chamar via AJAX a rota de API /api/question. Nesse momento, o back-end python recebe a requisição e retorna um json com uma frase e quatro alternativas. Com o auxílio da ferramenta de front-end esses dados são facilmente apresentados na tela dentro do HTML. Além do vue, foi utilizado jquery para uma mais rápida produção de código.

> Para criar as alternativas, a API python quando chamada executa uma query postgres utilizando RANDOM() para selecionar uma frase aleatória e a alternativa correta. Esta alternativa é coletada e é submetida à biblioteca NLTK para calcular seus sinonimos e antônimos. A aplicação coleta as palavras do arquivo txt e descarta os sinonimos e antonimos da lista. Dessa forma, alternativas semelhantes que possam comprometer a resposta correta não serão apresentados.

> Quando o botão do microfone é clicado, automaticamente dentro do arquivo vue é chamada a biblioteca RecordRTC que constrói um arquivo .webm com o que está sendo gravado naquele momento. Para ficar mais dinâmico, há um tempo limite de 3 segundos para a gravação parar. É um tempo bastante curto pois apenas uma palavra deve ser dita para o microfone. Com a confirmação do áudio, este arquivo .webm fica armazenado dentro do projeto ./src temporiariamente. Neste momento é chamada a rota /api/recognition do python. Ele identifica o arquivo .webm e faz o reconhecimento.

> O reconhecimento é feito dentro do arquivo python, que utiliza a biblioteca SpeechRecognition. Para analisar o arquivo .webm, foi ativado o idioma inglês e ao mesmo tempo o atributo show_all como True. Esse atributo serve para devolver várias alternativas de qual palavra foi pronunciada, pois no idioma inglês muitas vezes acontece de duas palavras terem pronuncias muito parecidas. Se esse atributo fica desativado, a identificação fica bastante precária e na maioria das vezes o sistema não funciona. Com todas as alternativas prontas, a API retorna o JSON com as opções.

> O front-end recebe as alternativas e faz as comparações com a palavra correta. Caso identifique que a palavra é correta e está nas alternativas, é somado na variavel score 1 ponto. Caso identifique que a palavra é errada e está nas alternativas, o score não sofre impacto. Caso não identifique a palavra ou note que a palavra não está na lista de alternativas, o sistema pede novamente para pronunciar a palavra.

> Como a API devolve várias alternativas de palavras que foram pronunciadas, o front-end analisa uma por uma, sempre priorizando caso tenha encontrado uma palavra correta.

> O score (pontos) e o counter (índice da frase atual) ficam no arquivo principal App.vue. Quando o counter for > 5, automaticamente o sistema coleta o score e mostra na tela o resultado para o usuário.

