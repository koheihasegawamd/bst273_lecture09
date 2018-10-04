#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description =
	"returns the number of lines, words, and bytes (characters) of a file. INPUT: a file path. OUTPUTs: count of lines, count of words, count of bytes" )

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
#3. Initialize output variables for lines, words, and bytes
lines = 0
words = 0
chars = 0
#4. Read the file line by line
for line in fh:
	#print(line)  # Sanity check
	lines += 1   # for each line, add 1 (ie, count) to the lines variable
	words += len( line.split() )
print("The number of lines is:", lines)
