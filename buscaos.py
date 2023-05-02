import speech_recognition as sr
import pyttsx3
from tkinter import *
import fdb

con = fdb.connect(
    host='localhost',
    database='C:\\syspro\\bd\\SYSDB.FBD',
    user='sysdba',
    password='masterkey'
)

def consulta_os(os_id): 
    cur = con.cursor()
    cur.execute('SELECT OS_DESC FROM  os_ordservico WHERE os_id = ? AND os_empcod = 1', (os_id,))
    result = cur.fetchall()
    cur.close()
    return result

recog = sr.Recognizer()

def ouvir():
    def SpeakText(command):
        out = pyttsx3.init()
        if (command != "desligar"):
            out.say(command)
        else:
            out.say("Ok, estou desligando...")
        out.runAndWait()

    text = ""

    if(text != "desligar"):
        try:
            with sr.Microphone() as mic:
                recog.adjust_for_ambient_noise(mic)
                audio = recog.listen(mic)
                text = recog.recognize_google(audio, language='pt-BR')
                text = text.lower()
                result = None
                if text.isnumeric():
                    result = consulta_os(int(text))

                if result is not None:
                    for row in result:
                        descricao = row[0]
                        SpeakText(descricao)
                        resultado_label.configure(text=descricao)
                else:
                    descricao = "Desculpe, não entendi o número da ordem de serviço."
                    SpeakText(descricao)
                    resultado_label.configure(text=descricao)

        except sr.RequestError as e:
            print("Não foi possível informar a OS; {0}".format(e))
        except sr.UnknownValueError as e:
            print("Não foi possível reconhecer o áudio; {0}".format(e))
    else:
        pyttsx3.init().runAndWait()

janela = Tk()
janela.title("Busca ordens de Serviço")

texto_orientacao = Label(janela, text="Clique no botão e fale a ordem de serviço desejada", font=("Arial", 12))
texto_orientacao.grid(column=0, row=0)

texto_orientacao = Label(janela, text="Clique aqui para ouvir", font=("Arial", 12))
texto_orientacao.grid(column=0, row=1)

botao = Button(janela, text="Fala", font=("Arial", 12), command=ouvir)
botao.grid(column=0,row=2)

resultado_label = Label(janela, text="", font=("Arial", 12))
resultado_label.grid(column=0, row=3)

botao_sair = Button(janela, text="Sair", font=("Arial", 12), command=janela.destroy)
botao_sair.grid(column=0,row=4)

def fechar_janela():
    con.close()
    janela.destroy()

janela.protocol("WM_DELETE_WINDOW", fechar_janela)

janela.mainloop()
con.close()