
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd  # For geographic analysis
from mpl_toolkits.basemap import Basemap  # For mapping

# Load datasets 
df1 = pd.read_csv('data/benin-malanville.csv') 
df2 = pd.read_csv('data/sierraleone-bumbuna.csv')
df3 = pd.read_csv('data/togo-dapaong_qc.csv')

# Combine datasets if they have similar structures
df = pd.concat([df1, df2, df3], ignore_index=True)

# Overview of the data
def overview(data):
    print(data.head())
    print(data.info())
    print(data.describe())

overview(df)

# Data Quality Check
def data_quality_check(data):
    # Convert relevant columns to numeric
    numeric_columns = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'RH', 'WS', 'WSgust']  # Update with your actual numeric column names
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')  # Convert to numeric, coercing errors to NaN

    # Select only numeric columns for quality check
    numeric_data = data.select_dtypes(include=[np.number])
    
    print("Missing values:\n", data.isnull().sum())
    negative_values = numeric_data[numeric_data < 0].dropna(how='all')  # Drop rows where all values are NaN
    print("Negative values:\n", negative_values)

data_quality_check(df)

# Time Series Analysis
def time_series_analysis(data):
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    data.set_index('Timestamp', inplace=True)
    
    daily_data = data.resample('D').mean()
    
    plt.figure(figsize=(14, 7))
    plt.plot(daily_data['GHI'], label='GHI')
    plt.plot(daily_data['DNI'], label='DNI')
    plt.plot(daily_data['DHI'], label='DHI')
    plt.title('Daily Average Solar Radiation')
    plt.xlabel('Date')
    plt.ylabel('Irradiance (W/m²)')
    plt.legend()
    plt.show()

time_series_analysis(df)

# Analyze Environmental Influences
def environmental_analysis(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='RH', y='Tamb', data=data)
    plt.title('Relative Humidity vs. Ambient Temperature')
    plt.xlabel('Relative Humidity (%)')
    plt.ylabel('Ambient Temperature (°C)')
    plt.show()

environmental_analysis(df)

# Identify High-Potential Regions
'''def high_potential_regions(data):
    # Assuming you have a column for geographical coordinates (latitude and longitude)
    plt.figure(figsize=(10, 8))
    plt.scatter(data['Longitude'], data['Latitude'], c=data['GHI'], cmap='viridis', alpha=0.5)
    plt.colorbar(label='GHI (W/m²)')
    plt.title('Geographic Distribution of Solar Radiation')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()

#high_potential_regions(df)
'''
# Correlation Analysis
def correlation_analysis(data):
    correlation_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'RH', 'WS', 'WSgust']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix of Solar Radiation and Other Variables')
    plt.show()

correlation_analysis(df)

# Final Report Generation 
def final_report(data):
    with open('reports/final_report.md', 'w') as f:
        f.write("# Final EDA Report\n")
        f.write("## Summary of Findings\n")
        # Add findings and recommendations here
        f.write("## Recommendations\n")
        # Add your recommendations here

final_report(df)

#  Save plots as images for the report
def save_plots():
    plt.savefig('reports/solar_radiation_trends.png')
    plt.savefig('reports/environmental_analysis.png')
    plt.savefig('reports/geographic_distribution.png')

save_plots()