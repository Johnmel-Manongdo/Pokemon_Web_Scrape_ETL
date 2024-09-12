# Pokemon Web Scraping, Data Cleaning, and SQL Server Loading

This project involves scraping data from a Pokemon website (https://pokemondb.net/), cleaning and transforming the data, and loading it into a Microsoft SQL Server database. The pipeline is implemented in Python, utilizing asynchronous web scraping, data transformation, and database operations.

## Features
- **Asynchronous Web Scraping:** Uses aiohttp and BeautifulSoup to efficiently scrape Pokemon data from the Pokemon website.
- **Data Transformation:** Cleans and transforms Pokemon data using pandas.
- **Database Loading:** Inserts the cleaned data into a Microsoft SQL Server database using pyodbc.

## Tech Stack
- **Language:**
  - Python

- **Libraries:**
  - **aiohttp** – for asynchronous HTTP requests.
  - **BeautifulSoup** – for scraping and parsing HTML data.
  - **pandas** – for data manipulation and transformation.
  - **pyodbc** – for database connection and data insertion.
- **Database:**
  - Microsoft SQL Server

## Setup and Installation

#### Prerequisites
- Python 3.8+
- Microsoft SQL Server installed and running
- Required Python libraries:

```
pip install aiohttp beautifulsoup4 pandas pyodbc
```

## Clone the Repository

```
git clone https://github.com/Johnmel-Manongdo/Pokemon_Web_Scrape_ETL.git
cd Pokemon_Web_Scrape_ETL
```

## Configuration

Update your database connection details in `load.py`:

```
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=your_server_name;"
    "Database=your_database_name;"
    "Trusted_Connection=yes;"
)
```

## Running the Project

1. **Extract Pokémon Data:** Scrape data from the Pokemon website.

```python extract.py```

  This will generate a CSV file pokemon_data.csv containing the raw data.

2. **Transform and Clean the Data:** Clean and transform the scraped data.

```python transform.py```

  This will generate a cleaned CSV file pokemon_data_cleaned.csv.

3. **Load Data to SQL Server:** Load the transformed data into the SQL Server database.

```python load.py```

## Project Structure

```
├── README.md           # Project documentation
├── extract.py          # Web scraping logic using aiohttp and BeautifulSoup
├── transform.py        # Data cleaning and transformation logic using pandas
├── load.py             # SQL Server loading logic using pyodbc
├── pokemon_data.csv    # Raw scraped data
├── pokemon_data_cleaned.csv  # Cleaned and transformed data
```

## Database Schema

The tbl_pokemon table in your SQL Server database should be structured as follows:

```
CREATE TABLE tbl_pokemon (
    Dex_Number INT,
    Name VARCHAR(255),
    Form VARCHAR(255),
    Types VARCHAR(255),
    Species VARCHAR(255),
    Height_ft DECIMAL(5, 2),
    Weight_kg DECIMAL(5, 2),
    Total INT,
    HP INT,
    Attack INT,
    Defense INT,
    Sp_Atk INT,
    Sp_Def INT,
    Speed INT
);
```

## Future Improvements

- Add error handling for asynchronous tasks and database loading.
- Automate the pipeline to run at scheduled intervals.
- Extend the scraper to gather additional Pokemon data or handle other websites.

## License

This project is licensed under the MIT License.






