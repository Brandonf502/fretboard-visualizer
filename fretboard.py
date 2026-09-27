from strings import *

class Fretboard:
    def __init__(self,tuning,string_count,frets):
        '''
        The next step in building the guitar fretboard is constructing the fretboard. When creating a Guitar object it will ask to make a fretboard.
        The fretboard then asks to build the string objects. see get_strings().
        build_fretboard() then returns a nested dictionary of the fretboard that looks somethig like..
        fretboard = String 1:         String 1 refers to the lowest string on the guitar
                        0: E          the index or key, refers to the fret number. index at 0 is equivalent to open string
                        1: F          then the value is the note. (In the example seemingly E# is skipped, however E# does not exist in the chromatic scale.)
                        2: F#         Don't think too much about this just know E#, and B# do not exist.
                        3: G ... etc.

        '''
        self.fretboard = {}
        self.string_count = string_count
        self.frets = frets
        self.tuning = tuning
        self.strings = []

    def get_strings(self): ## Funcction to ask for the string objects to be created
        for i in range(self.string_count):
            string = String(self.frets, self.tuning[i])
            self.strings.append(string.build_string())


    def build_fretboard(self): ## Build our dictionary or 'fretboard' ##
        fretboard = {}

        for i, string in enumerate(self.strings):
            fretboard[f"String {i+1}"] = {}

            for fret, note in enumerate(string):
                fretboard[f"String {i+1}"][fret] = note

        return fretboard





