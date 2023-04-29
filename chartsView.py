import tkinter as tk
from tkinter import ttk

import pandas as pd
from matplotlib import pyplot as plt


class ChartsView(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self)
        self.list1_options = ["Wybierz parametry", "fixed acidity", 'volatile acidity', 'citric acid', 'residual sugar',
                              'chlorides',
                              'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates',
                              'alcohol', 'quality']
        self.list2_options = ["Wybierz parametry", 'fixed acidity', "volatile acidity", 'citric acid', 'residual sugar',
                              'chlorides',
                              'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates',
                              'alcohol', 'quality']
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

        self.buttonGeneruj = tk.Button(self, text="Generuj wykres", font=('Arial', 12),
                                       command=self.generate_chart)
        self.buttonGeneruj.pack(padx=10, pady=10, side=tk.LEFT)

        self.pack(fill=tk.BOTH, expand=True)

    data_file = "winequality-white .csv"

    def generate_chart(self):
        chart_type = self.list3_var.get()
        if chart_type == "Wykres liniowy":
            self.generate_line_chart()
        elif chart_type == "Wykres słupkowy":
            self.generate_bar_chart()
        elif chart_type == "Wykres kołowy":
            self.generate_pie_chart()
        elif chart_type == "Wykres punktowy":
            self.generate_scatter_chart()
        elif chart_type == "Wykres pudełkowy":
            self.generate_box_chart()

    def generate_line_chart(self):
        data = pd.read_csv('winequality-white .csv', delimiter=";")
        plt.plot(data[self.list1_var.get()], data[self.list2_var.get()])
        plt.xlabel(self.list1_var.get())
        plt.ylabel(self.list2_var.get())
        plt.title('Wykres liniowy')
        plt.show()

    def generate_bar_chart(self):
        data = pd.read_csv('winequality-white .csv', delimiter=";")
        plt.bar(data[self.list1_var.get()], data[self.list2_var.get()])
        plt.xlabel(self.list1_var.get())
        plt.ylabel(self.list2_var.get())
        plt.title('Wykres słupkowy')
        plt.show()

    def generate_pie_chart(self):
        data = pd.read_csv('winequality-white .csv', delimiter=";")
        plt.pie(data[self.list1_var.get()], labels=data[self.list2_var.get()])
        plt.title('Wykres kołowy')
        plt.show()

    def generate_scatter_chart(self):
        data = pd.read_csv('winequality-white .csv', delimiter=";")
        plt.scatter(data[self.list1_var.get()], data[self.list2_var.get()])
        plt.xlabel(self.list1_var.get())
        plt.ylabel(self.list2_var.get())
        plt.title('Wykres punktowy')
        plt.show()

    def generate_box_chart(self):
        data = pd.read_csv('winequality-white .csv', delimiter=";")
        plt.boxplot(data[self.list1_var.get()])
        plt.title('Wykres pudełkowy')
        plt.show()

    @staticmethod
    def get_chart_types():
        return ["Wykres liniowy", "Wykres słupkowy", "Wykres kołowy", "Wykres punktowy", "Wykres pudełkowy"]
