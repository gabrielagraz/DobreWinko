import tkinter as tk
from tkinter import ttk
import pandas as pd
import self

from chartsView import ChartsView

class DobreWinkoApp:
    def __init__(self, master):

        self.master = master
        master.title("Wino w liczbach")
        master.geometry("800x500")

        # Tworzenie widżetu Notebook
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Dodawanie zakładek
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Wino białe")

        # self.page2 = ttk.Frame(self.notebook)
        # self.notebook.add(self.page2, text="Wino czerwone")

        # Dodanie suwaka do zakładki "Wino białe"
        self.action_frame = tk.Frame(self.master)
        self.action_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.action_label = tk.Label(self.action_frame, text="Wybierz akcję:", font=("Helvetica", 14))
        self.action_label.pack(side=tk.LEFT)

        self.action_var = tk.StringVar()
        self.action_var.set("Wybierz")

        self.action_options = ["Wybierz", "Pokaz dane", "Obliczanie miar statystycznych ", "Wyzanaczanie korelacji",
                               "Wykresy"]
        self.action_menu = ttk.OptionMenu(self.action_frame, self.action_var, *self.action_options,
                                          command=self.show_table)
        self.action_menu.pack(side=tk.LEFT, padx=10)

        # Ramka z tabelką
        self.table_frame = tk.Frame(self.page1)
        self.table_frame.pack(fill=tk.BOTH, expand=True)


        self.xscrollbar = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.yscrollbar = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL)
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Utworzenie tabeli
        self.table = ttk.Treeview(self.table_frame, yscrollcommand=self.yscrollbar.set,
                                  xscrollcommand=self.xscrollbar.set)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.xscrollbar.config(command=self.table.xview)
        self.yscrollbar.config(command=self.table.yview)


        # Pobieranie danych z pliku CSV wino białe i wstawienie ich do tabeli
        self.data = pd.read_csv("winequality-white .csv", sep=";")
        self.table["columns"] = list(self.data.columns)
        self.table["show"] = "headings"
        for column in self.table["columns"]:
            self.table.heading(column, text=column)
        for index, row in self.data.iterrows():
            self.table.insert("", "end", values=list(row))

        # Ukryj tabelkę na początku
        self.table_frame.pack_forget()

    def show_table(self, event):
        if self.action_var.get() == "Pokaz dane":
            # Usuń widżety poprzedniej opcji
            if hasattr(self, "chart"):
                self.chart.pack_forget()
            if hasattr(self, "correlations"):
                self.correlations.pack_forget()
            # Pokaż tabelkę
            self.table_frame.pack(fill=tk.BOTH, expand=True)

        elif self.action_var.get() == "Wykresy":
            # Usuń widżety poprzedniej opcji
            if hasattr(self, "table_frame"):
                self.table_frame.pack_forget()
            if hasattr(self, "correlations"):
                self.correlations.pack_forget()
            # Pokaż wykresy
            self.chart = ChartsView(self.master)
            self.chart.pack(fill=tk.BOTH, expand=True)

        elif self.action_var.get() == "Wyzanaczanie korelacji":
            # Usuń widżety poprzedniej opcji
            if hasattr(self, "chart"):
                self.chart.pack_forget()
            if hasattr(self, "table_frame"):
                self.table_frame.pack_forget()
            # Pokaż widok z korelacjami
            from correlations import Correlations
            self.correlations = Correlations(self.master)
            self.correlations.pack(fill=tk.BOTH, expand=True)

        elif self.action_var.get() == "Obliczanie miar statystycznych":
            # Usuń widżety poprzedniej opcji
            if hasattr(self, "measures"):
                self.chart.pack_forget()
            if hasattr(self, "table_frame"):
                self.table_frame.pack_forget()
            # Pokaż widok z miarami
            from measures import Measures
            self.measures = Measures(self.master)
            self.measures.pack(fill=tk.BOTH, expand=True)

        else:
            # Usuń widżety poprzedniej opcji
            if hasattr(self, "chart"):
                self.chart.pack_forget()
            if hasattr(self, "table_frame"):
                self.table_frame.pack_forget()
            if hasattr(self, "correlations"):
                self.correlations.pack_forget()
            if hasattr(self, "measures"):
                self.measures.pack_forget()

    def show_page1(self):
        self.notebook.select(self.page1)

    def show_page2(self):
        self.notebook.select(self.page2)


root = tk.Tk()
app = DobreWinkoApp(root)
root.mainloop()
# self.master.mainloop()