import pandas as pd

# Load the dataset
df = pd.read_csv('data/data_set/austin_weather.csv')

# Check data types
print("Data types before conversion:")
print(df.info())

# Data Cleaning
# Handle non-numeric values and convert columns to numeric
numeric_cols = ['DewPointHighF', 'DewPointAvgF', 'DewPointLowF',
                'HumidityHighPercent', 'HumidityAvgPercent', 'HumidityLowPercent',
                'SeaLevelPressureHighInches', 'SeaLevelPressureAvgInches', 'SeaLevelPressureLowInches',
                'VisibilityHighMiles', 'VisibilityAvgMiles', 'VisibilityLowMiles',
                'WindHighMPH', 'WindAvgMPH', 'WindGustMPH', 'PrecipitationSumInches']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

    # Check data types again after conversion
print("\nData types after conversion:")
print(df.info())