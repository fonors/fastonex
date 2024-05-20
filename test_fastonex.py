#!/usr/bin/env python3
import pytest
import fastonex
import tempfile

def test_fastatodict():
    known_input = ">Seq 1\nATGC"
    expected_output = {"Seq 1": "ATGC"}

    tp = tempfile.NamedTemporaryFile()
    tp.write(known_input)
    tp.flush()

    assert fastonex.fasta_todict(tp.name) == expected_output