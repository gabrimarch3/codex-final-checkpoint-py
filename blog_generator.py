from openai import OpenAI #Importo la libreria openai per integrare l'IA generativa
import os #Importo la libreria os per utilizzare comandi da CLI direttamente nel codice
from dotenv import dotenv_values #Importo la libreria dotenv per creare variabili d'ambiente

config = dotenv_values(".env") #Dico alla liberia dotenv dove andare a prendere le variabili d'ambiente

# Pass the api_key directly when creating the OpenAI client instance
client = OpenAI(api_key=config.get('OPENAI_API_KEY')) #Inizializzo la variabile d'ambiente API_KEY

# Inizializzo le variabili selected_language e is_language_selected per gestire la selezione della lingua
selected_language = '' # Questa viene impostata a una stringa vuota per permettere al prompt di ricevere la lingua impostata dall'utente
is_language_selected = False # Questa viene impostata a False per permettere al ciclo while di partire

# La riga qui sotto corrisponde al comando CLI 'clear'
# Permette quindi di pulire il terminale quando il programma viene avviato
os.system('cls' if os.name == 'nt' else 'clear')

# Tutta questa parte rappresenta la schermata iniziale del programma presentando un titolo e la lista delle lingue da selezionare
print("Benvenuto nel generatore di paragrafi per blog!\n")

print("1) Italiano")
print("2) Inglese")
print("3) Tedesco")
print("4) Francese")
print("5) Spagnolo")
language = int(input("\nSeleziona una lingua da quelle sopra inserendo il numero corrispondente\n")) # La variabile language si occupa di ricevere un numero corrispondente alla lingua e salvarlo


# In questo ciclo while imposto per ogni numero corrispondente ad una lingua un valore da passare poi l prompt
while is_language_selected == False:
    if language == 1:
        selected_language = 'italiano'
        print("Hai selezionato: Italiano")
        is_language_selected = True
    elif language == 2:
        selected_language = 'Inglese'
        print("Hai selezionato: Inglese")
        is_language_selected = True
    elif language == 3:
        selected_language = 'Tedesco'
        print("Hai selezionato: Tedesco")
        is_language_selected = True
    elif language == 4:
        selected_language = 'Francese'
        print('Hai selezionato: Francese')
        is_language_selected = True
    elif language == 5:
        selected_language = 'Spagnolo'
        print("Hai selezionato: Spagnolo")
        is_language_selected = True
    else:
        # Qui viene riprodotta la schermata iniziale del programma con in aggiunta
        # una riga che notifica all'utente che la selezione non è stata fatta correttamente.
        # Questa parte di codice serve anche per evitare che il ciclo while vada in loop infinito
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ops! Il valore selezionato non corrisponde a nessuna lingua! Riprova")
        print("1) Italiano")
        print("2) Inglese")
        print("3) Tedesco")
        print("4) Francese")
        print("5) Spagnolo")
        language = int(input("\nSeleziona una lingua da quelle sopra inserendo il numero corrispondente\n")) # Evita il loop infinito
        


# Inizializzo la funzione in grado di generare un paragrafo nella lingua scelta su un determinato argomento sempre scelto dall'utente
# La funzione accetta un argomento di tipo stringa e restituisce un paragrafo in italiano
def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {
                'role': 'user',
                'content': f"Scrivi un paragrafo in {selected_language} riguardo l'argomento scelto dall'utente ovvero {paragraph_topic}"
            }
        ]
    )

    retrieve_blog = response.choices[0].message.content

    return retrieve_blog


keep_writing = True

while keep_writing:
    answer = input("Vuoi generare un paragrafo? S per si, N per no:)")
    if answer == 'S' or answer == 's':
        paragraph_topic = input("Inserisci l'argomento del paragrafo: ")
        print(generate_blog(paragraph_topic))
    elif answer == 'N' or answer == 'n':
        print("\n Grazie per aver utilizzato il generatore di paragrafi!")
        keep_writing = False
    else:
        print("Non hai inserito una risposta valida, riprova.")


