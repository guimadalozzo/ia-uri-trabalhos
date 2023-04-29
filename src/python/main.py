from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import psycopg2
import os
import random
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet


app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
db_config = {
    'host': 'babar.db.elephantsql.com',
    'database': 'slwlbmhz',
    'user': 'slwlbmhz',
    'password': 'u94EkE3H15Z3yYLYf9uZh4LRCqlISLim',
    'port': '5432'
}

# Inicializa o reconhecedor
r = sr.Recognizer()

@app.route('/api/question', methods=['GET'])
def question():
    # Conexão com o banco de dados
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    # Consulta SQL para selecionar um registro aleatório
    cur.execute('SELECT * FROM sentences ORDER BY RANDOM() LIMIT 1')

    # Obtenha o resultado da consulta e transforme-o em um dicionário Python
    result = cur.fetchone()
    sentence = {
        'phrase': result[1],
        'correct_word': result[2],
    }

    # Guarda a palavra certa dentro da variável word
    word = result[2];

    # Feche o cursor e a conexão com o banco de dados
    cur.close()
    conn.close()

    # Gera as quatro palavras aleatórias
    option_words = generate_options(word)

    # Gera a questão com a frase, palavra correta e alternativas
    question = [sentence, option_words]

    return jsonify(question)

# Rota que recebe o arquivo de áudio enviado pelo JavaScript
@app.route('/api/recognition', methods=['POST'])
def recognition():
    # Obtém o arquivo de áudio enviado pelo JavaScript
    audio_file = request.files['audio']

    # Salva o arquivo de áudio em um local específico
    audio_file.save('audio.webm')

    # Faz o reconhecimento da palavra
    text = make_speech_recognition()

    # Retorna uma resposta para o JavaScript
    return text

def make_speech_recognition():
    with sr.AudioFile('audio.webm') as source:
        # Lê o áudio do arquivo
        audio = r.record(source)

        try:
            # Usa o Google Speech Recognition para reconhecer a fala
            text = r.recognize_google(audio, language='en', show_all=True)
            return text
        except sr.UnknownValueError:
            return 'Não foi possível reconhecer a fala'
        except sr.RequestError as e:
            return 'Erro ao se comunicar com o serviço de reconhecimento de fala: {0}'.format(e)

# Gera 3 novas palavras
# Parametro word = palavra correta 
# Retorna um array conjunto de 4 palavras (a certa e outras três aleatórias)
def generate_options(word):
    synonyms = set()
    antonyms = set()

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())

    # remove a palavra fornecida dos sinônimos
    if word in synonyms:
        synonyms.remove(word)

    # obtém o caminho do diretório atual e junta com o nome do arquivo
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir_path, "google-10000-english.txt")

    # lê a lista de palavras comuns do Google
    with open(filename, 'r') as f:
        all_words = [word.strip() for word in f.readlines()]

    # encontra 3 palavras aleatórias que não são sinônimos ou antônimos da palavra fornecida
    random_words = []
    while len(random_words) < 3:
        random_word = random.choice(all_words)
        if random_word != word and random_word not in synonyms and random_word not in antonyms and "'" not in random_word and "_" not in random_word:
            # ignora palavras menos frequentes
            if all_words.index(random_word) < 1000 and all_words.index(random_word) > 300:
                random_words.append(random_word)

    # adicionar a palavra fixa em uma posição aleatória na lista
    random_words.insert(random.randint(0, 2), word)

    # embaralha a lista de palavras aleatórias
    random.shuffle(random_words)

    return random_words


if __name__ == '__main__':
    app.run(debug=True)
