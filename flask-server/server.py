from flask import Flask
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

@app.route("/getWords")
def getWords():
    recog = sr.Recognizer()

    def SpeakText(command):
        out = pyttsx3.init()
        if (command != "desligar"):
            out.say(command)
        else:
            out.say("Ok Seu Lindo, Estou desligando...")
        out.runAndWait()
    
    text = ""
    while(text != "desligar"):
        try:
            with sr.Microphone() as mic:
                recog.adjust_for_ambient_noise(mic)
                print("IA: ouvindo...")
                audio = recog.listen(mic)
                text = recog.recognize_google(audio, language='pt-BR')
                text = text.lower()
                print("IA: Você disse "+text+"")
                SpeakText(text)
                return text
                
        except sr.RequestError as e:
            print("Não foi possível requisitar o pedido; {0}".format(e))
            
        except sr.UnknowValueError:
            print("Um erro desconhecido ocorreu")
        
    # return {"test": ["Renan", "Marcos", "Andreolla", "Lise"]}

if __name__ == "__main__":
    app.run(debug=True)


# import socket

# HOST = '127.0.0.1'  # endereço IP do servidor
# PORT = 5000  # porta em que o servidor irá escutar

# # cria um objeto socket TCP/IP
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # atribui o endereço e a porta ao socket
# server_socket.bind((HOST, PORT))

# # começa a escutar por conexões
# server_socket.listen()

# print(f"Servidor ouvindo em {HOST}:{PORT}")

# while True:
#     # espera por uma conexão
#     client_socket, address = server_socket.accept()

#     # lê a mensagem enviada pelo cliente
#     # data = client_socket.recv(1024).decode()

#     recog = sr.Recognizer()

#     def SpeakText(command):
#         out = pyttsx3.init()
#         if (command != "desligar"):
#             out.say(command)
#         else:
#             out.say("Ok Seu Lindo, Estou desligando...")
#         out.runAndWait()
        
#     text = ""
#     while(text != "desligar"):
#         try:
            
#             with sr.Microphone() as mic:
#                 recog.adjust_for_ambient_noise(mic)
#                 print("IA: ouvindo...")
#                 audio = recog.listen(mic)
#                 text = recog.recognize_google(audio, language='pt-BR')
#                 text = text.lower()
#                 print("IA: Você disse "+text+"")
#                 client_socket.send(text.encode())
#                 SpeakText(text)
                
#         except sr.RequestError as e:
#             print("Não foi possível requisitar o pedido; {0}".format(e))
            
#         except sr.UnknowValueError:
#             print("Um erro desconhecido ocorreu")

#     # imprime a mensagem recebida
#     # print(f"Mensagem recebida: {data}")

#     # envia uma resposta para o cliente
#     # response = "Olá, cliente!"
#     # client_socket.send(response.encode())

#     # fecha a conexão com o cliente
#     client_socket.close()
