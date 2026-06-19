import pandas as pd
import numpy as np

def load_and_standardize_weather(filepath):
    """
    Loads raw weather data and maps specific sensor headers to project variables.
    Handles missing values (NA, blanks) as instructed.
    """
    df = pd.read_csv(filepath, na_values=["NA", "", "NaN"])
    
    # Mapping based on your provided raw sensor headers
    mapping = {
        'ts': 'timestamp',
        'rg1': 'rainfall_mm',
        'temp_sht': 'temperature_c',
        'humidity_sht': 'humidity_pct',
        'si1145_uv': 'solar_index',
        'wind_spd': 'wind_speed_mps'
    }
    
    df = df.rename(columns=mapping)
    
    # Clean anomalies: e.g., temperature above 50C or humidity above 100
    df.loc[df['temperature_c'] > 50, 'temperature_c'] = np.nan
    df.loc[df['humidity_pct'] > 100, 'humidity_pct'] = 100
    
    # Fill missing values with forward fill or median for stability
    df = df.ffill()
    return df

def clean_soil_data(filepath):
    """Loads and cleans soil moisture sensor data."""
    df = pd.read_csv(filepath, na_values=["NA", ""])
    df['soil_moisture_pct'] = df['soil_moisture_pct'].clip(0, 100)
    df = df.dropna(subset=['soil_moisture_pct'])
    return df

# reusable function to aggregate weather data to daily level
def aggregate_daily_weather(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure timestamp column exists
    if 'ts' not in df.columns:
        raise KeyError("Expected column 'ts' not found in DataFrame")

    # Convert to datetime
    df['timestamp'] = pd.to_datetime(df['ts'])

    # Group by date and aggregate
    daily = (
        df.groupby(df['timestamp'].dt.date)
          .agg({
              'rg1': 'sum',          # total rainfall
              'temp_sht': 'mean',    # average temperature
              'humidity_sht': 'mean',
              'wind_spd': 'mean',
              'si1145_uv': 'max'     # peak solar intensity
          })
          .reset_index()
    )

    # Rename columns for clarity
    daily.columns = [
        'date', 'rainfall_mm', 'temp_c',
        'humidity_pct', 'wind_speed_mps', 'solar_index'
    ]

    return daily
