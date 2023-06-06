# ia-uri-trabalhos

A) A ideia geral do projeto é criar uma aplicação que permite ao usuário buscar informações sobre Pokémons. O usuário pode inserir o nome do Pokémon em um campo de texto ou pode falar o nome do Pokémon usando o reconhecimento de fala. A aplicação faz uma chamada à PokeAPI para obter os dados do Pokémon e exibe as informações na interface gráfica.

B) As principais tecnologias utilizadas são:

Python: A linguagem de programação utilizada para implementar a lógica do projeto.
Requests: Uma biblioteca em Python utilizada para fazer requisições HTTP.
SpeechRecognition: Uma biblioteca em Python utilizada para realizar o reconhecimento de fala.
Tkinter: Uma biblioteca gráfica em Python utilizada para criar a interface do usuário.
Essas tecnologias foram escolhidas por sua facilidade de uso, ampla documentação e pela capacidade de realizar as tarefas necessárias para o projeto, como fazer requisições HTTP e lidar com a entrada de áudio.

C) A arquitetura do software segue um padrão simples de back-end e front-end. O back-end é representado pelo código Python que lida com a lógica de buscar informações dos Pokémons e fazer requisições à PokeAPI. O front-end é representado pela interface gráfica criada com a biblioteca Tkinter, que permite a interação do usuário com a aplicação.

O back-end e o front-end se comunicam através de eventos. Quando o usuário clica no botão "Falar" ou "Pesquisar", são chamadas as respectivas funções no código Python que realizam as ações correspondentes. O resultado da busca é atualizado na interface gráfica, exibindo as informações do Pokémon pesquisado.

D) Não há diretórios específicos mencionados no código. O código é apresentado em um arquivo único contendo tanto a lógica do projeto quanto a criação da interface gráfica.

E) O código fornecido apresenta uma estrutura sequencial, com a definição das funções e a criação da interface gráfica em seguida.

A função buscarPokemonPorTexto é responsável por obter o nome do Pokémon digitado pelo usuário no campo de texto e chamar a função chamarAPI para buscar as informações do Pokémon.
A função buscarPokemonPorVoz utiliza a biblioteca SpeechRecognition para reconhecer o nome do Pokémon falado pelo usuário. Ela exibe uma mensagem na interface gráfica para instruir o usuário a falar o nome do Pokémon e, em seguida, utiliza a API de reconhecimento de fala do Google para transcrever o áudio. Se o reconhecimento for bem-sucedido, o nome do Pokémon é passado para a função chamarAPI.
A função chamarAPI faz uma requisição à PokeAPI usando o nome do Pokémon fornecido. Se a resposta da API for bem-sucedida (código de status 200), as informações do Pokémon são formatadas em uma string e exibidas na interface gráfica. Caso contrário, é exibida uma mensagem informando que o Pokémon não foi encontrado.
A interface gráfica é criada utilizando a biblioteca Tkinter. Ela consiste em uma janela principal com uma descrição, um campo de texto para digitar o nome do Pokémon, dois botões (um para busca por voz e outro para busca por texto) e um rótulo para exibir as
