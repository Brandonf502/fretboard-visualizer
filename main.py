from guitar import *
from scales import *

def main():

    tuning = ['E', 'A', 'D', 'G', 'B', 'E']
    guitar = Guitar(22, tuning)
    guitar.play()
    print(guitar.fretboard)

    with open('guitar.txt', 'w') as file:
        file.write(f'Tuning: {' '.join(guitar.tuning)}\n')
        file.write(f'Frets: {guitar.frets}\n')
        for key in guitar.fretboard:
            file.write(f'{key}: {guitar.fretboard[key]}\n')

    with open('scales.txt', 'w') as file:
        scales = Scales()
        for scale in scales.notes:
            major_scale = scales.major(scale)
            file.write(f'{scale} major scale: {', '.join(major_scale)}\n')

            dorian_scale = scales.dorian(scale)
            file.write(f'{scale} dorian scale: {', '.join(dorian_scale)}\n')

            phrygian_scale = scales.phrygian(scale)
            file.write(f'{scale} phrygian scale: {', '.join(phrygian_scale)}\n')

            lydian_scale = scales.lydian(scale)
            file.write(f'{scale} lydian scale: {', '.join(lydian_scale)}\n')

            mixolydian_scale = scales.mixolydian(scale)
            file.write(f'{scale} mixolydian scale: {', '.join(mixolydian_scale)}\n')

            minor_scale = scales.aeolian(scale)
            file.write(f'{scale} aeolian scale: {', '.join(minor_scale)}\n')

            locrian_scale = scales.locrian(scale)
            file.write(f'{scale} locrian scale: {', '.join(locrian_scale)}\n\n')





if __name__ == "__main__":
    main()