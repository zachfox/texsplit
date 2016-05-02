#!/usr/local/bin/python

import splitdoc
import scrunchdoc
import sys

if sys.argv[1] == '--scrunch':
    scrunchdoc.write_to_main()
    
elif sys.argv[1] == '--split':
    fname = sys.argv[2]
    ihandle = splitdoc.load_file(fname)
    splitdoc.loop_build(ihandle)
