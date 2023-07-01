## I valori sono sballati e non riesco a salvarlo come dataframe e quindi csv file.

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

url = 'https://www.sisal.it/scommesse-matchpoint/sport/calcio'
webdriver = webdriver.Chrome()
webdriver.get(url)

# Wait for the events to appear on the page
wait = WebDriverWait(webdriver, 30)
events_locator = (By.CLASS_NAME, 'text-capitalize')
wait.until(EC.presence_of_element_located(events_locator))
#time.sleep(15)
# Define the initial scroll height
last_height = webdriver.execute_script("return document.body.scrollHeight")

# Infinite scroll down
SCROLL_PAUSE_TIME = 0.5
while True:
    # Scroll down to bottom
    webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = webdriver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



# Parse the page source
#soup = BeautifulSoup(webdriver.page_source[206634:], 'lxml')
soup = BeautifulSoup(webdriver.page_source, 'lxml')



# Extract team names
team_spans = soup.find_all('span', {'class': 'd-block text-capitalize'})
team_names = [span.text for span in team_spans]
print(team_names)
# Extract odds
odds = soup.find_all('div', {'class': 'selectionButton_selectionPrice__B-6jq'})

data = [odd.text.strip() for odd in odds]
print(data)

data_trimmed = data[5:]

print(data_trimmed)
#data2 = [data_trimmed[i:i+6] for i in range(0, len(data_trimmed), 6)]

data_final = data_trimmed
print(data_final)

for i in range(0, len(team_names), 2):
    team1 = team_names[i]
    team2 = team_names[i+1]
    team_data = data_trimmed[i*5:(i+1)*5]
    data_final.append((team1, team2, team_data))

print(data_final)
data_final = data_final.reshape((145, 7))
df = pd.DataFrame(data_final, columns=['Home', 'Away', 'Home win', 'Tie', 'Away win', 'Under', 'Over'])

# Write the DataFrame to a CSV file
df.to_csv('data/sisal_data.csv', index=False)

print("Data saved to CSV file.")