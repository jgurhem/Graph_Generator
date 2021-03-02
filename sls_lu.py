#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

import graph_help.Node as gh
import graph_help.ParseInputArg as pia
from graph_help.Graph import GraphGenerator

in_var = pia.parse_input_arg()
p = in_var.N
myG = GraphGenerator("sls_lu" + "_p" + str(p), in_var)
myG.set_fontsize(in_var.fontsize)
myG.set_colorscheme(in_var.colorscheme)

for i in range(p):
	myG.op_vector_init(gh.Node("B", [i, 0]))
	for j in range(p):
		myG.op_matrix_init(gh.Node("A", [i, j, 0]))
	
for k in range(0, p - 1):
	myG.op_matrix_inv(gh.Node("A", [k, k, k]), gh.NodeSimple("inv", [k]))
	for i in range(k+1, p):
		myG.op_pmm1(gh.Node("A", [i, k, k]), gh.NodeSimple("inv", [k]))
		for j in range(k+1, p):
			myG.op_pmm_d(gh.Node("A", [i, k, k + 1]), gh.Node("A", [k, j, k]), gh.Node("A", [i, j, k]))


for i in range(0, p - 1):
	for j in range(i+1, p):
		myG.op_pmv_d(gh.Node("A", [j, i, i + 1]), gh.Node("B", [i, i]), gh.Node("B", [j, i]))

for i in range(p - 1, -1, -1):
	myG.op_sls(gh.Node("A", [i, i, i]), gh.Node("B", [i, p - 1]))
	for j in range(0, i):
		myG.op_pmv_d(gh.Node("A", [j, i, j]), gh.Node("B", [i, p]), gh.Node("B", [j, p - i + j - 1]))

if in_var.pdot:
  myG.graph_print()
if in_var.wdot:
  myG.graph_write()
if in_var.pdep:
  myG.graph_print_dep(in_var.show.split(":"))
