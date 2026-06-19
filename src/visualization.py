import matplotlib.pyplot as plt

def plot_water_balance(timestamps, soil_moisture, rainfall, title="Soil Moisture Trends"):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    ax1.plot(timestamps, soil_moisture, color='green', label='Soil Moisture %')
    ax1.set_ylabel('Moisture %', color='green')
    
    ax2 = ax1.twinx()
    ax2.bar(timestamps, rainfall, alpha=0.3, color='blue', label='Rainfall mm')
    ax2.set_ylabel('Rainfall mm', color='blue')
    
    plt.title(title)
    fig.tight_layout()
    return fig

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_evapotranspiration(df):
    """
    Create a 3D scatter plot of evapotranspiration vs weather variables.
    Accepts either raw or aggregated column names.
    """
    # Handle both raw and cleaned column names
    temp_col = 'temp_c' if 'temp_c' in df.columns else 'temp_sht'
    hum_col = 'humidity_pct' if 'humidity_pct' in df.columns else 'humidity_sht'
    wind_col = 'wind_speed_mps' if 'wind_speed_mps' in df.columns else 'wind_spd'
    et_col = 'et_mm' if 'et_mm' in df.columns else 'et'

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(
        df[temp_col],
        df[hum_col],
        df[et_col],
        c=df[wind_col],
        cmap='viridis',
        s=40,
        alpha=0.8
    )

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Humidity (%)")
    ax.set_zlabel("Evapotranspiration (mm/day)")
    ax.set_title("3D Evapotranspiration Visualization")

    return fig, ax
