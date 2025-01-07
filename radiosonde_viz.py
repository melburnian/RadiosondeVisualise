import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# Load JSON data from file
try:
    with open('ts.json', 'r') as file:
        json_data = json.load(file)
    print("JSON data loaded successfully.")
except json.JSONDecodeError:
    print("Error: The file 'ts.json' is empty or contains invalid JSON.")
    exit(1)

# Check if 'features' key exists in the JSON
if 'features' not in json_data:
    print("Error: The JSON file does not contain the 'features' key.")
    exit(1)

# Convert JSON data (features -> properties) to a DataFrame
features = json_data['features']
properties = [feature['properties'] for feature in features]
df = pd.DataFrame(properties)
print("DataFrame created successfully.")

# Calculate additional fields
df['height_km'] = df['gpheight'] / 1000
df['wind_speed_kmh'] = np.sqrt(df['wind_u'] ** 2 + df['wind_v'] ** 2) * 3.6
df['temp_celsius'] = df['temp'] - 273.15
df['humidity'] = 100 * (np.exp((17.625 * df['dewpoint']) / (243.04 + df['dewpoint'])) /
                        np.exp((17.625 * df['temp']) / (243.04 + df['temp'])))
print("Additional fields calculated successfully.")

# Plot the data
fig, ax1 = plt.subplots()

# Temperature plot
ax1.set_xlabel('Height (km)')
ax1.set_ylabel('Temperature (°C)', color='tab:red')
ax1.plot(df['height_km'], df['temp_celsius'], color='tab:red', label='Temperature (°C)')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.grid(True)
ax1.set_yticks(np.arange(int(df['temp_celsius'].min() // 10 * 10), int(df['temp_celsius'].max() // 10 * 10) + 10, 10))

# Wind speed plot on second axis
ax2 = ax1.twinx()
ax2.set_ylabel('Wind Speed (km/h)', color='tab:blue')
ax2.plot(df['height_km'], df['wind_speed_kmh'], color='tab:blue', label='Wind Speed (km/h)')
ax2.tick_params(axis='y', labelcolor='tab:blue')

fig.tight_layout(rect=[0, 0, 1, 0.95])
plt.title('Weather Balloon Data')
plt.show()
print("Plot displayed successfully.")
