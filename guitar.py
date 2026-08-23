from fretboard import *

class Guitar:
    def __init__(self):
        self.fretboard = None
        self.frets = None
        self.tuning = []
        self.string_count = None

    def build_guitar(self):
        self.frets = int(input("Enter number of frets:"))
        self.string_count = int(input("Enter number of strings: "))
        for i in range(self.string_count):
            self.tuning.append(input(f"Enter string {i+1} tuning (Enter strings from top to bottom please): "))


    def get_fretboard(self):
        fretboard = Fretboard(self.tuning, self.string_count, self.frets)
        fretboard.get_strings()
        return fretboard.build_fretboard()


    def play(self):
        self.build_guitar()
        self.fretboard = self.get_fretboard()








