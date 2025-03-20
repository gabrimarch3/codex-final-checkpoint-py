import openai
import os
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

selected_language = ''
is_language_selected = False

os.system('cls' if os.name == 'nt' else 'clear')
print("Benvenuto nel generatore di paragrafi per blog!\n")

print("1) Italiano")
print("2) Inglese")
print("3) Tedesco")
print("4) Francese")
print("5) Spagnolo")
language = int(input("\nSeleziona una lingua da quelle sopra inserendo il numero corrispondente\n"))

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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Ops! Il valore selezionato non corrisponde a nessuna lingua! Riprova")
        print("1) Italiano")
        print("2) Inglese")
        print("3) Tedesco")
        print("4) Francese")
        print("5) Spagnolo")
        language = int(input("\nSeleziona una lingua da quelle sopra inserendo il numero corrispondente\n"))
        

    

# Inizializzo la funzione in grado di generare un paragrafo in italiano su un determinato argomento
# La funzione accetta un argomento di tipo stringa e restituisce un paragrafo in italiano
def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = f"Scrivi un paragrafo in {selected_language} riguardo l'argomento scelto dall'utente ovvero {paragraph_topic}",
        max_tokens = 400,
        temperature = 0.3,
    )

    retrieve_blog = response.choices[0].text

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


