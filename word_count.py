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

print(args)
print(args.data_file)
