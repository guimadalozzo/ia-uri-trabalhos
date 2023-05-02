from flask import Flask, request, render_template
import speech_recognition as sr 
import pyttsx3 
import requests
from PIL import Image
from io import BytesIO
import threading

#Objeto app é criado como uma instância da classe Flask que define a aplicação web.
app = Flask(__name__)

#Criamos o objeto para habilitar microfone e realizar o reconhecimento da fala
recog = sr.Recognizer() 

#Criamos uma função	que	irá, a partir do PyTTSx3, repetir (falar) o comando do usuário
def SpeakText(comand): 
    out = pyttsx3.init()
    if (comand != "desligar"):
        #Armazena um comando na fila a ser executado
        out.say(comand) 
    else:
        out.say("Ok! Estou desligando...")
        #Executa todos os comandos adicionados na fila de comandos
        out.runAndWait() 

#Cria uma rota padrão da aplicação para a página inicial que retorna a página HTML 'index.html' usando o método render_template.
@app.route('/')
def index():
    return render_template('index.html')

#Cria outra rota para a página 'reconhecimento_de_voz'
@app.route('/reconhecimento_de_voz')
def reconhecimento_de_voz():
    text = ""
    while (text != "desligar"):
        try:
            #Habilita o microfone como recurso de entrada de audio
            with sr.Microphone() as mic: 
                #Aguarda um segundo para limpar o ruído do ambiente 
                recog.adjust_for_ambient_noise(mic) 
                print("IA: ouvindo...")
                #Inicia a escuta da fala do usuário
                audio = recog.listen(mic) 
                #Utiliza o método de reconhecimento de fala do Google
                text = recog.recognize_google(audio, language='pt-BR') 
                text = text.lower()
                #Executa o método para a IA repetir o que foi dito
                print("IA: Você disse " + text + "") 
                SpeakText(text)
                return search_marketplace(text)
        except sr.RequestError as e:
            print("Não foi possivel requisitar o pedido; {0}".format(e))

        except sr.UnknownValueError:
            print("Um erro desconhecido ocorreu")

    return "Reconhecimento de voz finalizado"

def say_results(results):
    result_titles = [result["title"] for result in results]
    text = ", ".join(result_titles)
    engine = pyttsx3.init()
    engine.setProperty('voice', 'brazil')
    engine.setProperty('encoding', 'utf-8')
    engine.say("Os resultados da busca são: " + text)
    engine.runAndWait()

@app.route('/busca_mercado_livre/<query>')
def search_marketplace(query):
    url = "https://api.mercadolibre.com/sites/MLB/search"
    payload = {
        "q": query,
        "limit": 5,
        "offset": 0
    }

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        results = response.json()["results"]
        thread = threading.Thread(target=say_results, args=(results,))
        thread.start()
        return render_template('resultado_busca.html', results=results)
    else:
        return "Não foi possível obter os resultados."

if __name__ == '__main__':
    app.run(debug=True)
