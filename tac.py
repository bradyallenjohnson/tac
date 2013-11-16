import sys

def print_usage():
  print "Usage: tac [-cs chunk size] <filename>"

def main():
  if len(sys.argv) < 2:
    print "ERROR, too few cmd line args"
    print_usage
    sys.exit(1)

  if sys.argv[1] == '-h':
    print_usage
    sys.exit(0)

  # TODO chunk-size not supported yet, need to incorporate GetOptions()
  if len(sys.argv) != 2:
    print "ERROR, chunk size not supported yet"
    sys.exit(1)

  print "Filename is %s" % sys.argv[1]

if __name__ == "__main__":
    main()
