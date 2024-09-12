import pandas as pd

# Function to clean and transform the Pokémon data
def transform_data():
    # Read the CSV file containing raw Pokémon data
    df = pd.read_csv('pokemon_data.csv')

    # Clean the 'Types' column by removing unwanted characters (e.g., square brackets, single quotes)
    df['Types'] = df['Types'].str.replace(r'[\[\]\']', '', regex=True).str.replace(r'\s+', ' ', regex=True).str.strip()
    df['Species'] = df['Species'].str.replace('Pokémon', 'Pokemon', regex=False)
    df.rename(columns={'Height': 'Height_ft'}, inplace=True)
    df['Height_ft'] = df['Height_ft'].str.extract(r"\(([^)]+)\)")
    df['Height_ft'] = df['Height_ft'].str.replace("′", ".").str.replace("″", "")
    df.rename(columns={'Weight': 'Weight_kg'}, inplace=True)
    # Clean the 'Weight_kg' column by removing text within parentheses and the 'kg' unit
    df['Weight_kg'] = df['Weight_kg'].str.replace(r"\s*\([^)]+\)", "", regex=True).str.replace('kg', '')
    df.to_csv('pokemon_data_cleaned.csv', index=False)

if __name__ == "__main__":
    transform_data()
