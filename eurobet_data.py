import csv
import itertools
import os
import urllib3
import json

# Creazione del payload
payload = {
    "betAliasUrl": "1x2",
    "disciplineAliasUrl": "calcio",
    "live": 0,
    "oddFilterType": "LTE",
    "oddValue": "150",
    "prematch": 1
}

# Conversione del payload in formato JSON
payload_json = json.dumps(payload)

# Creazione dell'oggetto `PoolManager` di urllib3
http = urllib3.PoolManager()

# Definizione degli header
headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "X-Eb-Accept-Language": "it_IT",
    "X-Eb-Marketid": "5",
    "X-Eb-Platformid": "2",
    "Referer": "https://www.eurobet.it/it/scommesse/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Origin": "https://www.eurobet.it"
}

# Effettuare la richiesta POST
url = "https://www.eurobet.it/search-service/sport-schedule/services/search/event/odd-filter"
response = http.request('POST', url, body=payload_json, headers=headers)

# Ottenere la risposta
response_data = response.data.decode('utf-8')
response_json = json.loads(response_data)
# Definisci i valori per le colonne
valori = []
home=[]
ospite=[]
one=[]
x=[]
two=[]

# Esegui l'iterazione su ogni elemento nel JSON
for item in response_json['result']:
    # Verifica se la stringa "manchester city" è presente nel valore
    for elem in item['itemList']:
        home.append(elem['eventInfo']['teamHome']['description'])
        ospite.append(elem['eventInfo']['teamAway']['description'])
        x12 = 0
        for val in elem["betGroupList"][0]['oddGroupList'][0]['oddList']:
            numero = int(val['oddValue']) /100
            numero = f"{numero:.2f}"
            if x12 ==0:
                one.append(numero)
            elif x12 == 1:
                x.append(numero)
            else:
                two.append(numero)
            x12+=1

# Scrivi i valori su file CSV
directory = 'data'
if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, 'eurobet_data.csv')

with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Home", "Away", "1", "X", "2"])
    for row in zip(home, ospite, one, x, two):
        writer.writerow(row)
    print("I valori sono stati scritti nel file CSV.")