import sys

def GraphGenerator(name, options):
  if options.backend == "dot":
    from graph_help.Graph_dot import Graph
    return Graph(name)
  elif options.backend == "Pegasus":
    from graph_help.Graph_pegasus import Graph
    return Graph(name, options)
  else:
    print("Error : Wrong backend")
    sys.exit(1)
