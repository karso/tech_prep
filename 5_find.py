# This is a python implementation of find command
# It takes 2 arguements, search_base and filename
import sys
import os

def usage(name):
    print "python", name, "[search dir]* [file name]"
    print "* Optional => Def: Current Working Directory"
    exit(1)

def find(search_dir, file):
    print "I am in find..."

if __name__ == '__main__':
    search_dir = ""
    file = ""
    if len(sys.argv) == 2:
        if os.path.isdir(sys.argv[1]):
            print "No file name input found..."
            usage(sys.argv[0])
        else:
            file = sys.argv[1]
            search_dir = os.getcwd()
    elif len(sys.argv) == 3:
        if os.path.isdir(sys.argv[1]):
            search_dir = sys.argv[1]
            file = sys.argv[2]
        else:
            print "Input directory does not exist..."
            usage(sys.argv[0])
    else:
        usage(sys.argv[0])
    find(search_dir, file)
