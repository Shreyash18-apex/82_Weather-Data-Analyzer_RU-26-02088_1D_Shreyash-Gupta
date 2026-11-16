import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_file():
    # keep asking until a valid file name is given
    while True:
        filename = input("Enter CSV file name: ")
        if os.path.exists(filename):
            break
        print("Error: File '" + filename + "' not found. Please enter a valid file name.")

    data = pd.read_csv(filename)
    data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
    return data


def show_summary(data):
    # use NumPy for calculations
    temp = np.array(data["Temp"])
    average = np.mean(temp)
    highest = np.max(temp)
    lowest = np.min(temp)
    std = np.std(temp)

    if len(data) == 1:
        # only one row of data
        print("Average Temp: %.2f C | Max: %d | Min: %d | Std Dev: %.2f"
              % (average, highest, lowest, std))
    else:
        hot_day = data["Date"][np.argmax(temp)].strftime("%Y-%m-%d")
        cold_day = data["Date"][np.argmin(temp)].strftime("%Y-%m-%d")
        rain = np.sum(data["Rainfall"])
        print("Average Temp: %.2f C | Max: %d (%s) | Min: %d (%s) | Total Rainfall: %d mm"
              % (average, highest, hot_day, lowest, cold_day, rain))


def clean_and_plot(data):
    # step 1: remove duplicate rows
    rows_before = len(data)
    data = data.drop_duplicates()
    data = data.reset_index(drop=True)
    removed = rows_before - len(data)

    # step 2: fill missing Temp with the mean
    mean_temp = data["Temp"].mean()
    data["Temp"] = data["Temp"].fillna(mean_temp)

    print("Duplicates removed: %d | Missing Temp filled with mean: %.2f" % (removed, mean_temp))
    print("Cleaned rows: %d | Line chart 'Temperature Trend' displayed" % len(data))

    # bar chart (rainfall) - saved as image
    plt.figure()
    plt.bar(data["Date"].dt.strftime("%Y-%m-%d"), data["Rainfall"])
    plt.title("Rainfall per Day")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.savefig("rainfall_bar.png")
    plt.close()

    # line chart (temperature) - saved and shown
    plt.figure()
    plt.plot(data["Date"], data["Temp"], marker="o")
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("temperature_trend.png")
    plt.show()


def main():
    data = load_file()

    while True:
        print()
        print("===== Weather Data Analyzer =====")
        print("1. Summary")
        print("2. Clean & Plot")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_summary(data)
        elif choice == "2":
            clean_and_plot(data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


main()
