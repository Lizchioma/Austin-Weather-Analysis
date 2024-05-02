import pandas as pd

# Load the dataset
df = pd.read_csv('data/data_set/austin_weather.csv')

# Check data types
print("Data types before conversion:")
print(df.info())