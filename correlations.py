import tkinter as tk
import pandas as pd


class Correlations(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Wyznaczanie korelacji pomiędzy dwoma atrybutami.")
        self.master.geometry("800x500")

        # etykiety i pola tekstowe
        self.label1 = tk.Label(self.master, text="Pierwsza cecha:", font=('Arial', 12))
        self.label1.pack()
        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label2 = tk.Label(self.master, text="Druga cecha:", font=('Arial', 12))
        self.label2.pack()
        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        # przycisk do wyznaczania korelacji
        self.button = tk.Button(self.master, text="Wyznacz korelację", font=('Arial', 13),
                                command=self.calculate_correlation)
        self.button.pack(pady=10)

        # okno tekstowe na wyniki
        self.result_text = tk.Text(self.master, width=40, height=5)
        self.result_text.pack()

        # Informacja o korelacji
        self.label = tk.Label(self.master, text='Wartość korelacji może przyjmować wartości od -1 do 1, ')
        self.label.pack()
        self.label2 = tk.Label(self.master,
                               text='gdzie wartość 1 oznacza pełną korelację dodatnią, -1 pełną korelację ujemną, a 0 brak korelacji.' \
                                    ' Im bliżej wartości 1 lub -1, tym silniejsza jest korelacja.')
        self.label2.pack()

        self.pack(fill=tk.BOTH, expand=True)  # Dodajemy ramkę do okna głównego aplikacji

    # funkcja do wyznaczania korelacji
    def calculate_correlation(self):
        # pobranie nazw wybranych cech z pola tekstowego
        feature1 = self.entry1.get()
        feature2 = self.entry2.get()

        # wczytanie danych z pliku csv
        df = pd.read_csv('winequality-white .csv', delimiter=';')

        # wyznaczenie korelacji między cechami
        correlation = df[feature1].corr(df[feature2])

        # wyświetlenie wyniku w oknie tekstowym
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f'Korelacja między {feature1} a {feature2}: {correlation:.2f}')



