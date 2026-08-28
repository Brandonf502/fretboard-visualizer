class Scales:
    def __init__(self):
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.major_mode = []
        self.melodic_minor_mode = None
        self.dorian_mode = []
        self.phrygian_mode = []
        self.lydian_mode = []
        self.mixolydian_mode = []
        self.aeolian_mode = []
        self.locrian_mode = []

    def whole_step(self, note):
        if note in self.notes:
            index = self.notes.index(note)
            index = (index + 2) % len(self.notes)
            return self.notes[index]
        return note

    def half_step(self, note):
        if note in self.notes:
            index = self.notes.index(note)
            index = (index + 1) % len(self.notes)
            return self.notes[index]
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

            self.major_mode = scale
        return scale

    def dorian(self, note):
        scale = []
        for note in self.notes:
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
            note = self.whole_step(note)
            scale.append(note)

            self.dorian_mode = scale
        return scale
    def phrygian(self, note):
        scale = []
        for note in self.notes:
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
            note = self.whole_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)

            self.phrygian_mode = scale
        return scale

    def lydian(self, note):
        scale = []
        for note in self.notes:
            scale.append(note)
            note = self.whole_step(note)
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
            note = self.half_step(note)
            scale.append(note)

            self.lydian_mode = scale
        return scale

    def mixolydian(self, note):
        scale = []
        for note in self.notes:
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
            note = self.half_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)

            self.mixolydian_mode = scale
        return scale

    def aeolian(self, note):
        scale = []
        for note in self.notes:
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)
            note = self.half_step(note)
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

            self.aeolian_mode = scale
        return scale

    def locrian(self, note):
        scale = []
        for note in self.notes:
            scale.append(note)
            note = self.half_step(note)
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

            self.locrian_mode = scale
        return scale


def main():
    scales = Scales()
    note = input('Enter a note: ')
    scale = scales.major(note)
    print(scale)


main()





