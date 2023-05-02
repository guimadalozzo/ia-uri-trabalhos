import requests
import speech_recognition as sr
import tkinter as tk

# Função responsável por buscar as informação do pokemon por Texto
def buscarPokemonPorTexto():
    pokemon_name = inputtxt.get(1.0, "end-1c").lower().strip()
    chamarAPI(pokemon_name)


# Função responsável por buscar as informação do pokemon por Voz
def buscarPokemonPorVoz():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        txt = "Por favor, diga o nome de um Pokémon:"
        lbl.config(text = txt)
        inputtxt.delete("1.0","end")
        frame.update()
        # Escutando a entrada de áudio do usuário
        audio = r.listen(source)  
    # Usando a API de reconhecimento de fala do Google para transcrever o áudio
    try:
        # Tentando transcrever o áudio usando a API do Google
        pokemon_name = r.recognize_google(audio).lower() #Letra minuscusla
        txt = f"Recuperando informações sobre {pokemon_name}..."
        inputtxt.insert(tk.END, pokemon_name)
        lbl.config(text = txt)
        chamarAPI(pokemon_name)
        #TESTADO COM PIKACHU, CHARMANDER E METAPOD, SÃO NOMES MAIS FÁCEIS DE SEREM RECONHECIDOS
    except sr.UnknownValueError:
        txt = "Desculpe, não entendi. \n  Por favor, digite o nome de um Pokemon e clique no Botão Pesquisar"
        # Se a fala não puder ser transcrita, pedimos ao usuário para digitar o nome do pokemon
        lbl.config(text = txt)      


def chamarAPI(text):
    # Fazendo uma solicitação ao PokeAPI com o nome do Pokemon
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{text}") 
    if response.status_code == 200:
# Convertendo a resposta da API
        pokemon_data = response.json()
# Imprimindo informações básicas sobre o Pokemon
        txt = f"Nome: {pokemon_data['name'].capitalize()} \n"
        txt += f"ID: {pokemon_data['id']} \n"
        txt += f"Altura: {pokemon_data['height']} \n"
        txt += f"Peso: {pokemon_data['weight']} \n"
        txt += f"Tipo(s): {[t['type']['name'] for t in pokemon_data['types']]} \n"
        lbl.config(text = txt)
    else:
        txt = "Desculpe, não encontramos esse Pokemon. Por favor, tente novamente."
        lbl.config(text = txt)

# Janela
frame = tk.Tk()
frame.title("Pokémon")
frame.geometry('400x300')

# Criação do Label
lblDesc = tk.Label(frame, text = "Fale ou Digite para buscar as informações sobre um Pokémon")
lblDesc.place(relx=0.5, rely= 0.1, anchor = 'center')
  
# Criação da caixa de texto
inputtxt = tk.Text(frame, height = 2, width = 20)
inputtxt.place(relx=0.5, rely= 0.2, anchor = 'center')
  
# Criação dos botões
printButton = tk.Button(frame, text = "Falar",  command = buscarPokemonPorVoz)
printButton.place(relx=0.5, rely= 0.4, anchor = 'center')

printButton = tk.Button(frame, text = "Pesquisar",  command = buscarPokemonPorTexto)
printButton.place(relx=0.5, rely= 0.5, anchor = 'center')
  
# Criação do Label
lbl = tk.Label(frame, text = "")
lbl.place(relx=0.5, rely= 0.7, anchor = 'center')

frame.mainloop()
