A) Ideia do projeto é construir um app Capaz de interpretar por meio da voz a palavra correta em ingles, ou seja, é disponibilizado uma frase com alternativas
onde uma delas é a correta, o usuario precisa falar no microfone a palavra correta, o app tem 5 perguntas onde ao final é mostrado o placar de acertos ou erros

B) VUE, HTML, CSS e Python, ElephantSQL: VUE é o front da aplicacao juntamente com html e css. É o front que vê se a sentença e armazena as variaveis, inicia ou para a gravação mostra
para o usuario se está correta ou errada a resposta, python foi usada como backend no projeto é ele o responsavel por pegar a API, faz a conexão com o banco e fazer
o tratamento do Banco de dados, alem de pegar as frases no banco e gerar as frases de modo aleatorio, o EephantSQL foi usado como banco de dados

C) Como foi falado o python é o backend ele faz o reconhecimento de voz do usuario, pega as 10000 palavras disponiveis e usa uma api para gerar os sinonimos, gera as
palavras e as questoes com as alternativas, usa o google speech para reconhecer o audio e conecta tudo ao frontend, por sua vez o vue biblioteca do JS faz a parte de pegar
todas essas informacoes e fazer o tratamento de erros ou acertos do audio em relacao as frases ditas

D) Na pasta /public é a pasta de configuração criada pelo vue.
/src/assets temos a pasta de img responsavel pelas imagens do projeto. 
/src/components temos o Front do projeto o arquivo WordSpeech.vue ele responsavel por fazer a logica do front
/src/App.vue é o arquivo de front onde mostra o inicio do projeto e o fim das questoes tbm
/src/python/google-10000-english.txt temos uma arquivo com 10000 mil palavras em ingles para ser usado como sinonimos
/src/python/main.py temos toda logica de backend do python alem da configuracao do banco de dados

E) O arquivo App.vue mostra o pagina inicial do projeto e o fim dele onde aparece o placar de acertos alem de um gif de palmas
   o arquivo WordSpeech.vue é o front do projeto onde:
   ele pega as palavras corretas e gera um score mostrando na tela com toggleRecording nesse é criado uma funcao onde se inicia ou para a gravação começa a gravar após 16000 milissegundos e para a gravação após 30000 milissegundos,
além disso ela grava a gravação e envia um ajax para o arquivo ser enviado ao servidor logo em seguida no codigo ele faz a verificação de cada uma das palavras na frase 
e diz se ela é valida ou não, se o valor de "data" é nulo a palavra nao existe, se o valor de "data" for "false" a palavra existe mas não é a correta, se o valor de "data"
for "true" a palavra é a certa, se o valor for diferente de "true" é exibido uma mensagem dizendo que a palavra é incorrerta.

  o arquivo main.py:
é a parte back do projeto onde primeiramente se faz a configuração do banco de dados no ElephantSQL, apos inicia o reconhecedor da fala, conecta o banco de dados,
após o resultado do pesquisa é pego e guardado na variavel a palavra certa, generate_options gera-se as 4 palavras aleatorias, após ele gera a perguntas, cria-se uma rota para receber o audio
salva o arquivo e faz o reconhecimento da fala, e manda devolta para o JS, após def make_speech_recognition(): ele le o audio do arquivo e usa o google spech para
reconhecer a fala, caso nao reconheça a fala ele gera erro, def generate_options(word):ele retorna um array conjunto de 4 palavras (a certa e outras três aleatórias),
synonyms.remove(word) remove a palavra certa dos sinonimos, após remover a palavra certa o arquivo é encaminhado ao diretorio atual. lê-se as 10000 palavras comuns do
google, encontra 3 palavras aleatórias que não são sinônimos e ignora as palavras menos frequentes, random_words.insert(random.randint(0, 2), word) adiciona a palavra em um array fixo,
random.shuffle(random_words) deixa as palavras em uma liasta aleatoria, e retorna ao JS

F) passo a passo para executar o projeto: ir no github https://github.com/rodrigomuntini/wordspeech-client/tree/master clicar em copiar o codigo, dar git clone em um
diretorio do PC, após executar um editor de texto recomenda-se o visual code, posteriormente abrir a pasta do projeto ir non terminal do visual code e executar npm install
para instalar as dependencias necessarias, apos executar npm run dev, abra o localhost para dar inicio ao projeto localmente na WEB, conectar um microfone ao Computador para a aplicação conseguir
identificar a resposta fornecida, pronto só usar a aplicação.
   
   
