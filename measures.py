# import pandas as pd
#
# # Wczytanie danych z pliku CSV
# data = pd.read_csv('winequality-white .csv', delimiter=';')
#
# # Obliczenie średniej zawartości alkoholu
# mean_alcohol = data['alcohol'].mean()
#
# # Wyświetlenie wyniku
# print('Średnia zawartość alkoholu:', mean_alcohol)


import tkinter
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

window=tkinter.Tk()
window.title("Miary statystyczne")
window.geometry("800x500")

label = tk.Label(window, text="Sekcja miar statystycznych", font=('Arial',18))
label.pack(padx=20, pady=20)

l2=Label(window,text='Wybierz współczynnik', font=('Arial',12))
l2.pack()
combobox=Combobox(window, values=['Kwasowość stała', "Kwasowość lotna", "Kwas cytrynowy", "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem", "gęstość", "pH", "siarczany", 'alkohol', 'jakość'])
combobox.pack()

l1=Label(window,text='Wybierz miarę', font=('Arial',12))
l1.pack()
combobox=Combobox(window, values=['Średnia arytmetyczna', 'Maksymalna ilość', 'Minimalna ilość', 'Odchylenie standardowe', 'Mediana', 'Moda'])
combobox.pack()

result_label = Label(window, text="Wyniki:", font=('Arial', 12))
result_label.pack(pady=10)

result_text = Text(window, width=60, height=10)
result_text.pack()

button = tk.Button(window, text="Oblicz!", font=('Arial',16))
button.pack(side=BOTTOM, padx=10, pady=10)


window.mainloop()
