""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    import os
    parser = ArgumentParser(description='This program applies a standard scale transform to the data in infile and writes it to outfile.')
    parser.add_argument('infile',help='provide input file path',nargs='?')
    parser.add_argument('outfile',help='provide output file path',nargs='?')
    data = parser.parse_args()
    out_data = np.loadtxt(data.infile)
    output = (out_data - out_data.mean(axis=0)) / out_data.std(axis=0)
    r_dir = get_repository_root()
    os.makedirs(r_dir / "outputs", exist_ok=True)
    np.savetxt(data.outfile, output, fmt='%.2e')
