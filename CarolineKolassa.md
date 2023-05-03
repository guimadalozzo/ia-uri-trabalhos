### A) Ideia geral do projeto 
A ideia geral do projeto é criar um produto integrado com a API do mercado livre que a partir do item falado traz as informações dos 5 primeiros resultados, como descritivo técnico, preço e imagens.

### B) As tecnologias e o motivo de suas utilizações são: 
- Linguagem Python: Por termos uma base do código de leitura de voz feita com ela e ser simplificada; 
- Framework Flask: Por ser de simples utilização e implementação;
- SpeechRecognition: Requisito do trabalho
- API Mercado Livre: API escolhida como requisito do trabalho

### C) Arquitetura do software
O backend é feito em python utilizando o framework flask e algumas blibiotecas como o request para enviar requisições http para a API online e gratuita do mercado livre. Além disso há uma threading para que o nosso código exiba as informações na tela enquanto os resultados são lidos. O frontend é feito em html e css e ficam em  diretórios chamados templates e static, respectivamente.  

### D) Os diretórios do projeto são:
- src -> Diretório principal, dentro deles há outros diretórios. 
- src/templates -> Neste diretório está localizado todo o esqueleto da página visualizada ao iniciar o ambiente virtual e todo o esqueleto da página renderizada após a escuta do produto falado pelo usuário.
- static/css -> css do botão de busca 
- app.py -> É um ARQUIVO que contém toda a lógica do projeto, como a função de escutar a fala do usuário, processa-lá e consultá-la na api do mercado livre.  
- venv -> Arquivo usuado para criação do ambiente virtual. 

### E) Explicação do código
No arquivo app.py, temos em primeiro lugar as importações das bibliotecas, após isso, a função SpeakText é definida para reconhecer comandos de interrupção por parte do usuário. Uma rota padrão é definida que iniciará pelo nosso arquivo index.html.
Outra rota é criada ('/reconhecimento_de_voz') e o processo de leitura de aúdio inicia. Em nosso código, utilizamos o metodo de reconhecimento de fala do google para extrair o texto dito. O parametro de texto é enviado ao mercado livre que nos retorna um json com os dados solicitados.  Os dados são exibidos na tela e falados. 

### F)   Passo-a-passo para a execução do projeto:
1- Clonar o repositório
2- Criar o ambiente virtual utilizando: python3 -m venv ./venv
3- Ativar o ambiente virtual: .\venv\Scripts\activate venv
4- Instalar as bibliotecas necessárias: 
- pip install flask
- pip install request 
- pip install wheel
- pip install pyaudio
- pip install speechrecognition
- pip install pyttsx3

5- Após isso, executar o arquivo app.py da seguinte maneira: python app.py 
6- Acessar a URL http://localhost:5000