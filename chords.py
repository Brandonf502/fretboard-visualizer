from scales import Scales

class Chords:
    def __init__(self):
        self.scales = Scales()
        self.chord = [True, False, True, False, True, False, False]
        self.chord_type = str(input("Enter chord type: "))

    def major_chord(self):
        chord = self.chord_type
        note = str(input("Enter a note: "))
        new_chord = []
        if chord == "major":
            chord = self.scales.major(note)

        for index, interval in enumerate(self.chord):
            if interval:
                chord = list(chord)
                new_chord.append(chord[index])
        chord = new_chord
        print(chord)
        return chord

    def major_seventh(self):
        chord = self.chord_type
        note = str(input("Enter a note: "))
        new_chord = []
        if chord == "major 7th":
            self.chord[6] = True
            chord = self.scales.major(note)

        for index, interval in enumerate(self.chord):
            if interval:
                chord = list(chord)
                new_chord.append(chord[index])
        chord = new_chord
        print(chord)
        return chord

    def minor_chord(self):
        chord = self.chord_type
        note = str(input("Enter a note: "))
        new_chord = []
        if chord == "minor":
            chord = self.scales.aeolian(note)

        for index, interval in enumerate(self.chord):
            if interval:
                chord = list(chord)
                new_chord.append(chord[index])
        chord = new_chord
        print(chord)
        return chord






