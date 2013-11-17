import os
import sys
import argparse


DEFAULT_SIMPLE_FILESIZE_LIMIT = 1024*1024 # for now, set it to 1 MB
DEFAULT_CHUNK_SIZE = 1024 # 1 KB chunks by default

#
# this is a more complex way that will be more eficient for larger files
#
def tac_complex(fname, fsize, chunk_size):
    # handling files using 'with' will ensure its always properly closed
    with open(fname, 'r') as f:
        # Iterate backwards through the file
        for i in range(1, fsize/chunk_size):
            # Set the position in the file to read from
            # 0 from beginning, 1 from current position, 2 from the end of the file
	    print "Getting chunk %d" % i
            f.seek(chunk_size*i*-1, 2)

            read_data = f.read(chunk_size)
	    print "Dumping data: %s" % read_data
            sys.stdout.write(read_data)
            #str.rfind(str, beg=0 end=len(read_data))
            # TODO what if a line is longer than a chunk_size??


        # Check if there are a few bytes left
        # f.tell() returns position in bytes from beginning of file
        remaining = f.tell()
	print "Remaining bytes in file %d" % remaining
        if remaining != 0:
            f.seek(0, 0)
            read_data = f.read(remaining)
	    print "Dumping remaining data:"
            sys.stdout.write(read_data)
            # TODO finish this

#
# this is a simpler way to do it for smaller files
#
def tac_simple(fname, fsize):
    contents = []

    # handling files using 'with' will ensure its always properly closed
    with open(fname) as f:
        #contents = f.readlines()
        for line in f:
	    contents.append(line)

    for line in reversed(contents):
        sys.stdout.write(line)

#
# Depending on the file size, go simple or complex
#
def tac(fname, chunk_size, simple_limit):
    statinfo = os.stat(fname)
    print "Filesize %d" % statinfo.st_size
    if statinfo.st_size < simple_limit:
        tac_simple(fname, statinfo.st_size)
    else:
        tac_complex(fname, statinfo.st_size, chunk_size)

def main():
    # 
    # Handle the command line args
    # 
    parser = argparse.ArgumentParser(description='Display the lines of a file in reverse order.')
    parser.add_argument('filename',
                        action='store',
                        type=str,
                        help='the path of the file to display in reverse order')
    parser.add_argument('-cs',
                        dest='chunk_size',
                        action='store',
                        metavar='bytes',
                        type=int,
                        default=DEFAULT_CHUNK_SIZE,
                        help='chunk size')
    parser.add_argument('-sl',
                        dest='simple_limit',
                        action='store',
                        metavar='file size in bytes',
                        type=int,
                        default=DEFAULT_CHUNK_SIZE,
                        help='simple file size limit, smaller file sizes will read in all lines')

    args = parser.parse_args()
    print args

    # 
    # Now tac it...
    # 
    tac(args.filename, args.chunk_size, args.simple_limit)

if __name__ == "__main__":
    main()

