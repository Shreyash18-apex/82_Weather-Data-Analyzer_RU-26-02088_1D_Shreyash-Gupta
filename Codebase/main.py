import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_file():
    while True:
        name = input("Enter CSV file name: ").strip()
        if os.path.isfile(name):
            df = pd.read_csv(name)
            df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d", errors="coerce")
            return df
        print(f"Error: File '{name}' not found. Please enter a valid file name.")


def summary(df):
    temp = df["Temp"].to_numpy(dtype=float)
    avg = np.mean(temp)
    if len(df) == 1:
        print(f"Average Temp: {avg:.2f} C | Max: {np.max(temp):.0f} | "
              f"Min: {np.min(temp):.0f} | Std Dev: {np.std(temp):.2f}")
        return
    imax, imin = np.argmax(temp), np.argmin(temp)
    d_max = df["Date"].iloc[imax].strftime("%Y-%m-%d")
    d_min = df["Date"].iloc[imin].strftime("%Y-%m-%d")
    rain = df["Rainfall"].sum()
    print(f"Average Temp: {avg:.2f} C | Max: {temp[imax]:.0f} ({d_max}) | "
          f"Min: {temp[imin]:.0f} ({d_min}) | Total Rainfall: {rain:.0f} mm")


def clean_and_plot(df):
    before = len(df)
    df = df.drop_duplicates().reset_index(drop=True)
    removed = before - len(df)
    mean_temp = df["Temp"].mean()
    df["Temp"] = df["Temp"].fillna(mean_temp)
    df["Humidity"] = df["Humidity"].fillna(df["Humidity"].mean())
    df["Rainfall"] = df["Rainfall"].fillna(0)

    print(f"Duplicates removed: {removed} | Missing Temp filled with mean: {mean_temp:.2f}")
    print(f"Cleaned rows: {len(df)} | Line chart 'Temperature Trend' displayed")

    plt.figure()
    plt.bar(df["Date"].dt.strftime("%Y-%m-%d"), df["Rainfall"], color="steelblue")
    plt.title("Rainfall per Day")
    plt.xlabel("Date")
    plt.ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.savefig("rainfall_bar.png")
    plt.close()

    plt.figure()
    plt.plot(df["Date"], df["Temp"], marker="o", color="red")
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.xticks(df["Date"], df["Date"].dt.strftime("%Y-%m-%d"), rotation=30)
    plt.tight_layout()
    plt.savefig("temperature_trend.png")
    plt.show()


def main():
    df = load_file()
    while True:
        print("\n===== Weather Data Analyzer =====")
        print("1. Summary")
        print("2. Clean & Plot")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            summary(df.drop_duplicates().reset_index(drop=True)
                    if df["Temp"].notna().all() else df)
        elif choice == "2":
            clean_and_plot(df)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
