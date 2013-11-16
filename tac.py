import os
import sys

SIMPLE_FILESIZE_LIMIT = 1024*1024 # for now, set it to 1 MB
CHUNK_SIZE = 1024 # 1 KB chunks by default

def print_usage():
    print "Usage: tac [-cs chunk size] <filename>"

#
# this is a more complex way that will be more eficient for larger files
#
def tac_complex(fname, fsize):
    # handling files using 'with' will ensure its always properly closed
    with open(fname, 'r') as f:
        # Iterate backwards through the file
        for i in range(1, fsize/CHUNK_SIZE):
            # Set the position in the file to read from
            # 0 from beginning, 1 from current position, 2 from the end of the file
            f.seek(CHUNK_SIZE*i, 2)

            read_data = f.read(CHUNK_SIZE)
            #str.rfind(str, beg=0 end=len(read_data))
	    # TODO what if a line is longer than a CHUNK_SIZE??


        # Check if there are a few bytes left
        # f.tell() returns position in bytes from beginning of file
        remaining = f.tell()
        if remaining != 0:
            f.seek(0, 0)
            read_data = f.read(remaining)
            # TODO finish this
#
# this is a simpler way to do it for smaller files
#
def tac_simple(fname, fsize):
    contents = []

    # handling files using 'with' will ensure its always properly closed
    with open(fname) as f:
        contents = f.readlines()

    for line in reversed(contents):
        sys.stdout.write(line)

def tac(fname):
    statinfo = os.stat(fname)
    if statinfo.st_size < SIMPLE_FILESIZE_LIMIT:
        tac_simple(fname, statinfo.st_size)
    else:
        tac_complex(fname, statinfo.st_size)

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

