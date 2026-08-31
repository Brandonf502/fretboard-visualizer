import tkinter as tk
from guitar import Guitar

class GuitarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Fretboard VIsualizer")
        self.root.geometry("1200x500")

        self.guitar = Guitar(22, ['E', 'A', 'D', 'G', 'B', 'E'])

        self.guitar.play()

        self.canvas = tk.Canvas(
            self.root,
            width=1100,
            height=350,
            background="#2b2118",
        )
        self.canvas.pack(padx=20, pady=20)

root = tk.Tk()
app = GuitarApp(root)
root.mainloop()