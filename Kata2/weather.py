import requests
import tkinter as tk
from tkinter import ttk, messagebox

def fetch_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    api_key = "12b978837cf582884b279fe4eab2c67d"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "Unable to fetch data."))
            return

        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        description = data['weather'][0]['description']

        result.set(f"🌡️ Temperature: {temp} °C\n"
                   f"💨 Wind Speed: {wind_speed} m/s\n"
                   f"📍 Latitude: {latitude}\n"
                   f"📍 Longitude: {longitude}\n"
                   f"🌤️ Description: {description.capitalize()}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data.\n{e}")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("450x350")
root.resizable(False, False)

# Add a modern font
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

# City input
city_frame = ttk.Frame(root)
city_frame.pack(pady=(10, 10), padx=20, fill="x")

city_label = ttk.Label(city_frame, text="Enter your city:", anchor="w")
city_label.pack(side="left")

city_entry = ttk.Entry(city_frame, width=30)
city_entry.pack(side="left", padx=10, expand=True, fill="x")

# Fetch weather button
fetch_button = ttk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack(pady=15)

# Weather result
result_frame = ttk.LabelFrame(root, text="Weather Details", labelanchor="n", padding=(10, 10))
result_frame.pack(pady=10, padx=20, fill="both", expand=True)

result = tk.StringVar()
result_label = ttk.Label(result_frame, textvariable=result, justify="left", anchor="w", padding=5)
result_label.pack(anchor="nw", fill="x", expand=True)

# Run the application
root.mainloop()