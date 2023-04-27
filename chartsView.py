import tkinter as tk
from tkinter import ttk

import pandas as pd
from matplotlib import pyplot as plt

import charts


class ChartsView(tk.Frame):
    def __init__(self, data_file):
        self.data_file = data_file
        tk.Frame.__init__(self)
        self.list1_options = ["Wybierz parametry", "Kwasowość stała", "Kwasowość lotna", "Kwas cytrynowy",
                              "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem",
                              "gęstość", "pH", "siarczany", "alkohol", "jakość", "quality"]
        self.list2_options = ["Wybierz parametry", "Kwasowość stała", "Kwasowość lotna", "Kwas cytrynowy",
                              "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem",
                              "gęstość", "pH", "siarczany", "alkohol", "jakość", "chlorides"]
        self.list3_options = ["Wybierz parametry", "Wykres liniowy", "Wykres słupkowy", "Wykres kołowy",
                              "Wykres punktowy", "Wykres pudełkowy"]

        self.list1_var = tk.StringVar()
        self.list1_var.set("Select Option")

        self.list2_var = tk.StringVar()
        self.list2_var.set("Select Option")

        self.list3_var = tk.StringVar()
        self.list3_var.set("Select Option")

        self.list1 = ttk.OptionMenu(self, self.list1_var, *self.list1_options)
        self.list1.pack(padx=50, pady=10, side=tk.LEFT)

        self.list2 = ttk.OptionMenu(self, self.list2_var, *self.list2_options)
        self.list2.pack(padx=50, pady=10, side=tk.LEFT)

        self.list3 = ttk.OptionMenu(self, self.list3_var, *self.list3_options)
        self.list3.pack(padx=50, pady=10, side=tk.LEFT)

        self.buttonGeneruj = tk.Button(self, text="Generuj wykres", font=('Arial', 12), command=charts.ChartGenerator)
        self.buttonGeneruj.pack(padx=10, pady=10, side=tk.LEFT)

        self.pack(fill=tk.BOTH, expand=True)




