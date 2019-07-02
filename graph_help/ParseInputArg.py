from optparse import OptionParser

def parse_input_arg():
  parser = OptionParser()
  parser.add_option("-n", "--n", dest="N", type="int", help="number of blocks", default=4)
  (options, args) = parser.parse_args()
  return options
