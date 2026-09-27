class String:
    def __init__(self, frets, tune):
        '''
        This initializes the string object. Each string has a number of frets equal to the amount of frets the guitar has.
            This number is passed in from the guitar object. Each string also has its own tuning.
            This note is also passed in from the guitar object. The example guitar is standard tuning or: E A D G B E
        '''
        self.frets = frets
        self.tune = tune
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'] ## List of notes in the !2 tone equal temperament scale. This will be used to calculate each string.##

    def build_string(self):
        strings = []
        index = None

        for i, note in enumerate(self.notes): ## For each note in the 12-TET scale start at th index of the note in the tuning. ##
            if self.tune in self.notes:
                index = self.notes.index(self.tune)

        for i in range(int(self.frets + 1)): ## For each fret of chosen amount, append the next note to that fret. ##
            strings.append(self.notes[index])
            index += 1
            if index == len(self.notes): ## Once we reach the end of the scale or G# (highest note in western music) Return back to 0 or A lowest note in western music ##
                index = 0  ## Music works in a circle the scale starts at A ends at G#, one half step up from G# is A. One half step down from A is G#. ##

        return strings












