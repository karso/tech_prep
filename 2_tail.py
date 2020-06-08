##  This is an implementation of "tail -n N".
##  ToDo: Do an implementation of "tail -f".

import sys
import os

def tail(file, line=20):
    print "Tailing", file, "for", line, "lines...\n"
    print "----------------"
    #   Taking a block of size buffer_size from the end of the file; and putting
    # it into a list
    #   Once we got enough lines in the list; printing out the number of lines
    # we need
    buffer_size = 8192
    lines = []
    block = -1

    with open(file, 'r') as f:
    # ToDo: What if 'file' exists but not a readable file?
        while len(lines) < line:
            try:
                #   In case the file is too small, or the number of lines
                # are too many; this will fail.
                #   In that case; the except block will read the file from the
                # begining and add to the list.
                f.seek(buffer_size * block, os.SEEK_END)
            except:
                f.seek(0, 0)
                lines = f.readlines()
                break
            block -= 1
            lines = f.readlines()
    for l in lines[-line:]:
        print l
    print "----------------"

def realfile(file):
    if os.path.isfile(file):
        return file
    else:
        print "File", file, "does not exist"
        exit(1)

def realdigit(num):
    if num.isdigit():
        return num
    else:
        usage(sys.argv[0])

def usage(name):
    print "Usage: python", name, "[File Name] [Number of lines(int); Def=20]*"
    print "* => Optional"
    exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # If no input for number of lines; def is 20 lines.
        # Making sure we got a real file
        file = realfile(sys.argv[1])
        tail(file)
    elif len(sys.argv) == 3:
        #   Making sure we got a realfile and
        # the line number is a positive integer
        file = realfile(sys.argv[1])
        line = realdigit(sys.argv[2])
        tail(file, int(line))
    else:
        usage(sys.argv[0])
