import tkinter as tk
from tkinter import ttk

class ChartsView(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.list1_options = ["Wybierz parametry", "Kwasowość stała", "Kwasowość lotna", "Kwas cytrynowy", "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem", "gęstość", "pH", "siarczany", "alkohol", "jakość"]
        self.list2_options = ["Wybierz parametry", "Kwasowość stała", "Kwasowość lotna", "Kwas cytrynowy", "Cukier resztkowy", "Chlorki", "Wolny dwutlenek siarki", "dwutlenek siarki ogółem", "gęstość", "pH", "siarczany", "alkohol", "jakość"]
        self.list3_options = ["Wybierz parametry", "Wykres liniowy", "Wykres słupkowy", "Wykres kołowy", "Wykres punktowy", "Wykres pudełkowy"]

        self.list1_var = tk.StringVar()
        self.list1_var.set("Select Option")

        self.list2_var = tk.StringVar()
        self.list2_var.set("Select Option")

        self.list3_var = tk.StringVar()
        self.list3_var.set("Select Option")

        self.list1 = ttk.OptionMenu(self, self.list1_var, *self.list1_options)
        self.list1.pack( padx=50, pady=10, side=tk.LEFT)

        self.list2 = ttk.OptionMenu(self, self.list2_var, *self.list2_options)
        self.list2.pack( padx=50, pady=10, side=tk.LEFT)

        self.list3 = ttk.OptionMenu(self, self.list3_var, *self.list3_options)
        self.list3.pack(padx=50, pady=10, side=tk.LEFT)

        self.buttonGeneruj = tk.Button(master, text="Generuj wykres", font=('Arial', 12))
        self.buttonGeneruj.pack(padx=10, pady=10, side=tk.LEFT)

        """self.submit_button = ttk.Button(self, text="Submit", command=self.submit_form)
        self.submit_button.pack(side=tk.LEFT, padx=10, pady=10)"""

        self.pack(fill=tk.BOTH, expand=True) # Dodajemy ramkę do okna głównego aplikacji

    """def submit_form(self):"""





