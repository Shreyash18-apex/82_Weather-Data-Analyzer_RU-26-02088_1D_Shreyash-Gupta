import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load CSV file
try:
    data = pd.read_csv("weather.csv")

except FileNotFoundError:
    print("Error: weather.csv file not found!")
    exit()
    
# Display original data
print("Original Weather Data")  
print(data)

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

#Remove duplicate records
data = data.drop_duplicates()

#Fill missing temperature with average
average_temp = data["Temp"].mean()
data["Temp"] = data["Temp"].fillna(data["Temp"].mean())

#Display cleaned data
print("\nCleaned Weather Data:")
print(data)

# Calculate temperature statistics

temp = data["Temp"]

average = np.mean(temp)
maximum = np.max(temp)
minimum = np.min(temp)
std_dev = np.std(temp)

# Calculate total rainfall
rainfall = np.sum(data["Rainfall"])

print("\nWeather Summary")
print("Average Temperature:", average)
print("Maximum Temperature:", maximum)
print("Minimum Temperature:", minimum)
print("Standard Deviation:", std_dev)
print("Total Rainfall:", rainfall)

# Temperature Line Graph

plt.plot(data["Date"], data["Temp"], marker="o")

plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Rainfall Bar Graph

plt.bar(data["Date"], data["Rainfall"])

plt.title("Rainfall Report")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Menu Driven Program

while True:

    print("\n===== WEATHER DATA ANALYZER =====")
    print("1. Display Weather Data")
    print("2. Display Weather Summary")
    print("3. Show Temperature Graph")
    print("4. Show Rainfall Graph")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(data)

    elif choice == "2":
        print("\nWeather Summary")
        print("Average Temperature:", average)
        print("Maximum Temperature:", maximum)
        print("Minimum Temperature:", minimum)
        print("Standard Deviation:", std_dev)
        print("Total Rainfall:", rainfall)

    elif choice == "3":
        plt.plot(data["Date"], data["Temp"], marker="o")
        plt.title("Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif choice == "4":
        plt.bar(data["Date"], data["Rainfall"])
        plt.title("Rainfall Report")
        plt.xlabel("Date")
        plt.ylabel("Rainfall (mm)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif choice == "5":
        print("Thank you for using Weather Data Analyzer!")
        break

    else:
        print("Invalid choice! Please try again.")
