import tkinter as tk
from tkinter import ttk
import pandas as pd


from correlations import Correlations
from measures import Measures
from chartsView import ChartsView

class DobreWinkoApp:
    def __init__(self, master):

        self.master = master
        master.title("Wino w liczbach")
        master.geometry("825x500")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Wino białe")

        self.action_frame = tk.Frame(self.master)
        self.action_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.action_label = tk.Label(self.action_frame, text="Wybierz akcję:", font=("Helvetica", 14))
        self.action_label.pack(side=tk.LEFT)

        self.action_buttons = []
        self.action_buttons.append(tk.Button(self.action_frame, text="Pokaz dane", command=self.show_table))
        self.action_buttons.append(tk.Button(self.action_frame, text="Obliczanie miar statystycznych", command=self.show_measures))
        self.action_buttons.append(tk.Button(self.action_frame, text="Wyznaczanie korelacji", command=self.show_correlations))
        self.action_buttons.append(tk.Button(self.action_frame, text="Wykresy", command=self.show_charts))

        for button in self.action_buttons:
            button.pack(side=tk.LEFT, padx=10)

        self.table_frame = tk.Frame(self.master)
        self.table_frame.pack(fill=tk.BOTH, expand=True)

        self.xscrollbar = tk.Scrollbar(self.table_frame, orient=tk.HORIZONTAL)
        self.xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.yscrollbar = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL)
        self.yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.table = ttk.Treeview(self.table_frame, yscrollcommand=self.yscrollbar.set,
                                  xscrollcommand=self.xscrollbar.set)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.xscrollbar.config(command=self.table.xview)
        self.yscrollbar.config(command=self.table.yview)

        self.data = pd.read_csv("winequality-white .csv", sep=";")
        self.table["columns"] = list(self.data.columns)
        self.table["show"] = "headings"
        for column in self.table["columns"]:
            self.table.heading(column, text=column)
        for index, row in self.data.iterrows():
            self.table.insert("", "end", values=list(row))

        self.table_frame.pack_forget()

    def show_table(self):
        self.hide_widgets()
        self.table_frame.pack(fill=tk.BOTH, expand=True)

    def show_charts(self):
        self.hide_widgets()
        chart_window = None
        chart = ChartsView(chart_window)
        chart.pack(fill=tk.BOTH, expand=True)

    def show_correlations(self):
        self.hide_widgets()
        correlations_window = tk.Toplevel(self.master)
        correlations_window.title("Korelacje")
        correlations_window.geometry("800x600")
        correlations = Correlations(correlations_window)
        correlations.pack(fill=tk.BOTH, expand=True)

    def show_measures(self):
        self.hide_widgets()
        measures_window = tk.Toplevel(self.master)
        measures_window.title("Miary statystyczne")
        measures_window.geometry("800x600")
        measures = Measures(measures_window)
        measures.pack(fill=tk.BOTH, expand=True)

    def hide_widgets(self):
        if hasattr(self, "correlations"):
            self.correlations.pack_forget()
            del self.correlations
        if hasattr(self, "measures"):
            self.measures.pack_forget()
            del self.measures

root = tk.Tk()
app = DobreWinkoApp(root)
root.mainloop()
