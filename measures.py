import tkinter as tk
from tkinter import *
import pandas as pd


class Measures(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Miary statystyczne")
        self.master.geometry("1025x500")

        self.label = tk.Label(self.master, text="Sekcja miar statystycznych", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.label1 = tk.Label(self.master, text='Wybierz atrybut:', font=('Arial', 12))
        self.label1.pack()

        self.columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                        'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
                        'quality']
        self.checkbox_vars_columns = []
        columns_frame = Frame(self.master)
        columns_frame.pack()
        for i, column in enumerate(self.columns):
            var = IntVar()
            checkbox = Checkbutton(columns_frame, text=column, variable=var)
            checkbox.pack(side=LEFT)
            self.checkbox_vars_columns.append((column, var))


        self.label2 = tk.Label(self.master, text='Wybierz miarę:', font=('Arial', 12))
        self.label2.pack()

        self.statistics = ['Średnia arytmetyczna', 'Maksymalna ilość', 'Minimalna ilość', 'Odchylenie standardowe',
                           'Mediana', 'Moda']
        self.checkbox_vars_statistics = []
        statistics_frame = Frame(self.master)
        statistics_frame.pack()
        for i, stat in enumerate(self.statistics):
            var = IntVar()
            checkbox = Checkbutton(statistics_frame, text=stat, variable=var)
            checkbox.pack(side=LEFT)
            self.checkbox_vars_statistics.append((stat, var))


        self.result_label = tk.Label(self.master, text="Wyniki:", font=('Arial', 12))
        self.result_label.pack(pady=10)

        self.result_text = tk.Text(self.master, width=60, height=10)
        self.result_text.pack()

        self.button1 = tk.Button(self.master, text="Oblicz!", font=('Arial', 16), command=self.calculate_statistics)
        self.button1.pack(side=BOTTOM, padx=10, pady=10)


    def calculate_statistics(self):
        # Pobranie wybranych wartości z checkboxów
        selected_columns = [column for column, var in self.checkbox_vars_columns if var.get() == 1]
        selected_statistics = [stat for stat, var in self.checkbox_vars_statistics if var.get() == 1]

        # Wczytanie danych z pliku csv
        df = pd.read_csv('winequality-white .csv', delimiter=';')

        # Obliczenie wybranych statystyk dla wybranych kolumn
        results = []
        for column in selected_columns:
            column_results = []
            for stat in selected_statistics:
                if stat == 'Średnia arytmetyczna':
                    column_results.append(f'Średnia arytmetyczna dla {column}: {df[column].mean()}')
                elif stat == 'Maksymalna ilość':
                    column_results.append(f'Maksymalna ilość dla {column}: {df[column].max()}')
                elif stat == 'Minimalna ilość':
                    column_results.append(f'Minimalna ilość dla {column}: {df[column].min()}')
                elif stat == 'Odchylenie standardowe':
                    column_results.append(f'Odchylenie standardowe dla {column}: {df[column].std()}')
                elif stat == 'Mediana':
                    column_results.append(f'Mediana dla {column}: {df[column].median()}')
                elif stat == 'Moda':
                    column_results.append(f'Moda dla {column}: {df[column].mode().values[0]}')
            results.extend(column_results)

        # Wyświetlenie wyników w oknie tekstowym
        self.result_text.delete(1.0, END)
        for result in results:
            self.result_text.insert(END, result + '\n')
