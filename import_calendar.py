import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import inflect

p = inflect.engine()

import re


## Autenticazione con Google Calendar API

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_DIR = '.credentials'
CREDENTIALS_PATH = os.path.join(CREDENTIALS_DIR, 'credentials.json')
TOKEN_PATH = os.path.join(CREDENTIALS_DIR, 'token.json')

creds = None
# Creare la directory delle credenziali se non esiste
if not os.path.exists(CREDENTIALS_DIR):
    os.makedirs(CREDENTIALS_DIR)

# Il file token.json memorizza i token di accesso e aggiornamento dell'utente.
if os.path.exists(TOKEN_PATH):
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

# Se non ci sono credenziali valide, chiedi all'utente di accedere.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
    # Salva le credenziali per la prossima esecuzione
    with open(TOKEN_PATH, 'w') as token:
        token.write(creds.to_json())


## Importa eventi dal calendario
try:
    service = build('calendar', 'v3', credentials=creds)
    xai_id = '8881f4je38oo4rbj8qs2cr05lo@group.calendar.google.com'
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    xai_bday = '2019-01-01T11:30:00+02:00'
    events_result = service.events().list(calendarId=xai_id, timeMin=xai_bday,
                                          maxResults=200, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    # Prints the start and name of the next 10 events
    seminars = []
    for i, event in enumerate(events):
        seminar = {}
        id = event['id']
        imported_event = service.events().get(calendarId=xai_id, eventId=id).execute()

        if '[XAI][SM]' in imported_event['summary']:
            start = imported_event['start'].get('dateTime', imported_event['start'].get('date'))
            seminar['date'] = {}
            seminar['date']['day'] = start.split('T')[0].split('-')[2]
            seminar['date']['month'] = start.split('T')[0].split('-')[1]
            seminar['date']['year'] = start.split('T')[0].split('-')[0]
            seminar['date']['hour'] = start.split('T')[1]
            seminar['complete_date'] = start
            seminar['summary'] = imported_event['summary'].replace('[XAI][SM]', '').strip()
            if 'location' in imported_event:
                seminar['location'] = imported_event['location']
            if 'description' in imported_event:
                seminar['description'] = imported_event['description']

            seminars.append(seminar)

            # if i == 7:
            #     break

except HttpError as error:
    print('An error occurred: %s' % error)




## Funzione per convertire il titolo dell'evento in un nome di file markdown

def title_to_md(event):
    def remove_special_characters(text):
        return re.sub(r'[^A-Za-z0-9\s]', '', text)

    title = event['summary']
    ltitle = title.split(' ')
    pltitle = [remove_special_characters(x.strip()) for x in ltitle]
    pltitle = [x for x in pltitle if x]
    name = '-'.join(pltitle[:5])
    mdName = event['date']['year'] + '-' + event['date']['month'] + '-' + event['date']['day'] + '-' + name + '.md'
    return mdName


## Creazione di un file markdown per ogni evento

# post_list = []
# for event in seminars:
#     [title_to_md(event) for event in seminars]



def create_file_in_post_folder(event):
    # Funzione per rimuovere i caratteri speciali da un testo (ad eccezione di spazi, lettere e numeri e i segni di punteggiatura come virgole punti due punti e trattini)
    def special_remove(text):
        return re.sub(r'[^A-Za-z0-9\s.,:;-<>#]', '', text)
    
    # Event variable is a dictionary with keys: 'summary', 'complete_date', 'description'
    title = special_remove(event['summary'])
    event_date = event['complete_date'].replace('T', ' ').split('+')[0]
    #set current date to now if event_date is in the future
    if datetime.datetime.now() < datetime.datetime.strptime(event_date, '%Y-%m-%d %H:%M:%S'):
        date = datetime.datetime.now().isoformat()
        
    year = event_date.split('-')[0]
    if 'location' in event:
        location = event['location']
    else:
        location = ''
    # description = special_remove(event['description'])
    description = event['description']
    if '##' in description:
        presenter = description.split('##')[1].strip()
        # Remove html element from presenter variable string:
        presenter = re.sub('<[^<]+?>', '', presenter)
        description = description.split('##')[2]

    # Assicurati che la directory _posts/xai esista
    directory = "_posts/xai"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = title_to_md(event)
    file_path = os.path.join(directory, filename)

    # Controlla se il file esiste già, altrimenti crealo
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            # Puoi aggiungere contenuto di default se necessario
            f.write(f'''---
layout: post
title: "{title}"
event-date: "{event_date}"
date: "{datetime.datetime.now().isoformat()}"
year: {year}
tags: "seminar"
location: "{location}"
presenter: "{presenter}"
---
<h5>{presenter}</h5>
<em>Location: {location}<em>
<br>
<hr>

{description}

                ''')  # File vuoto
        print(f"File created: {file_path}")
    else:
        print(f"File already exists: {file_path}")


# Esegui la funzione per ogni nome evento
for event in seminars:
    create_file_in_post_folder(event)

print('Done!')