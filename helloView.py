import tkinter as tk
from PIL import Image, ImageTk

class helloView:
    def __init__(self, master):
        self.master = master
        self.master.title("Witaj w aplikacji Dobre Winko!")

# utworzenie okna
window = tk.Tk()
window.title("Witaj w aplikacji Dobre Winko!")

# załadowanie obrazka
image = Image.open("wine.png")
image = ImageTk.PhotoImage(image)

# utworzenie widżetu z obrazkiem
label = tk.Label(window, image=image)
label.pack()

# utworzenie przycisku
button = tk.Button(window, text="Poznaj wino w liczbach!")
button.pack(pady=10)

# wyśrodkowanie przycisku na obrazku
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def przejdz_do_nowego_okna(self):
    self.master.withdraw()  # ukryj okno główne

window.mainloop()
