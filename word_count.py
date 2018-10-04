#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )
parser.add_argument(
#1. Get our input file as a commandline argument (probably using argparse)
	"data_file",
	help = "path to the file we want to read"

)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------

# Sanity check for args
print("argss=", args)

#2. Open the file
fh = open( args.data_file )
print("the file handle is", fh)
#3. Initialize variables for lines, words, and bytes
lines = 0
words = 0
chars = 0
#4. Read the file line by line
for line in fh:
	print(line)
	lines += 1
