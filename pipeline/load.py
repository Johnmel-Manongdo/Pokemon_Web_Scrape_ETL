import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv(r"pokemon_data_cleaned.csv")
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=Johnmel\SQLEXPRESS;"
    "Database=pokemon_db;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()
sql_query =  """
        INSERT INTO tbl_pokemon (Dex_Number, Name, Form, Types, Species, Height_ft, Weight_kg, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Insert DataFrame to existing table
for row in df.itertuples():
    cursor.execute(
        sql_query,
        row.Dex_Number,
        row.Name,
        row.Form,
        row.Types,
        row.Species,
        row.Height_ft,
        row.Weight_kg,
        row.Total,
        row.HP,
        row.Attack,
        row.Defense,
        row.Sp_Atk,
        row.Sp_Def,
        row.Speed,
    )

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()
