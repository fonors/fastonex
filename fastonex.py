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
    nexus_header = "#NEXUS\n\n"
    nexus_header = nexus_header + "BEGIN DATA;\n"
    nexus_header = nexus_header + f"DIMENSIONS NTAX={str(len(seqdict))} NCHAR={str(maxseqlen(inputfile))};\n"
    if isdna:
        newnexusfile.write("FORMAT DATATYPE=DNA MISSING=N GAP=-;\n")
    else:
        newnexusfile.write("FORMAT DATATYPE=RNA MISSING=N GAP=-;\n")

def nexus_matrix():
    newnexusfile.write("MATRIX\n\n")
    for seq in seqdict:
        if len(seqdict[seq]) < maxseqlength:
            ngaps = maxseqlength - len(seqdict[seq])
            newnexusfile.write(f"{seq}     {seqdict[seq]}")
            for gaps in range(ngaps):
                newnexusfile.write("-")
            newnexusfile.write("\n")
        else:
            newnexusfile.write(f"{seq}     {seqdict[seq]}\n")
    newnexusfile.write(";\n")
    newnexusfile.write("\nEND;")

if __init__ == "__name__":
    user_args = user_args(parser)
    seq_dict = fasta_todict(user_args.input)
