# Weather Balloon Data Analysis

This project processes and visualises weather balloon (radiosonde) data from a JSON file. The data includes measurements such as height, temperature, wind speed, and dewpoint, collected by weather balloons as they ascend through the atmosphere. This script extracts, processes, and plots the data for easy analysis.

## Overview

This Python script performs the following tasks:

1. **Load JSON data**: It reads the weather balloon data from a `ts.json` file, which follows a GeoJSON format. 
2. **Process data**: It calculates useful metrics such as:
   - Temperature in Celsius (`temp_celsius`).
   - Wind speed in kilometres per hour (`wind_speed_kmh`), computed using the u and v components of the wind.
   - Humidity (`humidity`) is based on temperature and dewpoint using the Magnus formula.
3. **Visualise data**: The script generates a dual-axis plot:
   - The left y-axis shows the temperature (°C).
   - The right y-axis shows the wind speed (km/h).
   - The x-axis represents the altitude (in kilometres).

## Prerequisites

To run this script, you need to have Python installed along with the following packages:
* [Pandas](https://pypi.org/project/pandas/)
* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org)

```bash
pip install pandas numpy matplotlib
```

## How to Run
	1.	Clone or download this repository.
	2.	Make sure the ts.json file containing the weather balloon data is in the same directory as the script.
	3.	Run the script with Python:
 
```bash
python weather_balloon.py
```

This will load the data, calculate additional fields, and generate a temperature and wind speed plot vs. height.

## Example JSON Structure

The JSON file (ts.json) should have a structure similar to the following:
```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "gpheight": 1000,
        "temp": 273.15,
        "dewpoint": 270.15,
        "wind_u": 5.0,
        "wind_v": -2.0
      },
      "geometry": {
        "type": "Point",
        "coordinates": [longitude, latitude, altitude]
      }
    },
    ...
  ]
}
```
## Output

The script will generate a plot with:

	•	Temperature (°C) vs. Height (km) on the left y-axis.
	•	Wind speed (km/h) vs. Height (km) on the right y-axis.

## Common Troubleshooting Steps

1. **File Not Found**

If the ts.json file is missing or in the wrong directory, you may get a “file not found” error. Ensure the ts.json file is in the same directory as the Python script.

2. **Invalid JSON Format**

If you encounter a JSONDecodeError, the ts.json file is either empty or contains malformed JSON. Double-check the structure of your JSON file to ensure it follows the expected GeoJSON format.

3. **KeyError: ‘features’**

This error occurs when the script cannot find the features key in your JSON file. Ensure your JSON data uses the correct structure with relevant weather data features.

4. **FAW: Feature Attribute Warnings**

	•	Missing Attributes: If specific weather attributes such as gpheight, temp, dewpoint, or wind_u/wind_v are missing from your data, the script cannot compute values like temperature, wind speed, or humidity.
	•	Incorrect Data Types: Ensure that the values in your JSON file are correctly formatted (e.g., numbers for gpheight, temp, etc.).

5. **Plot Not Showing**

If the plot does not display after running the script, it could be because the matplotlib GUI backend isn’t configured correctly. Ensure you run the script in an environment that supports graphical displays, such as Jupyter Notebook or a local Python environment with GUI support.

