A) Qual é a ideia geral do projeto?

O intuito do projeto foi criar uma prova de conceito que implementasse técnicas de IA, como speech to text, text to speech, comunicação com API da OpenAI para aprimoramento do texto gerado/inserido pelo usuário -- utilizando modelo davinci-002 -- e também permitir ao usuário clicar em um botão para ouvir o resultado final.
Em suma, as capacidades do projeto são: 
- Usuário pode gravar um áudio; 
- Esse áudio, gravado e armazenado em ´.mp3´ é convertido para ´.flac´ e, posterior enviado para o Google GCP onde é realizado o processo de speech to text; 
- Após receber o retorno, este é apresentado ao usuário; 
- O usuário possui um botão, com o qual pode solicitar uma versão aprimorada do texto; 
- Ao clicar nesse botão, o app se comunica com a API da OpenAI para obter o texto tratado / aprimorado / corrigido;
- Quando o app recebe um retorno da API OpenAI o texto gerado é apresentado ao usuário; 
- Em caso de falha nesse momento ou durante o processo de speech to texto um erro é exibido ao usuário; 
- Por fim, o usuário tem a opção de ouvir o texto retornado pela OpenAI, onde é utilizado o processo de speech to text (APIs nativas da plataforma - Android / iOS). 

B) Qual as tecnologias utilizadas, e porque?
Para front end: Flutter
Motivo: Framework muito versátil e rebusto que permite a construção de app em multiplas plataformas, i.e Android / iOS / Windows / MacOS / Linux etc. 
Além disso utiliza Dart para construção declarativa de interfaces, o que torna o processo de desenvolvimento muito mais dinâmico.  

Para speech to text: Google 
Motivo: Foi uma das únicas plataformas que permitiu a criação de um projeto e utilização gratuíta de recursos até certo limite (free tier).

Para aprimoramento/correção do texto: OpenAI - Modelo davinci-002
Motivo: Foi a proposta aceita para o projeto.

Para text to speech: APIs nativas do SO. 
Motivo: facilitade de uso. 

C) Qual a arquitetura do software? Quem é o back, o front, como se comunicam, etc

Tendo em vista a simplicidade do software, não foi implementado um padrão arquitetural complexo, haja vista que não se objetiva utilização comercial ou de modo outro senão uma prova de conceito.
Em suma, o projeto consiste de 6 arquivos e dois diretórios:

constants/
   routes.dart // arquivo estático com os nomes das rotas disponíveis na aplicação (1 rota apenas)
pages/ 
   demo.dart // página onde ocorrem as interações do usuário; comunicação com Google Cloud; Comunicação com OpenAI; 
main.dart // inicialização do projeto; definição das rotas nomeadas; definição da chave the API da OpenAI.   
route_generator.dart // definição das rotas nomeadas 

Vale ressaltar que, as chaves de API da OpenAI e Google GCP são armazenas / inseridas na aplicação via ´--dart-define´, ou seja, ficam disponíveis apenas em tempo de execução e devem ser definidas da inicialização do app, ex: ´flutter run --release --dart-define=KEY=VALUE´.

D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.

Conforme supracitado, tendo por base que esta seria apenas uma prova de conceito, não foram implementados padrões arquiteturais que viabilizem a publicação ou utilização desse app fora de um ambiente/escopo controlado. 

constants/
   routes.dart // arquivo estático com os nomes das rotas disponíveis na aplicação (1 rota apenas)
pages/ 
   demo.dart // página onde ocorrem as interações do usuário
main.dart // inicialização do projeto; definição das rotas nomeadas; definição da chave the API da OpenAI.   
route_generator.dart // definição das rotas nomeadas

E) Explicar o código dos principais arquivos do projeto. Ex: No backend, de for python/dart/js, explicar os métodos e funcionalidades. No frontend, de for flutter/html/react, explicar os principais componentes.

main.dart // aqui é inicializada a aplicação 'void main()' e definida a chave the api da OpenAI. 

route_generator.dart // arquivo simples para definição das rotas do app, nesse caso apenas uma. 

constants/ 
  routes.dart // arquivo estático contendo apenas o nome da rota criada em route_generador.dart 

pages/
  demo.dart
Métodos e responsabilidades: 
 
Método privado _checkStoragePermission_: Na inicializção do app verifica status das permissões de armazenamento e microfone, caso alguma não esteja com status de ´granted´ o app irá requisitar acesso as permissões, após sua execução irá executar o método _createEmptyFiles_.
Método privado _createEmptyFiles_: Responsável pela criação de dois arquivos vazios na pasta de cache do dispositivo, sendo eles ´audio.mp3´ e ´audio.flac´. 
Método privado _localPath_: Getter que retorna path do diretório de cache no SO;
Método privado _localFile_: Getter que retorna path arquivo ´.mp3´ no diretório de cache no SO;
Método privado _getAudioContent_: Realiza a conversão do arquivo ´.mp3´ para ´.flac´. 
Método privado _deleteFiles_: Ao clicar em "Gravar", os arquivos existentes no diretório de cache serão deletados (.mp3 e .flac); 

Botão ´Gravar/Parar´: utiliza uma simples expressão ternária para identificar estado atuado da aplicação -- gravando ou não -- para determinar o texto do botão e ação a ser executada no clique.
Caso precise gravar ou parar será utilizada uma instância previamente criada do plugin ´RecordMp3´.

Botão ´Converter para texto´: irá obter o path do arquivo ´.mp3´ gerado utilizando o método privado _localFile_, converter para ´.flac´ via método privado _getAudioContent_ e se comunicar com Google GCP para obter a o texto transcrito.
Ao obter o texto irá atualizar a tela do app apresentado o resultado. Em caso de erro irá apresentar uma mensagem com um erro.

Botão ´Obter versão do texto com aprimoramento´: Irá se comunicar com a API da OpenAI, utilizando o texto retornado via Google API como parâmetro. De mesmo modo, ou irá apresentar o resultado ou um erro.

F) Por fim, explicar o passo-a-passo para a execução do projeto.

- Realize o download do flutter em flutter.dev -- versão 3.3.7 -- e siga o passo a passo de instalação; 
- Crie uma chave de API no Google Cloud Platform para a API speech to text;
- Crie uma chave de API na OpenAI; 

Realize o clone do projeto via Github e acesse a branch BrunoSecchi+WilliamSecchi.
Abra um emulador Android ou conecte seu celular ao computador. 

Execute os seguintes comandos: 
- flutter pub get; 
- flutter run --dart-define=GOOGLE_API_KEY=SUA_CHAVE_GOOGLE_AQUI --dart-define=OPEN_AI_API_KEY=SUA_CHAVE_OPEN_AI_AQUI

:) 







