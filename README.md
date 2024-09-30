# Pokemon Web Scraping, Data Cleaning, and SQL Server Loading

This project involves scraping data from a Pokemon website (https://pokemondb.net/), cleaning and transforming the data, and loading it into a Microsoft SQL Server database. The pipeline is implemented in Python, utilizing asynchronous web scraping, data transformation, and database operations.

## Sample Data

```
  Dex_Number        Name              Form          Types              Species  Height_ft Weight_kg  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed
0           1   Bulbasaur               NaN  Grass, Poison         Seed Pokemon       2.04      6.9     318  45      49       49      65      65     45
1           2     Ivysaur               NaN  Grass, Poison         Seed Pokemon       3.03     13.0     405  60      62       63      80      80     60
2           3    Venusaur               NaN  Grass, Poison         Seed Pokemon       6.07    100.0     525  80      82       83     100     100     80
3           3    Venusaur     Mega Venusaur  Grass, Poison         Seed Pokemon       6.07    100.0     625  80     100      123     122     120     80
4           4  Charmander               NaN           Fire       Lizard Pokemon       2.00      8.5     309  39      52       43      60      50     65
5           5  Charmeleon               NaN           Fire        Flame Pokemon       3.07     19.0     405  58      64       58      80      65     80
6           6   Charizard               NaN   Fire, Flying        Flame Pokemon       5.07     90.5     534  78      84       78     109      85    100
7           6   Charizard  Mega Charizard X   Fire, Dragon        Flame Pokemon       5.07     90.5     634  78     130      111     130      85    100
8           6   Charizard  Mega Charizard Y   Fire, Flying        Flame Pokemon       5.07     90.5     634  78     104       78     159     115    100
9           7    Squirtle               NaN          Water  Tiny Turtle Pokemon       1.08      9.0     314  44      48       65      50      64     43
```

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
  - aiohttp
  - beautifulsoup4
  - pandas
  - pyodbc

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





