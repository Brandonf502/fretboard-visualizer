class Scales:
    def __init__(self):
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.major_scale = []
        self.melodic_minor = None
        self.dorian = None
        self.phrygian = None
        self.lydian = None
        self.mixolydian = None
        self.aeolian = None
        self.locrian = None

    def whole_step(self, note):
        if note in self.notes:
            index = self.notes.index(note)
            index += 2
            if index > len(self.notes) - 1:
                index = 0
                index += 1
                note = self.notes[index]
            else:
                note = self.notes[index]
        return note

    def half_step(self, note):
        if note in self.notes:
            index = self.notes.index(note)
            index += 1
            if index > len(self.notes) - 1:
                index = 0
                note = self.notes[index]
            else:
                note = self.notes[index]
        return note

    def major(self, note):
        scale = []
        if note in self.notes:
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)
            note = self.half_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)
            note = self.half_step(note)
            scale.append(note)

            self.major_scale = scale
        return scale






def main():
    scales = Scales()
    note = input('Enter a note: ')
    scale = scales.major(note)
    print(scale)


main()





