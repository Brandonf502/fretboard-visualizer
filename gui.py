import tkinter as tk
from guitar import Guitar
from scales import Scales

class GuitarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guitar Fretboard VIsualizer")
        self.root.geometry("1200x500")
        self.controls = tk.Frame(self.root)
        self.tuning_controls = tk.Frame(self.root)
        self.selected_root = tk.StringVar()
        self.selected_root.set("C")
        self.selected_mode = tk.StringVar()
        self.selected_mode.set("major")
        self.string_count = tk.IntVar()
        self.string_count.set(6)
        self.fret_count = tk.IntVar()
        self.fret_count.set(22)
        self.tuning_vars = []

        self.guitar = None
        self.music = Scales()

        self.controls.pack(fill="x")
        self.tuning_controls.pack(fill="x")

        self.build_controls()
        self.tuning_settings()
        self.build_canvas()

    def build_canvas(self):
        self.canvas = tk.Canvas(
            self.root,
            width=1100,
            height=350,
            background="black",
        )
        self.canvas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20,
        )
        self.canvas.bind("<Configure>", self.draw_fretboard)

    def build_controls(self,):
        root_label = tk.Label(
            self.controls,
            text="Root:"
        )
        mode_label = tk.Label(
            self.controls,
            text="Mode:"
        )
        string_count_label = tk.Label(
            self.controls,
            text="String Count:"
        )
        fret_count_label = tk.Label(
            self.controls,
            text="Fret Count:"
        )
        apply_button = tk.Button(
            self.controls,
            text="Apply",
            command=self.create_guitar
        )

        root_menu = tk.OptionMenu(
            self.controls,
            self.selected_root,
            *self.music.notes,
            command=self.update_scale
        )

        mode_menu = tk.OptionMenu(
            self.controls,
            self.selected_mode,
            "All",
            *self.music.modes,
            command=self.update_scale
        )
        string_count_menu = tk.Spinbox(
            self.controls,
            from_=1,
            to=12,
            textvariable = self.string_count,
            command=self.tuning_settings
        )
        fret_count_menu = tk.Spinbox(
            self.controls,
            from_=5,
            to=36,
            textvariable = self.fret_count
        )


        root_label.pack(side="left")
        root_menu.pack(side="left")

        mode_label.pack(side="left")
        mode_menu.pack(side="left")

        string_count_label.pack(side="left")
        string_count_menu.pack(side="left")

        fret_count_label.pack(side="left")
        fret_count_menu.pack(side="left")

        apply_button.pack(side="left")

    def tuning_settings(self):
        string_count = self.string_count.get()
        for widget in self.tuning_controls.winfo_children():
            widget.destroy()
        self.tuning_vars = []
        for i in range(string_count):
            tuning_var = tk.StringVar()
            tuning_var.set("")
            self.tuning_vars.append(tuning_var)
            tuning_menu = tk.OptionMenu(
                self.tuning_controls,
                tuning_var,
                *self.music.notes
            )
            tuning_menu_label = tk.Label(
                self.tuning_controls,
                text=f"String {i + 1} Tuning:"
            )
            tuning_menu_label.pack(side="left")
            tuning_menu.pack(side="left")

    def get_selected_scale(self):
        note = self.selected_root.get()
        mode = self.selected_mode.get()

        mode_functions = {
            "major": self.music.major,
            "dorian": self.music.dorian,
            "phrygian": self.music.phrygian,
            "lydian": self.music.lydian,
            "mixolydian": self.music.mixolydian,
            "aeolian": self.music.aeolian,
            "locrian": self.music.locrian
        }

        play = mode_functions[mode]

        return play(note)

    def draw_fretboard(self, event=None):
        if not self.guitar:
            return

        self.canvas.delete("all")

        string_count = self.guitar.string_count
        fret_count = self.guitar.frets
        tuning = self.guitar.tuning

        margin = 50
        canvas_height = self.canvas.winfo_height()
        canvas_width = self.canvas.winfo_width()
        usable_width = canvas_width - (margin * 2)

        fretboard_height = 250
        string_spacing = fretboard_height / (string_count - 1)
        fret_spacing = usable_width / fret_count
        fretboard_top = (canvas_height - fretboard_height) / 2
        fretboard_bottom = fretboard_top + fretboard_height

        x1 = margin
        x2 = usable_width + margin

        self.canvas.create_rectangle(
            x1,
            fretboard_top,
            x2,
            fretboard_bottom,
            fill="#2b2118",
            outline=""
        )

        for i in range(1, fret_count + 1):
            x = margin + (fret_spacing * i)
            self.canvas.create_line(x, fretboard_top, x, fretboard_bottom, fill="silver")

        for i in range(string_count):
            display_string = (string_count -1) - i

            y = fretboard_top + (string_spacing * display_string)
            self.canvas.create_line(x1, y, x2, y, fill="grey")
            self.canvas.create_text(x1 - 10, y, text=tuning[i], fill="white")

        self.draw_notes(
            string_count,
            fret_count,
            margin,
            fretboard_top,
            string_spacing,
            fret_spacing
        )

    def draw_notes(
            self,
            string_count,
            fret_count,
            margin,
            fretboard_top,
            string_spacing,
            fret_spacing
    ):
        selected_mode = self.selected_mode.get()
        if selected_mode == "All":
            fretboard_scale = self.music.notes
        else:
            display_scale,fretboard_scale = self.get_selected_scale()

        radius = 10

        for i in range(string_count):
            string_key = f"String {i + 1}"
            display_string = (string_count -1) - i


            # Y position stays the same for every note
            # on this particular string.
            note_y = fretboard_top + (string_spacing * display_string)

            # Go through frets 1 through 22
            for j in range(1, fret_count + 1):
                # Find the center of this fret space.
                note_x = (
                        margin
                        + (fret_spacing * (j - 1))
                        + (fret_spacing / 2)
                )

                # Get the actual note from your fretboard dictionary.
                note = self.guitar.fretboard[string_key][j]

                if note in fretboard_scale:

                    # Draw the note bubble.
                    self.canvas.create_oval(
                        note_x - radius,
                        note_y - radius,
                        note_x + radius,
                        note_y + radius,
                        fill="white"
                    )

                    self.canvas.create_text(
                        note_x,
                        note_y,
                        text=note,
                        fill="black"
                    )


    def create_guitar(self):
        fret_count = self.fret_count.get()
        tuning = []
        for string in self.tuning_vars:
            tuning.append(string.get())

        self.guitar = Guitar(fret_count, tuning)
        self.guitar.play()
        self.draw_fretboard()

    def update_scale(self, selection):
        self.draw_fretboard()





root = tk.Tk()
app = GuitarApp(root)
root.mainloop()