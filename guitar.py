from fretboard import *

class Guitar:
    def __init__(self):
        self.fretboard = None
        self.frets = None
        self.tuning = None
        self.string_count = None

    def get_fretboard(self):
        fretboard = Fretboard(self.tuning,self.string_count, self.frets)




