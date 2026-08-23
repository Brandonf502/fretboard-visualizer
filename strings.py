class Strings:
    pass


notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

tune = input("Enter string tuning: ")
frets = input("Enter number of frets: ")

strng = []

for i, note in enumerate(notes):
    if tune in notes:
        strng.apppend(note)
print(strng)



