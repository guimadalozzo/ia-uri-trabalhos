from flask import Flask, render_template, request
import datetime
import pytz
import os.path
import google.auth.transport.requests
import google.oauth2.credentials
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import speech_recognition as sr
import pyttsx3
import calendar


def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = None


def obter_credenciais():
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/agendar')
def agendar():
    return render_template('agendar.html')


@app.route('/agendando', methods=['POST'])
def agendando():
    if request.method == 'POST':
        creds = obter_credenciais()
        service = build('calendar', 'v3', credentials=creds)

        evento = {
            'summary': request.form['nome'],
            'location': request.form['local'],
            'description': request.form['desc'],
            'start': {
                'dateTime': request.form['date1'],
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': request.form['date2'],
                'timeZone': 'America/Sao_Paulo',
            },
            'reminders': {
                'useDefault': True,
            },
        }
        evento_criado = service.events().insert(
            calendarId='primary', body=evento).execute()
        evento_url = f"https://calendar.google.com/calendar/r/eventedit/{evento_criado.get('id')}"
        mensagem = f"Evento {request.form['nome']} agendado para {request.form['date1']}."
        speak(mensagem)
        return render_template('index.html', url=evento_url)


@app.route('/compromissos')
def compromissos():
    qtd_eventos = request.args.get('qtd', default=10, type=int)
    creds = obter_credenciais()
    service = build('calendar', 'v3', credentials=creds)

    agora = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indica UTC
    eventos_result = service.events().list(calendarId='primary', timeMin=agora,
                                           maxResults=qtd_eventos, singleEvents=True, orderBy='startTime').execute()
    eventos = eventos_result.get('items', [])

    if not eventos:
        return "Nenhum evento encontrado."

    eventos_mes_atual = []
    for evento in eventos:
        data_hora_inicio = evento['start'].get(
            'dateTime', evento['start'].get('date'))
        inicio = datetime.datetime.fromisoformat(
            data_hora_inicio).astimezone(pytz.timezone('America/Sao_Paulo'))
        if inicio.month == datetime.datetime.now().month:
            evento_dict = {
                'summary': evento['summary'],
                'location': evento.get('location', ''),
                'description': evento.get('description', ''),
                'start': inicio.strftime('%d/%m/%Y %H:%M')
            }
            eventos_mes_atual.append(evento_dict)

    nome_mes_atual = calendar.month_name[datetime.datetime.now().month]

    engine = pyttsx3.init()
    eventos_mes_atual_str = '\n'.join(
        [f"{evento['summary']} em {evento['start']}" for evento in eventos_mes_atual])
    engine.say(
        f"Compromissos do mês de {nome_mes_atual}: {eventos_mes_atual_str}")
    engine.runAndWait()

    return render_template('compromissosM.html', eventos=eventos_mes_atual)


if __name__ == '__main__':
    app.run(debug=True)
