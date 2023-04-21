import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pandas as pd

window = tk.Tk()
window.title("Miary statystyczne")
window.geometry("800x500")

label = tk.Label(window, text="Sekcja miar statystycznych", font=('Arial', 18))
label.pack(padx=20, pady=20)

l2 = Label(window, text='Wybierz współczynnik', font=('Arial', 12))
l2.pack()
combobox1 = Combobox(window, values=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                                     'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality'])
combobox1.pack()

l1 = Label(window, text='Wybierz miarę', font=('Arial', 12))
l1.pack()
combobox2 = Combobox(window, values=['Średnia arytmetyczna', 'Maksymalna ilość', 'Minimalna ilość',
                                     'Odchylenie standardowe', 'Mediana', 'Moda'])
combobox2.pack()

result_label = Label(window, text="Wyniki:", font=('Arial', 12))
result_label.pack(pady=10)

result_text = Text(window, width=60, height=10)
result_text.pack()

def calculate_statistics():
    # Pobranie wybranych wartości z comboboxów
    column_name = combobox1.get()
    stat_name = combobox2.get()

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
    result_text.delete(1.0, END)
    result_text.insert(END, f'{stat_name} dla {column_name}: {result}')

button = tk.Button(window, text="Oblicz!", font=('Arial',16), command=calculate_statistics)
button.pack(side=BOTTOM, padx=10, pady=10)

window.mainloop()
