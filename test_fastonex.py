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
import pytest
import fastonex
import tempfile

def test_fastatodict():
    """
    Unit test that determines if a FASTA formatted file can be successfully converted into Leave NEXUS.
    """
    known_input = ">Seq 1\nATGC\n>Seq 2\nATG"
    expected_output = {"Seq 1": "atgc", "Seq 2": "atg"}

    with tempfile.NamedTemporaryFile(delete=False, mode="w") as tp:
        tp.write(known_input)
        temp_file_name = tp.name

    with open(temp_file_name, "r") as tp:
        assert fastonex.fasta_todict(tp.name) == expected_output

def test_nexus_data():
    """
    Unit test that determines if a Leave NEXUS DATA header can be determined from a sequence dictionary.
    """
    seqdict = {"Seq1": "atgc", "Seq2": "atg"}
    expected_output = "#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX=2 NCHAR=4;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\n"

    assert fastonex.nexus_data(seqdict) == expected_output

def test_nexus_matrix():
    """
    Unit test that determines if a Leave NEXUS MATRIX block can be determined from a sequence dictionary.
    """
    know_input = {"Seq1" : "atgc", "Seq2" : "atg-"}
    expected_output = "MATRIX\n\nSeq1     atgc\nSeq2     atg-\n;\n\nEND;"

    assert fastonex.nexus_matrix(know_input) == expected_output
