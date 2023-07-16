import csv
import matplotlib.pyplot as plt

# Read the Tetracycline1 dataset from a CSV file
with open('tetracycline1.csv', 'r') as file:
    reader = csv.DictReader(file)
    time = []
    concentration = []
    for row in reader:
        time.append(float(row['Time']))
        concentration.append(float(row['Concentration']))

# Create a line plot of tetracycline concentration over time
plt.plot(time, concentration)
plt.xlabel('Time (hours)')
plt.ylabel('Tetracycline Concentration (mg/L)')
plt.title('Tetracycline Absorption Profile')
plt.show()
