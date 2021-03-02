#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

import graph_help.Node as gh
import graph_help.ParseInputArg as pia
from graph_help.Graph import GraphGenerator

in_var = pia.parse_input_arg()
p = in_var.N
myG = GraphGenerator("sls_gj" + "_p" + str(p), in_var)
myG.set_fontsize(in_var.fontsize)

for i in range(p):
	myG.op_vector_init(gh.Node("B", [i, 0]))
	for j in range(p):
		myG.op_matrix_init(gh.Node("A", [i, j, 0]))
	
for k in range(0, p):
	myG.op_matrix_inv(gh.Node("A", [k, k, k]), gh.NodeSimple("inv", [k]))
	myG.op_pmv(gh.NodeSimple("inv", [k]), gh.Node("B", [k, k]))

	for j in range(k + 1, p):
		myG.op_pmm2(gh.NodeSimple("inv", [k]), gh.Node("A", [k, j, k]))
		for i in range(0, k):
			myG.op_pmm_d(gh.Node("A", [i, k, k]), gh.Node("A", [k, j, k + 1]), gh.Node("A", [i, j, k]))
		for i in range(k + 1, p):
			myG.op_pmm_d(gh.Node("A", [i, k, k]), gh.Node("A", [k, j, k + 1]), gh.Node("A", [i, j, k]))

	for i in range(0, k):
		myG.op_pmv_d(gh.Node("A", [i, k, k]), gh.Node("B", [k, k + 1]), gh.Node("B", [i, k]))
	for i in range(k + 1, p):
		myG.op_pmv_d(gh.Node("A", [i, k, k]), gh.Node("B", [k, k + 1]), gh.Node("B", [i, k]))

if in_var.pdot:
  myG.graph_print()
if in_var.wdot:
  myG.graph_write()
if in_var.pdep:
  myG.graph_print_dep(in_var.show.split(":"))
