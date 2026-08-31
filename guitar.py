from fretboard import *

class Guitar:
    def __init__(self, frets, tuning):
        self.fretboard = None
        self.frets = int(frets)
        self.tuning = tuning
        self.string_count = len(tuning)

    def get_fretboard(self):
        fretboard = Fretboard(self.tuning, self.string_count, self.frets)
        fretboard.get_strings()
        return fretboard.build_fretboard()


    def play(self):
        self.fretboard = self.get_fretboard()









