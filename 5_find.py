# This is a python implementation of find command
# It takes 2 arguements, search_base and filename
# In case just one argument provided; it treats it as file name and searches in
# current working directory

import sys
import os

def usage(name):
    print "python", name, "[search dir]* [file name]"
    print "* Optional => Def: Current Working Directory"
    exit(1)

def find(search_dir, file):
    dirs = [search_dir]
    for dir in dirs:
        # print dir
        try:
            dir_content = os.listdir(dir)
        except Exception as e:
            print "File not found"
            exit(1)
        for obj in dir_content:
            # print "dp2"
            # print dir+obj
            if os.path.isfile(dir+obj) and obj == file:
                print "File Found..."
                print dir, file
                exit(1)
            elif os.path.isdir(dir+obj):
                dirs.append(dir+obj)
                # print dirs
                # print dirs
            else:
                continue
    print "File not found"

if __name__ == '__main__':
    search_dir = ""
    file = ""

    #one argument provided
    #treat is as file name; let user know
    if len(sys.argv) == 2:
        file = sys.argv[1]
        print "Looking for file", file, "in current working directory and all sub-directories"
        search_dir = os.getcwd() + '/'
    #two arguments provided
    #take first argument as base dir, second argument as fille name;
    elif len(sys.argv) == 3:
        search_dir = sys.argv[1]
        file = sys.argv[2]
        #make sure dir exists
        if os.path.isdir(search_dir):
            print "Looking for file", file, "in", search_dir, "and all sub-directories"
        else:
            print "The base dir", search_dir, "is not found"
            usage(sys.argv[0])
    #everything else
    else:
        usage(sys.argv[0])

    find(search_dir, file)
