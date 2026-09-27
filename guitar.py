from fretboard import *
'''
Here we create the Guitar object. Pass it all of the information it needs, so that it may pass it to it's subsequent objects. 
These are 'has a' attributes. Guitar has a fretboard and strings. Fretboard has frets, and notes(or strings). Strings have notes, and fret positions.
'''

class Guitar: ## Define the guitars parameters to pass.
    def __init__(self, frets, tuning):
        self.fretboard = None
        self.frets = int(frets)
        self.tuning = tuning
        self.string_count = len(tuning)

    def get_fretboard(self): ## Build the fretbaord, get the strings.return teh result.
        fretboard = Fretboard(self.tuning, self.string_count, self.frets)
        fretboard.get_strings()
        return fretboard.build_fretboard()


    def play(self):
        self.fretboard = self.get_fretboard() ## pass our fretboard object into a local variable to the guitar object so that it is accessible.









