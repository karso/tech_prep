# This code implements linux 'head -n N' command
import sys
import os

def realfile(file):
    if os.path.isfile(file):
        return file
    else:
        print "File", file, "does not exist"
        exit(1)

def realnum(num):
    if num.isdigit():
        return num
    else:
        usage()

def usage():
    print "python [script] [file] [num(int)]*"
    exit(1)

def head(file, lines=20):
    stored_lines = []
    buffer_size = 1024
    fp = True
    with open(file, 'r') as f:
        while len(stored_lines) < lines and fp != '':
            stored_lines = f.readlines(buffer_size)
            fp = f.read(buffer_size)

    for line in stored_lines[:lines]:
        print line

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = realfile(sys.argv[1])
        head(file)
    elif len(sys.argv) == 3:
        file = realfile(sys.argv[1])
        lines = realnum(sys.argv[2])
        head(file, int(lines))
    else:
        usage()

# ToDo: Need to handle very small files or very large number of lines.
