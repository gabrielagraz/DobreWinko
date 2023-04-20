import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Charts:

 def __init__(self, data_file):
  self.data_file = data_file

def generate_quality_histogram(self):
 with open(self.data_file, 'r') as file:
  data = pd.read_csv(file, delimiter=';')
 plt.hist(data['quality'], bins=np.arange(3,11)-0.5, rwidth=0.8)
# Wykres histogramu jakości wina
 plt.xlabel('Jakość')
 plt.ylabel('Częstotliwość')
 plt.title('Histogram jakości wina')
 return plt

# Wykres punktowy dla kwasu winowego i pH
def generate_acidity_pH_scatter(self):
 with open(self.data_file, 'r') as file:
  data = pd.read_csv(file, delimiter=';')
 plt.scatter(data['fixed acidity'], data['pH'])
 plt.xlabel('Ustalona Kwasowość')
 plt.ylabel('pH')
 plt.title('Wykres punktowy dla kwasu winowego i pH')
#dodanie linii trendu
 x = data['fixed acidity']
 y = data['pH']
 m, b = np.polyfit(x, y,1)
 plt.plot(x, m*x + b, color='red')
 return plt

#Wykres jakości i ceny
def generate_quality_price_bar(self):
 with open(self.data_file, 'r') as file:
  data = pd.read_csv(file, delimiter=';')
 plt.bar(data['chlorides'], data['quality'])
 plt.xlabel('Jakość')
 plt.ylabel('Cena')
 plt.title('Wykres jakości i ceny win')
 return plt

