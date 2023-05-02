import speech_recognition as sr
import pyttsx3
import requests
from flask import Flask, render_template, request

recog = sr.Recognizer()

app = Flask(__name__)

def SpeakText(command):
    out = pyttsx3.init()
    if command != "desligar":
        out.say(command)
    else:
        out.say("Ok! Estou desligando...")
    out.runAndWait()

def get_weather(city):
    api_key = "66edcb4dbe36c6e04aaf2899a7209a9d"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"Atualmente em {city} está fazendo {weather} com temperatura de {temp:.1f} graus Celsius."
    else:
        return f"Não foi possível obter a previsão do tempo de {city}."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    text = request.form['text']
    text = text.lower()
    if "tempo em" in text:
        city = text.split("tempo em ")[1]
        weather = get_weather(city)
        print(f"IA: {weather}")
        SpeakText(weather)
        return weather
    return "Comando não reconhecido"

if __name__ == '__main__':
    app.run(debug=True)
