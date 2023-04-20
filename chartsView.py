import tkinter as tk
from tkinter import ttk

class ChartsView(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.list1_options = ["Kwasowość stała", "Kwasowość lotna", "Kwas cytrynowy", "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem", "gęstość", "pH", "siarczany", "alkohol", "jakość"]
        self.list2_options = ["Kwasowość stała", "Kwasowość lotna", "Kwas cytrynowy", "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem", "gęstość", "pH", "siarczany", "alkohol", "jakość"]
        self.list3_options =["Tutaj typy wykresów"]
        self.list1_var = tk.StringVar()
        self.list1_var.set("Select Option")

        self.list2_var = tk.StringVar()
        self.list2_var.set("Select Option")

        self.list3_var = tk.StringVar()
        self.list3_var.set("Select Option")

        print("Wybierz parametry do utworzenia wykresów")

        self.list1 = ttk.OptionMenu(self, self.list1_var, *self.list1_options)
        self.list1.pack( padx=10, pady=10)

        self.list2 = ttk.OptionMenu(self, self.list2_var, *self.list2_options)
        self.list2.pack( padx=10, pady=10)

        self.list3 = ttk.OptionMenu(self, self.list3_var, *self.list3_options)
        self.list3.pack(padx=10, pady=10)

        """self.submit_button = ttk.Button(self, text="Submit", command=self.submit_form)
        self.submit_button.pack(side=tk.LEFT, padx=10, pady=10)"""

        self.pack(fill=tk.BOTH, expand=True) # Dodajemy ramkę do okna głównego aplikacji

    """def submit_form(self):"""





