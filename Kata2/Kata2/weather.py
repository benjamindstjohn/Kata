import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_weather():
    city1 = city1_entry.get().strip()
    city2 = city2_entry.get().strip()

    if not city1 and not city2:
        messagebox.showerror("Error", "Please enter at least one city name.")
        return

    api_key = "12b978837cf582884b279fe4eab2c67d"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    data_dict = {}

    # Helper function to fetch weather for a single city
    def get_weather_data(city):
        try:
            res = requests.get(base_url, params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            })
            res.raise_for_status()
            data = res.json()

            if data.get("cod") != 200:
                return None, f"{city}: {data.get('message', 'Unable to fetch data.')}"
            
            return data, None
        except requests.exceptions.RequestException as e:
            return None, f"{city}: Failed to fetch weather data. {e}"

    # Fetch data for the cities
    for city in [city1, city2]:
        if city:
            data, error = get_weather_data(city)
            if data:
                data_dict[city] = {
                    "temp": data["main"]["temp"],
                    "wind_speed": data["wind"]["speed"],
                    "latitude": data["coord"]["lat"],
                    "longitude": data["coord"]["lon"],
                    "description": data["weather"][0]["description"].capitalize(),
                }
            else:
                data_dict[city] = {"error": error}

    # Display results
    if city1 in data_dict:
        if "error" in data_dict[city1]:
            result1.set(f"{city1}\n{data_dict[city1]['error']}")
        else:
            city1_data = data_dict[city1]
            result1.set(
                f"🌡️ Temp: {city1_data['temp']} °C\n"
                f"💨 Wind: {city1_data['wind_speed']} m/s\n"
                f"📍 Lat: {city1_data['latitude']}, Lon: {city1_data['longitude']}\n"
                f"🌤️ Desc: {city1_data['description']}"
            )
    else:
        result1.set("")

    if city2 in data_dict:
        if "error" in data_dict[city2]:
            result2.set(f"{city2}\n{data_dict[city2]['error']}")
        else:
            city2_data = data_dict[city2]
            result2.set(
                f"🌡️ Temp: {city2_data['temp']} °C\n"
                f"💨 Wind: {city2_data['wind_speed']} m/s\n"
                f"📍 Lat: {city2_data['latitude']}, Lon: {city2_data['longitude']}\n"
                f"🌤️ Desc: {city2_data['description']}"
            )
    else:
        result2.set("")

    # Calculate and display differences if both cities have data
    if city1 in data_dict and city2 in data_dict and "error" not in data_dict[city1] and "error" not in data_dict[city2]:
        city1_data = data_dict[city1]
        city2_data = data_dict[city2]

        temp_diff = abs(city1_data["temp"] - city2_data["temp"])
        wind_diff = abs(city1_data["wind_speed"] - city2_data["wind_speed"])
        lat_diff = abs(city1_data["latitude"] - city2_data["latitude"])
        lon_diff = abs(city1_data["longitude"] - city2_data["longitude"])

        differences.set(
            f"🌡️ Temp Difference: {temp_diff:.2f} °C\n"
            f"💨 Wind Difference: {wind_diff:.2f} m/s\n"
            f"📍 Latitude Difference: {lat_diff:.2f}\n"
            f"📍 Longitude Difference: {lon_diff:.2f}"
        )
    else:
        differences.set("")

# Create the main window
root = tk.Tk()
root.title("Weather Comparison App")
root.geometry("600x500")
root.resizable(False, False)

# Add modern fonts
FONT_HEADING = ("Arial", 16, "bold")
FONT_TEXT = ("Arial", 12)

# Style configuration for ttk
style = ttk.Style(root)
style.configure("TLabel", font=FONT_TEXT, padding=5)
style.configure("TEntry", font=FONT_TEXT)
style.configure("TButton", font=("Arial", 12, "bold"), padding=5)

# App heading
heading_label = ttk.Label(root, text="Weather App", font=FONT_HEADING, anchor="center")
heading_label.pack(pady=(10, 20))

# Input Frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=(10, 10), padx=20, fill="x")

# City 1 input
city1_label = ttk.Label(input_frame, text="Location 1:")
city1_label.grid(row=0, column=0, padx=5, pady=5)
city1_entry = ttk.Entry(input_frame, width=25)
city1_entry.grid(row=0, column=1, padx=5, pady=5)

# City 2 input
city2_label = ttk.Label(input_frame, text="Location 2:")
city2_label.grid(row=1, column=0, padx=5, pady=5)
city2_entry = ttk.Entry(input_frame, width=25)
city2_entry.grid(row=1, column=1, padx=5, pady=5)

# Fetch weather button
fetch_button = ttk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack(pady=15)

# Results Frame
result_frame = ttk.Frame(root)
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Result 1
result1 = tk.StringVar()
result1_label = ttk.LabelFrame(result_frame, text="Location 1 Details", labelanchor="n", padding=(10, 10))
result1_label.pack(side="left", fill="both", expand=True, padx=5)
result1_display = ttk.Label(result1_label, textvariable=result1, justify="left", anchor="w")
result1_display.pack(anchor="nw", fill="x", expand=True)

# Result 2
result2 = tk.StringVar()
result2_label = ttk.LabelFrame(result_frame, text="Location 2 Details", labelanchor="n", padding=(10, 10))
result2_label.pack(side="left", fill="both", expand=True, padx=5)
result2_display = ttk.Label(result2_label, textvariable=result2, justify="left", anchor="w")
result2_display.pack(anchor="nw", fill="x", expand=True)

# Differences Frame
differences = tk.StringVar()
differences_label = ttk.LabelFrame(root, text="Differences", labelanchor="n", padding=(10, 10))
differences_label.pack(pady=10, padx=20, fill="both", expand=True)
differences_display = ttk.Label(differences_label, textvariable=differences, justify="left", anchor="w")
differences_display.pack(anchor="nw", fill="x", expand=True)

# Run the application
root.mainloop()