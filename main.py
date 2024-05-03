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

# Handle missing values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Data Wrangling
# Impute missing values with the mean of each column
numeric_cols = df.select_dtypes(include=['number']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
df = df.round(2)

# Recheck for missing values after imputation
print("\nMissing values after imputation:")
print(df.isnull().sum())

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Save as CSV
df.to_csv('data/processed_data/clean_data.csv', index=False)