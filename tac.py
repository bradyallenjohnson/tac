import os
import sys

# for now, set it to 1 MB
SIMPLE_FILESIZE_LIMIT = 1024*1024

def print_usage():
    print "Usage: tac [-cs chunk size] <filename>"

def tac_complex(fname):
    # TODO not implemented yet
    print "ERROR the complex way of doing tac hasnt been implemented yet"

# this is a simpler way to do it for smaller files
def tac_simple(fname):
    contents = []

    with open(fname) as f:
        contents = f.readlines()

    for line in reversed(contents):
        sys.stdout.write(line)

def tac(fname):
    statinfo = os.stat(fname)
    if statinfo.st_size < SIMPLE_FILESIZE_LIMIT:
        tac_simple(fname)
    else:
        tac_complex(fname)

def main():
    if len(sys.argv) < 2:
        print "ERROR, too few cmd line args"
        print_usage
        sys.exit(1)

    if sys.argv[1] == '-h':
        print_usage
        sys.exit(0)

    # TODO chunk-size not supported yet, need to incorporate getopt
    if len(sys.argv) != 2:
        print "ERROR, chunk size not supported yet"
        sys.exit(1)

    #print "Filename is %s" % sys.argv[1]
    tac(sys.argv[1])

if __name__ == "__main__":
    main()

