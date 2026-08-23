from strings import *

class Fretboard:
    def __init__(self,tuning,string_count,frets):
        self.fretboard = {}
        self.string_count = string_count
        self.frets = frets
        self.tuning = tuning
        self.strings = []

    def get_strings(self):
        for i in range(self.string_count):
            string = String(self.frets, self.tuning[i])
            self.strings.append(string.build_string())


    def build_fretboard(self):
        fretboard = {}

        for i, string in enumerate(self.strings):
            fretboard[f"String {i+1}"] = {}

            for fret, note in enumerate(string):
                fretboard[f"String {i+1}"][fret] = note

        return fretboard





