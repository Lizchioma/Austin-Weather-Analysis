import pandas as pd
import matplotlib.pyplot as plt

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

# Analysis
# Visualize trends in temperature, visibility, and precipitation over time
plt.figure(figsize=(14, 8))

# Temperature
plt.subplot(3, 1, 1)
plt.plot(df['Date'], df['TempAvgF'], color='red')
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.grid(True)

# Visibility
plt.subplot(3, 1, 2)
plt.plot(df['Date'], df['VisibilityAvgMiles'], color='blue')
plt.title('Average Visibility Over Time')
plt.xlabel('Date')
plt.ylabel('Visibility (Miles)')
plt.grid(True)

# Precipitation
plt.subplot(3, 1, 3)
plt.plot(df['Date'], df['PrecipitationSumInches'], color='green')
plt.title('Total Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (Inches)')
plt.grid(True)

plt.tight_layout()
plt.show()