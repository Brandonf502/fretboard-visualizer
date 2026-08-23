# PyGuitar 🎸

**PyGuitar** is a Python-based guitar and stringed-instrument visualization tool designed to help musicians understand how **notes, scales, chords, and musical patterns change across different tunings**.

Most guitar applications focus on standard tuning, predefined chord shapes, or tuning the instrument itself. PyGuitar takes a different approach: it generates the fretboard based on the instrument the user describes, allowing musicians to explore the relationships between notes across the entire neck in virtually any tuning.

## Purpose

The goal of PyGuitar is to help beginner through advanced musicians visualize:

* Notes across the entire fretboard
* Scales and scale patterns
* Chord construction and chord shapes
* Musical patterns across different tunings
* How changing an instrument's tuning changes the location of notes, scales, and chords

Rather than assuming a standard six-string guitar in E standard tuning, PyGuitar allows the instrument itself to be defined by the user.

## Instrument Customization

Users will be able to specify:

* **Number of strings**
* **Number of frets**
* **Tuning of each string**

This makes the underlying system adaptable beyond a standard guitar.

Potential instruments include:

* Electric and acoustic guitars
* Bass guitars
* 7-, 8-, and extended-range guitars
* 12-string guitars
* Ukuleles
* Violins
* Violas
* Cellos
* Other fretted or stringed instruments

The long-term goal is for the program to generate its musical relationships dynamically rather than relying exclusively on predefined fretboard layouts.

## Inputs

PyGuitar will use information provided by the user to construct an instrument.

Examples of user input include:

```text
String Count: 6
Fret Count: 22
Tuning: E A D G B E
```

A different instrument could instead be defined as:

```text
String Count: 4
Fret Count: 20
Tuning: E A D G
```

The program can then construct the appropriate fretboard from those parameters.

## Outputs

Based on the selected instrument and tuning, PyGuitar will eventually be capable of displaying:

* Fretboard notes
* Scales
* Chords
* Chord shapes
* Scale patterns
* Note relationships across the neck
* Patterns unique to alternate tunings

## Program Structure

PyGuitar is being designed using **object-oriented programming** so that the major concepts of the instrument can be represented independently.

### Guitar

The `Guitar` object represents the complete instrument.

It is responsible for information such as:

* Number of strings
* Number of frets
* Instrument tuning
* Collection of String objects

### String

Each individual string is represented by its own object.

A String knows:

* Its open tuning
* The number of available frets
* Which note occurs at each fret

Conceptually, an E string could produce data similar to:

```text
Fret 0  -> E
Fret 1  -> F
Fret 2  -> F#/Gb
Fret 3  -> G
...
Fret 12 -> E
```

The notes repeat according to the twelve-tone equal temperament system.

### Chord

Chord objects will represent chord formulas rather than only storing fixed guitar shapes.

Examples include:

* Major
* Minor
* Diminished
* Augmented
* Seventh chords
* Extended chords

This will allow PyGuitar to determine where the notes belonging to a chord occur on a user-generated instrument.

### Scale

Scale objects will represent the interval relationships that define different scales.

Potential examples include:

* Major
* Natural Minor
* Harmonic Minor
* Major Pentatonic
* Minor Pentatonic
* Blues
* Modes

Because scales are generated from musical relationships rather than fixed diagrams, the same scale can eventually be visualized in different keys and tunings.

### Pattern

Pattern objects will represent recognizable relationships between notes across the fretboard.

This system is intended to help musicians understand **why familiar guitar patterns change when alternate tunings are used**, rather than simply memorizing diagrams.

## Data Structures

The final data structure is still being developed as the project evolves.

Current possibilities include using dictionaries to associate fret positions with their corresponding notes.

For example:

```text
E String
{
    "fret 0": "E",
    "fret 1": "F",
    "fret 2": "F#/Gb",
    "fret 3": "G"
}
```

Classes will be used to represent larger musical concepts such as instruments, strings, chords, scales, and patterns.

The architecture may change as development continues and more efficient representations become apparent.

## Project Goals

The project is intended to demonstrate and strengthen several Python programming concepts, including:

* Object-oriented programming
* Classes and object relationships
* Dictionaries and other data structures
* Loops and iteration
* Modular arithmetic
* User input validation
* Algorithm design
* Dynamic data generation
* Separation of program responsibilities

A major goal of the project is to **calculate musical information instead of hard-coding every possible instrument, tuning, chord, or scale**.

## Planned Development

Initial development will focus on constructing the underlying fretboard model.

Planned milestones include:

1. Create configurable instruments from user input.
2. Generate individual strings from their tunings.
3. Calculate the note at every fret.
4. Display the complete fretboard.
5. Implement scale formulas.
6. Highlight scales across the generated fretboard.
7. Implement chord formulas.
8. Identify possible chord shapes and note combinations.
9. Implement reusable fretboard patterns.
10. Expand support for alternate and extended-range instruments.
11. Develop a graphical fretboard visualization.

## Example Use Case

A guitarist normally plays in standard tuning:

```text
E A D G B E
```

but changes to an alternate tuning:

```text
D A D G A D
```

Instead of searching for separate diagrams for every chord and scale, the user could enter the new tuning into PyGuitar.

PyGuitar would generate the new fretboard and allow the musician to explore where notes, scales, chords, and patterns now occur.

## Intended Audience

PyGuitar is designed for:

**Beginners** who want to understand the relationship between notes and chord shapes.

**Intermediate musicians** exploring scales, improvisation, and alternate tunings.

**Advanced musicians** experimenting with unusual tunings, extended-range instruments, and unfamiliar fretboard relationships.

## Status

🚧 **PyGuitar is currently in development.**

The initial version is being developed as a comprehensive Python programming project. Features and architecture are expected to evolve as development continues.

## Future Vision

The long-term vision for PyGuitar is to become an interactive fretboard exploration tool where musicians can define almost any stringed instrument and immediately visualize its musical possibilities.

Rather than asking:

> *"What shapes am I supposed to memorize in this tuning?"*

PyGuitar aims to help musicians understand:

> *"Where are the notes, why do these shapes work, and what new patterns can I discover?"*
