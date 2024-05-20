#!/usr/bin/env python3
import argparse
from sys import stderr, exit

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
    nexus_header = "#NEXUS\n\n"
    nexus_header = nexus_header + "BEGIN DATA;\n"

    seqlist = []
    for seq in seqdict:
        seqlist.append(seqdict[seq])
    maxseqlen = max(len(seq) for seq in seqlist)
    nexus_header = nexus_header + f"DIMENSIONS NTAX={str(len(seqdict))} NCHAR={str(maxseqlen))};\n"

    for seq in seq_dict:
        current_sequence = seq_dict[seq].upper()
        if "U" in current_sequence:
            nexus_header = nexus_header + "FORMAT DATATYPE=RNA MISSING=N GAP=-;\n"
        elif "T" in current_sequence:
            nexus_header = nexus_header + "FORMAT DATATYPE=DNA MISSING=N GAP=-;\n"

    return nexus_header

def nexus_matrix(seqdict):
    """
    Takes a dictionary containing sequences and returns the NEXUS MATRIX block.
    """
    seqlist = []
    for seq in seqdict:
        seqlist.append(seqdict[seq])
    maxseqlen = max(len(seq) for seq in seqlist)

    nexus_matrix_block = "MATRIX\n\n"
    for seq in seqdict:
        if len(seqdict[seq]) < maxseqlen:
            ngaps = maxseqlen - len(seqdict[seq])
            nexus_matrix_block = nexus_matrix_block + f"{seq}     {seqdict[seq]}")
            for gaps in range(ngaps):
                nexus_matrix_block = nexus_matrix_block + "-"
            nexus_matrix_block = nexus_matrix_block + "\n"
        else:
            nexus_matrix_block = nexus_matrix_block + f"{seq}     {seqdict[seq]}\n"
    nexus_matrix_block = nexus_matrix_block + ";\n"
    nexus_matrix_block = nexus_matrix_block + "\nEND;"

    return nexus_matrix_block

if __init__ == "__name__":
    user_args = user_args(parser)
    seq_dict = fasta_todict(user_args.input)
    output = nexus_data(seq_dict)
    output = output + nexus_matrix(seq_dict)
    print(output)
