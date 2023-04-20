import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('winequality-white .csv', 'r') as file:

 data = pd.read_csv(file, delimiter=';')

plt.hist(data['quality'], bins=np.arange(3,11)-0.5, rwidth=0.8)
# Wykres histogramu jakości wina
plt.xlabel('Jakość')
plt.ylabel('Częstotliwość')
plt.title('Histogram jakości wina')
plt.show()

# Wykres punktowy dla kwasu winowego i pH
plt.scatter(data['fixed acidity'], data['pH'])
plt.xlabel('Ustalona Kwasowość')
plt.ylabel('pH')
plt.title('Wykres punktowy dla kwasu winowego i pH')

#dodanie linii trendu
x = data['fixed acidity']
y = data['pH']
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red')
plt.show()

#Wykres jakości i ceny
plt.bar(data['price'], data['quality'])
plt.xlabel('Jakość')
plt.ylabel('Cena')
plt.title('Wykres jakości i ceny win')
plt.show()

