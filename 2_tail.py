import sys
import os

def tail(file, line=20):
    print "Tailing", file, "for", line, "lines..."

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
        file = realfile(sys.argv[1])
        tail(file)
    elif len(sys.argv) == 3:
        file = realfile(sys.argv[1])
        line = realdigit(sys.argv[2])
        tail(file, line)
    else:
        usage(sys.argv[0])
