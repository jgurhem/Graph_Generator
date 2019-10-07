from optparse import OptionParser

def parse_input_arg():
  parser = OptionParser()
  parser.add_option("-n", "--n", dest="N", type="int", help="number of blocks", default=4)
  parser.add_option("-s", "--s", dest="show", type="str", help="list of operations shown in dependencies, default shows all operations", default="")
  parser.add_option("--pdep", "--print_dependencies", dest="pdep", action="store_true", help="print dependencies", default=False)
  parser.add_option("--pdot", "--print_dot_graph", dest="pdot", action="store_true", help="print dot graph", default=True)
  parser.add_option("--no-pdot", "--no-print_dot_graph", dest="pdot", action="store_false", help="print dot graph", default=True)
  parser.add_option("--wdot", "--write_dot_graph", dest="wdot", action="store_true", help="write dot graph in '<graph_name>.dot'", default=False)
  parser.add_option("--backend", dest="backend", action="store", help="Supported backends : dot and Pegasus", default="dot", type=str)
  parser.add_option("--datasize", dest="datasize", action="store", help="Size of the global matrix", default=16, type=int)
  parser.add_option("--bin_dir", dest="bin_dir", action="store", help="Bin directory containing the applications", default="", type=str)
  (options, args) = parser.parse_args()
  return options
