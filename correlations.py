import tkinter as tk
import pandas as pd

# funkcja do wyznaczania korelacji
def calculate_correlation():
    # pobranie nazw wybranych cech z pola tekstowego
    feature1 = entry1.get()
    feature2 = entry2.get()

    # wczytanie danych z pliku csv
    df = pd.read_csv('winequality-white .csv', delimiter=';')

    # wyznaczenie korelacji między cechami
    correlation = df[feature1].corr(df[feature2])

    # wyświetlenie wyniku w oknie tekstowym
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f'Korelacja między {feature1} a {feature2}: {correlation:.2f}')

# tworzenie okna
window = tk.Tk()
window.title("Wyznaczanie korelacji pomiędzy dwoma atrybutami.")
window.geometry("800x500")

# etykiety i pola tekstowe
label1 = tk.Label(window, text="Pierwsza cecha:", font=('Arial', 12))
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Druga cecha:", font=('Arial', 12))
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# przycisk do wyznaczania korelacji
button = tk.Button(window, text="Wyznacz korelację",font=('Arial', 13), command=calculate_correlation)
button.pack(pady=10)

# okno tekstowe na wyniki
result_text = tk.Text(window, width=40, height=5)
result_text.pack()

#Informacja o korelacji
label = tk.Label(window, text='Wartość korelacji może przyjmować wartości od -1 do 1, ' )
label.pack()
label2 = tk.Label(window, text='gdzie wartość 1 oznacza pełną korelację dodatnią, -1 pełną korelację ujemną, a 0 brak korelacji.' \
          ' Im bliżej wartości 1 lub -1, tym silniejsza jest korelacja.')
label2.pack()

# pętla zdarzeń
window.mainloop()

