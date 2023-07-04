import csv
import xml.etree.ElementTree as ET
import requests

# Define the URL to the XML file
url = 'https://www.snai.it/sites/default/files/dati_processi/psqf3_piuGiocate.xml'

# Make an HTTP request to fetch the XML data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML data
    root = ET.fromstring(response.content)

    # Create a list to store the extracted data
    data = []

    # Extract team names and odds from XML
    for avvenimento in root.iter("avvenimento"):
        team1 = ""
        team2 = ""
        odds = []

        for element in avvenimento.iter():
            
            if element.tag == "avvenimento":
                des_avvenimento = avvenimento.get("des_avvenimento")
                team1, team2 = des_avvenimento.split(" - ")
            elif element.tag == "evento":
                odds.append(element.get("quota"))

        if len(odds) >= 3:
            # Append the extracted data to the list
            data.append([team1, team2, int(odds[0])/100, int(odds[1])/100, int(odds[2])/100])

    # Define the path to save the CSV file
    csv_file = "data/snai_data.csv"

    # Write the extracted data to a CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Home", "Away", "1", "X", "2"])  # Write header row
        writer.writerows(data)  # Write data rows

    print("CSV file saved successfully!")
else:
    print(f"Failed to fetch XML data from the URL. Status code: {response.status_code}")
