# A) Qual é a ideia geral do projeto?
### - A ideia geral se remete a criação de uma API em Python para agendamentos de compromissos/eventos e consulta de compromissos do mês linkadas com a API externa do Google Agenda/Calendar, assim facilitando tais ações.

# B) Qual as tecnologias utilizadas, e porque?
* **Python:** Linguagem de programação utilizada para a criação da API back-end e pré-requisito para a utilização do Flask;
* **Flask:** Falando no Flask, ele foi utilizado para a criação do Front-End em html, css e javascript utilizando como principal meio de função, o Python. Ele criou toda a frente do projeto e fez com que possa ser feito a API e a utilização da API do Google Agenda;
* **Google Cloud:** Utilizado principalmente para a utilização da API externa do Google Agenda. A forma com que é moldado fez com que o projeto fique de forma organizada e coerente. O uso de credenciais e tokens foi o principal papel para que tudo ocorra como o esperado;
* **SpeechRecognition:** Principal pacote Python utilizado no projeto, sendo capaz criar funções em que a IA fala o compromisso agendado após o agendamento e também na consulta de compromissos do mês;
* **Json:** A manipulação de JSON se mostrou essencial para o projeto. Após a criação de um QAuth2.0 no Google Cloud, foi possível manipular de diversas formas no projeto;
* **HTML5:** Linguagem de marcação utilizada para a criação da estrutura da frente do projeto com a utilização de tags;
* **CSS3:** Linguagem de folha de estilo usada para a manipulação de estilo em folha para deixar o html mais intuitivo com tags como animation e border para manipulaçao estrutural do html.

# C) Qual a arquitetura do software? Quem é o back, o front, como se comunicam, etc
* **Back-end:** Python;
* **Front-end:** HTML5, CSS3, FlaskIcon;
* **Como se comunicam:** Começando pelos fatores A e B, Python e Front-End, para que a conexão seja bem feita é preciso do fator C, Flask, que no projeto em questão, serve como uma âncora entre o fator A e B, podendo assim fazer um projeto HTML e etc, com o Python sendo um back-end. Obs.: o Html está empregado como um fator imóvel pois não interfere na conexão assim podendo ser feita usando react, node e etc... O Python não consegue se comunicar diretamente com o HTML e manter-se estável, aí que entra o Flask podendo conciliar os dois. Dentro do HTML, é utilizado tags "forms" com recursos de action POST e GET.

# D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.
1. **src:** utilizado para guardar os recursos Front e Back do projeto em arquitetura de pastas, como static, templates e arquivos back como app.py, credentials.json e token.json;
* **static:** diretório utilizado para armazenamento das pastas de css;
* **css:** Armazenamento das folhas de estilo CSS3;
* **templates:** diretório utilizado para armazenamento dos HTML;
* **__init.py:** arquivo criado para manutenção pyton após execução do mesmo.
* **app.py**: arquivo principal do projeto, guardando todas as funcionalidades do projeto, com uso de python.

# E) Explicar o código dos principais arquivos do projeto. Ex: No backend, se for python/dart/js, explicar métodos e funcionalidades. No frontend, se for flutter/htmkl/react, explicar os principais componentes.
* Back-end: app.py: métodos de utilização speechRecognition que foi usado para mais de uma função como def agendar e def compromissos e serve para a utilizacação de uma IA para reconhecimento de voz ou como é feito nesse projeto, textToSpeech, para a utilizacação de uma leitura por IA dos compromissos agendados e dos compromissos do mês. def agendar: função presente no código que é usada para a criação do agenamento na aplicação e Google Agenda do usuário logado pelo token.json e credentials.json. def compromissos: função que tem sua utilização em obter a visualização dos compromissos do mês em uma rota chamada "/compromissos". def obter_credenciais: a utilizacação dessa função é de extrema importância ao usuário pois faz a leitura das credenciais de acesso do usuário antes registrado no QAuth2.0 do GoogleCloud. credentials.json: arquivo a parte do app.py, utilizado para leitura da credencial na função obter_credenciais, presente no arquivo app.py.
* Front-end: HTML5: templates: Os templates organizados dentro da pasta src, guardando os htmls, permitindo melhor organização. Os principais componentes são a utilização de forms com actions POST e GET para comunicação direta e indireta com o back-end, e tags especificas para a manipulação css posterios. CSS3: Folhas de estilo com principais tags sendo animation, display(flex e dynamic).

# F) Por fim, explicar o passo-a-passo para a execução do projeto.
1. Baixar/Clonar o projeto do Github: LeonardoFCorrea com nome de Text-to-Speech-GoogleCalendar-API;
2. Requisito: Python;
3. Ativar o venv usando activate venv na pasta do projeto;
4. Instalar todos os modulos presentes no arquivo app.py(src/);
5. entrar na pasta src/;
6. Executar: python app.py;