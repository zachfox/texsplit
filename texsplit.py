#!/usr/local/bin/python

import splitdoc
import scrunchdoc
import sys
#import argparse

#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('--scrunch', metavar='N', type=int, nargs='+',
#                   help='an integer for the accumulator')

if sys.argv[1] == '--scrunch':
    scrunchdoc.write_to_main()
    splitdoc.copy_to_dest('./sections/','./')

elif sys.argv[1] == '--split':
    fname = sys.argv[2]
    ihandle = splitdoc.load_file(fname)
    splitdoc.loop_build(ihandle)
