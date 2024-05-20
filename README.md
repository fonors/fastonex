# FASTA to Leave NEXUS Converter
Converts a FASTA formatted file into *Leave* NEXUS and prints it to STDOUT.

## Function
The main program is `fastonex.py`. Running it will properly will return e *Leave* NEXUS formatted file into STDOUT.
You also have `test_fastonex.py`, which has a couple of unit tests to ensure that the program works as intended.

## Motivation
The motivation for creating this application is to understand how unit tests can improve our workflow and debugging process, making catching and fixing any currently present bugs easier, and making it so that future problems are prevented. It also allows for a good learning exercise on the differences between different text-based sequence file formats.

## Usage
### Mandatory arguments
You must use these arguments in order for the conversion to work at all.

`-i` or `--input`: Input FASTA file path.

### Unit Tests
You can run the unit tests to verify if the program's functions works as intended using pytest. To do so, just run:
`pytest test_fastonex.py`

## Credits
This program was developed by fonors, goncalof21, MadalenaFranco2 & scmdcunha.
