## Funziona ma prende poche righe, max 8

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd

url = 'https://www.eurobet.it/it/scommesse/#!'
webdriver = webdriver.Chrome()
webdriver.get(url)

# Wait for the events to appear on the page
wait = WebDriverWait(webdriver, 30)
events_locator = (By.CLASS_NAME, 'event-row')
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
soup = BeautifulSoup(webdriver.page_source, 'lxml')
print(soup.prettify())  # Add this line to check the page source
events = soup.find_all('div', {'class': 'event-row'})
print(len(events))  # Add this line to check the number of events
# Process the events
data = []
for event in events:
    team_names = event.find('div', {'class': 'event-players'}).text.strip().split(' - ')
    odds = event.find_all('div', {'class': 'quota-new'})
    odds_values = [odd.find('a').text for odd in odds]
    row = team_names + odds_values
    data.append(row)

# Create a DataFrame from the data and define the column names
df = pd.DataFrame(data, columns=['Home', 'Away', 'Home win', 'Tie', 'Away win', 'Under', 'Over'])

# Write the DataFrame to an Excel file
with pd.ExcelWriter('data/eurobet_data.xlsx') as writer:
    df.to_excel(writer, index=False)