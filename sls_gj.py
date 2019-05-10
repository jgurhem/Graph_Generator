#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

from graphviz import Digraph
import graph_help as gh

p=4
myG = gh.Graph("sls_gj" + " p = " + str(p))

for i in range(p):
	myG.op_vector_init(gh.Node("B", [i, 0]))
	for j in range(p):
		myG.op_matrix_init(gh.Node("A", [i, j, 0]))
	
for k in range(0, p):
	myG.op_matrix_inv(gh.Node("A", [k, k, k]), gh.Node("A", [k, k, k + 1]))
	myG.op_pmv(gh.Node("A", [k, k, k + 1]), gh.Node("B", [k, k]))

	for j in range(k + 1, p):
		myG.op_pmm2(gh.Node("A", [k, k, k + 1]), gh.Node("A", [k, j, k]))
		for i in range(0, k):
			myG.op_pmm_d(gh.Node("A", [i, k, k]), gh.Node("A", [k, j, k + 1]), gh.Node("A", [i, j, k]))
		for i in range(k + 1, p):
			myG.op_pmm_d(gh.Node("A", [i, k, k]), gh.Node("A", [k, j, k + 1]), gh.Node("A", [i, j, k]))

	for i in range(0, k):
		myG.op_pmv_d(gh.Node("A", [i, k, k]), gh.Node("B", [k, k + 1]), gh.Node("B", [i, k]))
	for i in range(k + 1, p):
		myG.op_pmv_d(gh.Node("A", [i, k, k]), gh.Node("B", [k, k + 1]), gh.Node("B", [i, k]))

myG.graph_print()