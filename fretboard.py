from strings import *

class Fretboard:
    def __init__(self,tuning,string_count, frets):
        self.fretboard = []
        self.string_count = string_count
        tuning = tuning.split()
        self.frets = frets

    def build_fretboard(self):
        for tune in tuning:


