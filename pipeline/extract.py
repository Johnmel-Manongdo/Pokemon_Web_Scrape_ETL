import asyncio
import aiohttp
import logging
import pandas as pd
from bs4 import BeautifulSoup

# Setup logging to display messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = 'https://pokemondb.net/'
URL = BASE_URL + '/pokedex/all'

# Asynchronous function to fetch the HTML content
async def fetch(url, session):
    logging.info(f'Fetching URL: {url}')
    async with session.get(url) as response:
        text = await response.read()
        return text.decode('utf-8')

# Asynchronous function to fetch and process data for each pokemon row
async def fetch_pokemon_data(row, session, index, total_rows):
    columns = row.find_all('td')

    # Extract pokemon data from the table cells
    dex_number = columns[0].find('span', {'class': 'infocard-cell-data'}).text.strip()
    name = columns[1].find('a', {'class': 'ent-name'}).text.strip()
    form = columns[1].find('small', {'class': 'text-muted'})
    types = [t.text.strip() for t in columns[2].find_all('a', {'class': 'type-icon'})]
    total = columns[3].text.strip()
    hp = columns[4].text.strip()
    attack = columns[5].text.strip()
    defense = columns[6].text.strip()
    sp_atk = columns[7].text.strip()
    sp_def = columns[8].text.strip()
    speed = columns[9].text.strip()

    if form:
        form = form.text.strip()

    link = columns[1].find('a', {'class': 'ent-name'}).get('href')
    full_link = BASE_URL + link

    # Fetch additional pokemon page for more data
    pokemon_page = await fetch(full_link, session)
    pokemon_soup = BeautifulSoup(pokemon_page, 'html.parser')

    additional_data = pokemon_soup.find_all('table', {'class': 'vitals-table'})
    species = additional_data[0].find('th', string='Species').find_next('td').text.strip()
    height = additional_data[0].find('th', string='Height').find_next('td').text.strip()
    weight = additional_data[0].find('th', string='Weight').find_next('td').text.strip()

    # Log the progress of tasks
    logging.info(f'Fetched {index}/{total_rows}: {name} ({form})')

    # Return a dictionary of pokemon data
    return {
        'Dex_Number': dex_number,
        'Name': name,
        'Form': form,
        'Types': types,
        'Species': species,
        'Height': height,
        'Weight': weight,
        'Total': total,
        'HP': hp,
        'Attack': attack,
        'Defense': defense,
        'Sp_Atk': sp_atk,
        'Sp_Def': sp_def,
        'Speed': speed,
    }

# Asynchronous function to handle the overall data extraction for all pokemon
async def extract_pokemon_data():
    async with aiohttp.ClientSession() as session:
        response = await fetch(URL, session)
        soup = BeautifulSoup(response, 'html.parser')

        # Find the pokemon table and extract all rows except the header
        table = soup.find('table', {'id': 'pokedex'})
        rows = table.find_all('tr')[1:]
        total_rows = len(rows)

        # Create a list of tasks to fetch data for each pokemon row
        tasks = [fetch_pokemon_data(row, session, index, total_rows) for index, row in enumerate(rows, start=1)]
        pokemon_data = await asyncio.gather(*tasks)

        # Create a DataFrame from the fetched pokemon data and save it to a CSV file
        df = pd.DataFrame(pokemon_data)
        df.to_csv('pokemon_data.csv', encoding='utf-8', index=False)

# Function to run the extraction function
def extract_task():
    asyncio.run(extract_pokemon_data())  # Run the asynchronous extraction task in the event loop

if __name__ == "__main__":
    extract_task()
