from guitar import *

def main():

    tuning = ['E', 'A', 'D', 'G', 'B', 'E']
    guitar = Guitar(22, tuning)
    guitar.play()
    print(guitar.fretboard)


if __name__ == "__main__":
    main()