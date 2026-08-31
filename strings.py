class String:
    def __init__(self, frets, tune):
        self.frets = frets
        self.tune = tune
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    def build_string(self):
        strings = []
        index = None

        for i, note in enumerate(self.notes):
            if self.tune in self.notes:
                index = self.notes.index(self.tune)

        for i in range(int(self.frets + 1)):
            strings.append(self.notes[index])
            index += 1
            if index == len(self.notes):
                index = 0

        return strings












