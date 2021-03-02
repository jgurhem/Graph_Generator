#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

import graph_help.Node as gh
import graph_help.ParseInputArg as pia
from graph_help.Graph import GraphGenerator

in_var = pia.parse_input_arg()
p = in_var.N
myG = GraphGenerator("lu" + "_p" + str(p), in_var)
myG.set_fontsize(in_var.fontsize)

for i in range(p):
	for j in range(p):
		myG.op_matrix_init(gh.Node("A", [i, j, 0]))
	
for k in range(0, p - 1):
	myG.op_matrix_inv(gh.Node("A", [k, k, k]), gh.NodeSimple("inv", [k]))
	for i in range(k+1, p):
		myG.op_pmm1(gh.Node("A", [i, k, k]), gh.NodeSimple("inv", [k]))
		for j in range(k+1, p):
			myG.op_pmm_d(gh.Node("A", [i, k, k + 1]), gh.Node("A", [k, j, k]), gh.Node("A", [i, j, k]))


if in_var.pdot:
  myG.graph_print()
if in_var.wdot:
  myG.graph_write()
if in_var.pdep:
  myG.graph_print_dep(in_var.show.split(":"))
