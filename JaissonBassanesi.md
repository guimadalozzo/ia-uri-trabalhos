## Jaisson Bassanesi

#<h3>O que é?</h3>

O Audio Notes foi criado para funcionar como um site para anotar ideias por áudio, para que o usuário não precise digitar e possa fazer anotações de forma rápida.
O Audio Notes também realiza a categorização automatica das anotações de acordo com a escrita da mesma.
Por exemplo ideias para novos projetos, ideias para reformas, anotações de afazeres, lista de compras, entre outros.
<br>
<br>


#<h3>Stacks</h3>

- <strong>Front-end:</strong>
<br>
Para o front-end foi utilizado o React como biblioteca prinpipal com JS como linguagem de programação, além de outras liguagens de estilo e marcação como CSS e HTML.
Além disso, o core do 'Speech to Text' foi feito com a biblioteca "react-speech-recognition", que é responsável por identificar comandos de parada, para parar de ouvir o usuário e de transformar o áudio em texto.
Optando por essa stack front-end pelo vasto conteúdo online, conhecimento prévio dos desenvolvedores, por serem simples de utilizar e atenderem os requisitos.

<br>

- <strong>Back-end:</strong>
<br>
No back-end utilizou-se o Node.js com REST e sequelize para a construção da API que fornece o necessário para o front-end.
Optando por essa stack back-end pelo vasto conteúdo online, conhecimento prévio dos desenvolvedores, por serem simples de utilizar e atenderem o desejado.

<br>
<br>


#<h3>Arquitetura</h3>

O front-end como já citado, foi desenvolvido em react.js, sendo assim, de simples comunicação com APIs utilizando o axios (uma lib muito utilizada para comunicação no react).
A API é responsável por manter usuários, categorias, mensagens e conversas. Onde uma conversa possui 1 ou mais mensagens e uma única categoria.
Além disso o back-end faz a categorização da conversa, considerando o conteúdo da primeira mensagem da conversa.
Retornando assim todos os dados necessários para o front-end quando o mesmo requisita.

<br>
<br>


#<h3>Indo mais a fundo - Front-end</h3>

O projeto em React foi criado utilizando o ```create-react-app```, sendo assim, boa parte da disposição de diretórios foi criada ao iniciar o projeto:
- ```public```: - Contem apenas imagens do projeto inicial do react e um index.html da mesma finalidade;
- ```src```: - É o core da aplicação front-end, onde se encontram os arquivos principais do projeto, principalmente o App.js que é o primeiro arquivo a carregar ao executar a aplicação e é responsável pelas rotas publicas e privadas;
	- ```assets```: Armazenar arquivos de imagens e ícones;
	- ```components```: Onde ficam os componentes da aplicação, sendo neste caso Header e Speech, está separação é interessante em casos que os mesmos componentes são utilizados em páginas diferentes;
	- ```pages```: Contém as três páginas do projeto, cada página fica em uma rota diferente;
	- ```services```: Contém a configuração da api, para facilitar a chamada dos endpoints de qualquer página ou componente.
<br>
#<h3>Indo mais a fundo - Back-end</h3>

- ```src```: - Contém os diretórios principais e demais arquivos de configuração de projeto;
	- ```config```: Diretório responsável pela configuração do banco de dados;
	- ```controllers```: Basicamente mapea os endpoints e protocolos dos mesmos para que o front-end consiga buscar, alterar e adicionar novos dados;
	- ```migrations```: Mapea os campos das tabelas do banco de dados e tipagem dos mesmos;
	- ```models```: Responsável pela modelagem das tabelas do banco;
	- ```routes```: Mapea as rotas publicas e privadas da API, redirecionando cada chamada para o controller respectivo;
	- ```seeders```: Cria alguns registros no banco para testes de desenvolvimento;
	- ```services```: Contém arquivos uteis, como por exemplo a IA responsável pela categorização das conversas e outro arquivo para padronização de datas com o timezone correto;

<br>
<br>


#<h3>Arquivos principais</h3>

- <strong>Front-end:</strong>
	- ```App.js```: Arquivo que inicia e define as rotas/URLs do projeto, chamando os demais arquivos das pages quando necessário;
	- ```Speech``` > ```index.js```: Responsável pela lógica do Speech, transforma o áudio em texto;
<br>
- <strong>Back-end:</strong>
	- ```AuthenticationController.js```: Responsável pela autenticação do usuário;
	- ```ConversationController.js```: Responsável por manter as conversas;
	- ```UserController.js```: Responsável por manter os dados do usuário;
<br>


#<h3>Execução</h3>

Seguimos o seguinte fluxo para a criação deste projeto:
- Mapeamos as funcionalidades;
- Mapeamos os endpoints necessários;
- Definimos o layout;
- Dividimos as tarefas, em front-end e back-end;
- Iniciamos o desenvolvimento;
- Alinhamos funcionalidades e corrigimos bugs;
- Apresentação do trabalho.








