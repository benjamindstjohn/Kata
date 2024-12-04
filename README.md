# Weather API App

A Python application that allows users to fetch and compare weather data for one or two locations. The app provides temperature, wind speed, coordinates, and a description of the weather. It also provides the differences between the locations when two locations are provided.

## Features

- Fetch weather data for one or two locations.
- Compare weather information (temperature, wind speed, latitude, and longitude).
- Display differences in measurable attributes between two cities.
- Modern and user-friendly graphical interface built with Tkinter.

## Prerequisites

- Python 3.6 or later
- `requests` library (install using `pip install requests`)

## How to Run

1. Clone the repository or download the script.
2. Install dependencies by running:
   ```bash
   pip install requests
   ```
3. Run the script using:
   ```bash
   python weather.py
   ```
4. Enter one or two location names in the input fields.
5. Click **"Get Weather"** to display the results.

## Example Output

### Weather for City 1:
- Temp: 20 °C
- Wind Speed: 3 m/s
- Latitude: 52.52
- Longitude: 13.405
- Description: Clear sky

### Weather for City 2:
- Temp: 25 °C
- Wind Speed: 2 m/s
- Latitude: 48.8566
- Longitude: 2.3522
- Description: Partly cloudy

### Differences:
- Temp Difference: 5 °C
- Wind Difference: 1 m/s
- Latitude Difference: 3.66
- Longitude Difference: 11.0532


---

Developed by Benjamin St John.

