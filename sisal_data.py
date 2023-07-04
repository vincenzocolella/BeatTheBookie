import csv
import itertools
import os
import urllib3
import json
import requests
# Creazione del payload
payload = {
    "offerId" : "0"
}

# Conversione del payload in formato JSON
payload_json = json.dumps(payload)

# Creazione dell'oggetto `PoolManager` di urllib3
http = urllib3.PoolManager()


params = {"offerId": "0"}
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Dnt": "1",
    "Host": "betting.sisal.it",
    "Origin": "https://www.sisal.it",
    "Pragma": "no-cache",
    "Referer": "https://www.sisal.it/",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "User_data": "{\"accountId\":null,\"token\":null,\"tokenJWT\":null,\"locale\":\"it_IT\",\"loggedIn\":false,\"channel\":62,\"brandId\":175,\"offerId\":0}"
}


# Effettuare la richiesta POST
url = "https://betting.sisal.it/api/lettura-palinsesto-sport/palinsesto/prematch/top-match/1?offerId=0"
#response = http.request('POST', url, body=payload_json, headers=headers)

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    response_data = response.json()
    # salva la risposta in un file di testo
    with open("response_data.txt", "w") as f:
        json.dump(response_data, f)
else:
    print(f"Errore nella richiesta: {response.status_code} - {response.reason}")
    
if response.status_code == 200:
    response_data = response.json()

data=response_data
    # Prepare CSV file
csv_file = "data/sisal_data.csv"
fieldnames = ["Home","Away","1","X","2"]

# Extract and save data to CSV
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for key, value in data["scommessaMap"].items():
        try:
            teams = value["descrizioneAvvenimento"].split(" - ")
            team1 = teams[0]
            team2 = teams[1]
            new_key = key + "-0"
            esito_list = data["infoAggiuntivaMap"][new_key]["esitoList"]
            print(esito_list)
            odds_1 = next(esito["quota"] for esito in esito_list if esito["codiceEsito"] == 1)
            odds_x = next(esito["quota"] for esito in esito_list if esito["codiceEsito"] == 2)
            odds_2 = next(esito["quota"] for esito in esito_list if esito["codiceEsito"] == 3)
        except:
            continue
        
        writer.writerow({
                "Home": team1,
                "Away": team2,
                "1": odds_1/100,
                "X": odds_x/100,
                "2": odds_2/100
        })
        
print(f"Data saved to '{csv_file}' successfully.")