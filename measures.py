import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd

class Measures(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Miary statystyczne")
        self.master.geometry("800x500")

        self.label = tk.Label(self.master, text="Sekcja miar statystycznych", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.l2 = Label(self.master, text='Wybierz współczynnik', font=('Arial', 12))
        self.l2.pack()
        self.combobox1 = Combobox(self.master, values=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                                     'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality'])
        self.combobox1.pack()

        self.l1 = Label(self.master, text='Wybierz miarę', font=('Arial', 12))
        self.l1.pack()
        self.combobox2 = Combobox(self.master, values=['Średnia arytmetyczna', 'Maksymalna ilość', 'Minimalna ilość',
                                     'Odchylenie standardowe', 'Mediana', 'Moda'])
        self.combobox2.pack()

        self.result_label = Label(self.master, text="Wyniki:", font=('Arial', 12))
        self.result_label.pack(pady=10)

        self.result_text = Text(self.master, width=60, height=10)
        self.result_text.pack()


        self.button1 = tk.Button(self, text="Oblicz!", font=('Arial',16), command=calculate_statistics)
        self.button1.pack(side=BOTTOM, padx=10, pady=10)


def calculate_statistics(self):
    # Pobranie wybranych wartości z comboboxów
    column_name = self.combobox1.get()
    stat_name = self.combobox2.get()

    # Wczytanie danych z pliku csv
    df = pd.read_csv('winequality-white .csv', delimiter=';')

    # Obliczenie wybranej statystyki dla wybranej kolumny
    if stat_name == 'Średnia arytmetyczna':
        result = df[column_name].mean()
    elif stat_name == 'Maksymalna ilość':
        result = df[column_name].max()
    elif stat_name == 'Minimalna ilość':
        result = df[column_name].min()
    elif stat_name == 'Odchylenie standardowe':
        result = df[column_name].std()
    elif stat_name == 'Mediana':
        result = df[column_name].median()
    elif stat_name == 'Moda':
        result = df[column_name].mode().values[0]
    else:
        result = 'Nieznana miara'

    # Wyświetlenie wyników w oknie tekstowym
    self.result_text.delete(1.0, END)
    self.result_text.insert(END, f'{stat_name} dla {column_name}: {result}')



