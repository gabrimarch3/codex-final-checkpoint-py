# Generatore di Paragrafi per Blog

Questo progetto è un generatore di paragrafi per blog che utilizza l'API di OpenAI per creare contenuti in diverse lingue. L'utente può selezionare una lingua e fornire un argomento, e il programma genererà un paragrafo relativo all'argomento scelto.

## Requisiti

- Python 3.x
- Libreria `openai`
- Libreria `python-dotenv`
- Un file `.env` contenente la chiave API di OpenAI

## Installazione

1. Clona il repository:
    ```sh
    git clone <repository-url>
    cd progetto-finale-codex
    ```

2. Installa le dipendenze:
    ```sh
    pip install openai python-dotenv
    ```

3. Crea un file `.env` nella directory principale del progetto e aggiungi la tua chiave API di OpenAI:
    ```env
    API_KEY=la_tua_chiave_api
    ```

## Utilizzo

1. Esegui lo script `blog_generator.py`:
    ```sh
    python blog_generator.py
    ```

2. Seleziona una lingua tra le opzioni disponibili.

3. Inserisci l'argomento del paragrafo che desideri generare.

4. Segui le istruzioni sullo schermo per generare nuovi paragrafi o terminare il programma.

## Lingue Supportate

- Italiano
- Inglese
- Tedesco
- Francese
- Spagnolo

## Autore

Gabriel Marchegiani

