class Scales:
    '''
    There are 7 total modes in western music. These modes are all derived from the major scale.
    Major scale is our home mode and most common.
    If we're working from the A major scale. A, B, C#, D, E, F#, G#, A. to get the dorian mode of this major scale we will start from the second interval.
    A, B, C#, D, E, F#, G#, A        Notice in th example to the left, each mode uses the exact same notes as the parent major scale. Everything in music works like a circle.
    B, C#, D, E, F#, G#, A, B
    C#, D, E, F#, G#, A, B, C#
    D, E, F#, G#, A, B, C#, D
    E, F#, G#, A, B, C#, D, E
    F#, G#, A, B, C#, D, E, F#
    G#, A, B, C#, D, E, F#, G#
    '''
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

    def whole_step(self, note): ## Define what a whole step is in music theory ##
        if note in self.notes:
            index = self.notes.index(note)
            index = (index + 2) % len(self.notes)
            return self.notes[index]
        return note

    def half_step(self, note):## define a half step in music theory ##
        if note in self.notes:
            index = self.notes.index(note)
            index = (index + 1) % len(self.notes)
            return self.notes[index]
        return note

    def major(self, note):
        '''
        Scales are built off of whole steps and half steps. Using the chromatic scale starting from your desired note.
        W W H W W W H builds a major scale. now just like the modes. Move to the subsequent interval to get dorian etc.
        W H W W W H W is the formula to build a Dorian scale..so on so forth.
        '''
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
        if note in self.notes:
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
        if note in self.notes:
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
        if note in self.notes:
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
            note = self.half_step(note)
            scale.append(note)
            note = self.whole_step(note)
            scale.append(note)

            self.mixolydian_mode = scale
        return scale

    def aeolian(self, note):
        scale = []
        if note in self.notes:
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
        if note in self.notes:
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








