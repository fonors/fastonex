#!/usr/bin/env python3
'''
    FASTA to Leave NEXUS Converter - Convert a FASTA file into Leave NEXUS
    Copyright (C) 2024  fonors, goncalof21, MadalenaFranco2 & scmdcunha

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import argparse

parser = argparse.ArgumentParser(
                    prog = 'FASTA to NEXUS Converter',
                    description = 'Convert a FASTA formatted file into the NEXUS format.')

def user_args(argparser):
    """
    Gets the arguments the user defined when running the script and returns them.
    """
    argparser.add_argument("-i", "--input", help="Input FASTA file.")

    user_args = argparser.parse_args()
    return user_args

def fasta_todict(file):
    """
    Takes a FASTA formatted file and returns a dictionary with the sequences.
    """
    with open(file, "r") as file:
        sequences = {}
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
                sequences[name] = sequences[name].lower()
    return sequences

def nexus_data(seqdict):
    """
    Takes a dictionary containing sequences and returns the NEXUS DATA header.
    """
    nexus_header = "#NEXUS\n\nBEGIN DATA;\n"

    for seq in seqdict:
        current_sequence = seqdict[seq].upper()
        if "U" in current_sequence:
            datatype = "FORMAT DATATYPE=RNA MISSING=N GAP=-;\n"
        elif "T" in current_sequence:
            datatype = "FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"

    maxseqlen = max(len(seq) for seq in seqdict)
    nexus_header = nexus_header + f"DIMENSIONS NTAX={str(len(seqdict))} NCHAR={str(maxseqlen)};\n" + datatype

    return nexus_header

def nexus_matrix(seqdict):
    """
    Takes a dictionary containing sequences and returns the NEXUS MATRIX block.
    """
    nexus_matrix_block = "MATRIX\n\n"
    maxseqlen = max(len(seq) for seq in seqdict)

    for seq in seqdict:
        if len(seqdict[seq]) < maxseqlen:
            ngaps = maxseqlen - len(seqdict[seq])
            nexus_matrix_block = nexus_matrix_block + f"{seq}     {seqdict[seq]}"
            for gaps in range(ngaps):
                nexus_matrix_block = nexus_matrix_block + "-"
            nexus_matrix_block = nexus_matrix_block + "\n"
        else:
            nexus_matrix_block = nexus_matrix_block + f"{seq}     {seqdict[seq]}\n"
    nexus_matrix_block = nexus_matrix_block + ";\n"
    nexus_matrix_block = nexus_matrix_block + "\nEND;"

    return nexus_matrix_block

if __name__ == "__main__":
    user_args = user_args(parser)
    seq_dict = fasta_todict(user_args.input)
    output = nexus_data(seq_dict)
    output = output + nexus_matrix(seq_dict)
    print(output)
