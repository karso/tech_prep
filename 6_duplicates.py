# This program finds all the duplicate files in a given directory
# Definition of duplicate is that the checksum of the 2 files are same
# It does not consider sub-folders
import os
import sys

def usage():
    print "python", sys.argv[0], "[target_dir]"
    exit(1)

def duplicate(target_dir):
    print "The target directory found. Looking for duplicates..."
    # find all object inside the dir
    dir_contents = os.path.listdir(target_dir)
    chksum = {}
    # for each obj, if it is a file; find the checksum and add in a dict
    for obj in dir_contents:
        if os.path.isfile(target_dir+obj):
            # find the checksum and add in dict. what if file is too big
        else:
            continue



if __name__ == "__main__":
    target_dir = ""
    #take a folder name to look at
    if len(sys.argv) == 2:
        target_dir = sys.argv[1]
        # check if the path is correct
        if os.path.isdir(target_dir):
            duplicate(target_dir)
        else:
            print "The input dir does not exist."
            usage()
    else:
        usage()
