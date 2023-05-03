1- Baixar a sua branch localmente, por ex: GuilhermeMadalozzo+FulanoDeTal+CiclanoDaSilva

2- Deverá escrever em um arquivo de markdown (nome.md por ex: GuilhermeMadalozzo.md) e responder, neste arquivo, as seguintes questões:


A) Qual é a ideia geral do projeto?

A ideia geral do projeto foi realizar a criação de um APP com a ideia de speech to text.

	Onde iremos iniciar da seguinte forma:

-Vamos gravar uma mensagem de voz (Exemplo: O tempo da região sul do brasil é... // O calor é muito melhor pois..)

-Após gravar a mensagem de voz, o APP irá memorizar e converter em texto (irá aparecer o texto que falamos na tela) com a possibilidade de realizar uma melhoria/aprimoração nesse texto/frase.

-Após mensagem e texto memorizados, temos a possibilidade de ter a melhoria/aprimoração dessa mesma frase com a comunicação/integração com o chat gpt, sendo que irá continuar a frase que mencionamos acima.
Exemplo de aprimoração das mensagens:

-O tempo da região sul do brasil é muito agrádavel em determinadas épocas sendo possível agradar todas as pessoas da região (Apenas uma suposição)

-O calor é muito melhor pois temos a possibilidade de tomar bebidas geladas, visitar locais como praias, piscinas e nos divertir muito mais do que no inverno (Apenas uma suposição)

-Após tudo isso também temos a possibilidade de reproduzir o texto. E caso for inserir um novo texto todos os dados requisitados serão apagados para gerar um novo conteúdo.


B) Qual as tecnologias utilizadas, e porque?

-Utilizamos dart com framework Flutter para realizar a criação do projeto onde temos a possibilidade de criar o aplicativo mobile 

-Utilizamos a API do OPEN AI, assim podemos ter a integração que faz as continuações/aprimorações das mensagens solicitadas

-Pacote do Google speech



C) Qual a arquitetura do software? Quem é o back, o front, como se comunicam, etc

Código em dart com utilização do framework flutter


D) Explicar os diretórios do projeto, mostrando as responsabilidades técnicas de cada um.

> lib/main.dart - Onde temos o titulo do projeto, com uma rota direcionando para o diretório pages/demo.dart onde temos a principal parte do projeto,. Além disso no main temos a integração com a api do OPEN AI

> lib/pages/demo.dart - Onde temos todas as bibliotecas que foram necessárias para a realização do projeto incluido as da API / conversão do arquivo de audio / Google speech que faz a parte do speech to text / o gravador de voz 



E) Explicar o código dos principais arquivos do projeto. Ex: No backend, de for python/dart/js, explicar os métodos e funcionalidades. No frontend, de for flutter/html/react, explicar os principais componentes.

> Main.dart - const String openAiApiKey = String.fromEnvironment - comunicação com a API
> demo.dart - 	String transcriptedText = Onde será convertido de texto para audio
  		String generatedText = O texto que foi gerado com o audio aparecendo na tela
		await File('${await _localPath}/audio.mp3').create(recursive: true); = Conversão do audio 
      		await File('${await _localPath}/audio.flac').create(recursive: true); = Conversão do audio 
		ElevatedButtons - Ao pressionar para comunicar com o speech to text do google / Transcrição do audio / Aprimoramento do texto / Reprodução do audio
		

F) Por fim, explicar o passo-a-passo para a execução do projeto.

-Criamos um projeto flutter
-Passo a passo do projeto:
(1 - Criar campo para a gravação e memorização da mensagem onde utilizamos um pacote do google speech e também do flutter para ter o gravador de voz
 2 - Realizar a conversão do texto falado/gravado para aparecer em tela 
 3 - A mensagem gravada ficou salva em arquivo .mp3, sendo assim foi necessário realizar a conversão de .mp3 para .flac (tambem diminuindo o tamanho do arquivo na hora do armazenamento)
 4 - Realizar a integração com a API do OPEN AI para as melhorias das frases 
 5 - Reprodução do texto 
