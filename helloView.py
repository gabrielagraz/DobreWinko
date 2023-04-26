import tkinter as tk
from PIL import Image, ImageTk


class HelloView:
    def __init__(self, master):
        self.master = master
        self.master.title("Witaj w aplikacji Dobre Winko!")

        # załadowanie obrazka
        image = Image.open("wine.png")
        self.image = ImageTk.PhotoImage(image)

        # utworzenie widżetu z obrazkiem
        self.label = tk.Label(self.master, image=self.image)
        self.label.pack()

        # utworzenie przycisku
        self.button = tk.Button(self.master, text="Poznaj wino w liczbach!", command=self.open_new_window)
        self.button.pack(pady=10)

        # wyśrodkowanie przycisku na obrazku
        self.button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def open_new_window(self):
        self.master.withdraw()  # ukryj okno główne
        from main import DobreWinkoApp
        DobreWinkoApp(self)

    def on_closing(self):
        self.master.destroy()  # zamknij aplikację


# utworzenie okna głównego
root = tk.Tk()
hello_view = HelloView(root)

# wyśrodkowanie okna głównego na ekranie
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

root.mainloop()
