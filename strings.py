from enum import nonmember


class String:
    def __init__(self, frets, tune):
        self.frets = frets
        self.tune = tune
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    def build_string(self):
        strng = []
        index = None

        for i, note in enumerate(notes):
            if tune in notes:
                index = notes.index(tune)

        for i in range(int(frets)):
            strng.append(notes[index])
            index += 1
            if index == len(notes):
                index = 0



notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

tune = input("Enter string tuning: ")
frets = input("Enter number of frets: ")





