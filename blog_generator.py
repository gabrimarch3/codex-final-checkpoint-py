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

language = 0

# Questa parte gestisce l'output colorato nel terminale
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def select_a_language():
    global language
    print(f"{GREEN}Benvenuto nel generatore di onepage di Gabriel Marchegiani!{RESET}\n")
    print("1) Italiano")
    print("2) Inglese")
    print("3) Tedesco")
    print("4) Francese")
    print("5) Spagnolo")
    language = int(input("\nSeleziona una lingua da quelle sopra inserendo il numero corrispondente\n")) # La variabile language si occupa di ricevere un numero corrispondente alla lingua e salvarlo
    return language

language = select_a_language()

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
        print(f"{RED}Ops! Il valore selezionato non corrisponde a nessuna lingua! Riprova{RESET}")
        select_a_language() # Evita il loop infinito
        


# Inizializzo la funzione in grado di generare un paragrafo nella lingua scelta su un determinato argomento sempre scelto dall'utente
# La funzione accetta un argomento di tipo stringa e restituisce un paragrafo in italiano
def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages = [
            {
                'role': 'system',
                'content': 'You are an expert web designer and developer specialized in creating stunning one-page websites with modern design principles.'
            },
            {
                'role': 'user',
                'content': f"""
                            Crea una pagina onepage in {selected_language} sul tema: "{paragraph_topic}".
                            
                            REQUISITI TECNICI:
                            - Utilizza HTML5 semantico (header, nav, main, section, footer)
                            - Integra Tailwind CSS via CDN per lo styling
                            - Includi FontAwesome o Google Material icons per icone moderne
                            - Aggiungi animazioni fluide con CSS e JavaScript minimalista
                            - Design completamente responsive e mobile-first
                            - Palette colori armoniosa (max 3-4 colori principali)
                            - Non deve sembrare creata da un IA
                            - Assicurati che il codice sia ben strutturato e facile da mantenere
                            - Includi meta tag per SEO e social media (Open Graph, Twitter Cards)
                            - Assicurati che la pagina sia accessibile (rispetta le linee guida WCAG)
                            - Non usare immagini o video
                            
                            STRUTTURA RICHIESTA:
                            1. Hero section con gradienti dinamici o animati
                            2. Navbar sticky con logo e links funzionanti
                            3. 2-3 sezioni di contenuto con layout moderni e TANTO TESTO per ogni sezione (grid/flex)
                               - Ogni sezione deve contenere almeno 300-400 parole di testo informativo
                               - Il testo deve essere dettagliato, approfondito e ricco di informazioni sul tema
                               - Usa sottotitoli, elenchi puntati e paragrafi ben strutturati
                               - Assicurati di coprire diversi aspetti del tema richiesto
                               - Il contenuto testuale deve sembrare scritto da un esperto del settore
                            4. Componenti interattivi (es. slider, tabs, accordions, counters) che contengano ulteriore testo informativo
                            6. Footer elegante con credits (one page creata dal tool python di Gabriel Marchegiani)
                            
                            STILE VISIVO:
                            - Design pulito e minimalista, abbondante whitespace
                            - Tipografia moderna e leggibile (max 2-3 font diversi)
                            - Elementi UI con effetti hover raffinati
                            - Animazioni al caricamento e allo scroll
                            - Shadow e bordi sottili per creare profondità
                            - Utilizza una griglia per mantenere l'allineamento e la coerenza
                            - Assicurati che i colori e i font siano coerenti in tutta la pagina
                            
                            CONTENUTO TESTUALE:
                            - Fornisci testo dettagliato e abbondante su ogni aspetto del tema
                            - Assicurati che ogni paragrafo sia completo e ricco di contenuti (minimo 4-5 frasi per paragrafo)
                            - Includi almeno 1000-1500 parole di testo totali nella pagina
                            - Il testo deve essere strutturato in modo logico e ben organizzato
                            - Usa un linguaggio professionale e appropriato per il tema
                            
                            IMPORTANTE: Scrivi SOLO codice HTML completo e funzionante, senza commenti introduttivi o conclusivi e senza marcatori html come '''html e così via
                            """
            }
        ],
        temperature = 0.7
    )

    retrieve_blog = response.choices[0].message.content

    #Aggiungo qui una funzione per creare un file di testo e inserire il paragrafo creato
    save_on_file = open(f"{paragraph_topic}.html", 'w')
    save_on_file.write(retrieve_blog)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{GREEN} File generato con successo!{RESET}")
    save_on_file.close()

    return retrieve_blog

# Prompt the user to input the topic for the blog paragraph
paragraph_topic = input("Inserisci l'argomento della onepage che vuoi creare: ")

# Call the generate_blog function with the user-provided topic
generate_blog(paragraph_topic)

