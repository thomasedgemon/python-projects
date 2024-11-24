from datetime import datetime
import requests
import tkinter as tk

def calculate_dollars_per_hour():
    try:
        # Get the current date and calculate the time difference
        current_date = datetime.now()
        time_difference = target_date - current_date
        hours_until_target = time_difference.total_seconds() / 3600

        # Make a GET request to the CoinGecko API
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the JSON response and extract Bitcoin price
        data = response.json()
        bitcoin_price = int(data['bitcoin']['usd'])

        # Calculate the needed dollars per hour
        btc_difference = btc_goal - bitcoin_price
        dollars_per_hour = btc_difference / hours_until_target

        # Update the label text
        result_label.config(text=f"Dollars per hour needed: {dollars_per_hour:.2f}")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error fetching data: {e}")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

# Define target date and goal
target_date = datetime(2024, 11, 29, 23, 59)  # Example target date
btc_goal = 100000

# CoinGecko API endpoint
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Create the Tkinter window
root = tk.Tk()
root.title("Dollars Per Hour Calculator")

# Create a label to display the result
result_label = tk.Label(root, text="Click 'Refresh' to calculate", font=("Arial", 14))
result_label.pack(pady=20)

# Create a refresh button
refresh_button = tk.Button(root, text="Refresh", command=calculate_dollars_per_hour, font=("Arial", 14))
refresh_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
