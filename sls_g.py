#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

import graph_help.Node as gh
from graph_help.Graph_dot import Graph


p=4
myG = Graph("sls_g" + "_p" + str(p))

for i in range(p):
	myG.op_vector_init(gh.Node("B", [i, 0]))
	for j in range(p):
		myG.op_matrix_init(gh.Node("A", [i, j, 0]))
	
for k in range(0, p):
	myG.op_matrix_inv(gh.Node("A", [k, k, k]), gh.NodeSimple("inv", [k]))
	myG.op_pmv(gh.NodeSimple("inv", [k]), gh.Node("B", [k, k]))

	for i in range(k+1, p):
		myG.op_pmm2(gh.NodeSimple("inv", [k]), gh.Node("A", [k, i, k]))

	for i in range(k+1, p):
		myG.op_pmv_d(gh.Node("A", [i, k, k]), gh.Node("B", [k, k + 1]), gh.Node("B", [i, k]))
		for j in range(k+1, p):
			myG.op_pmm_d(gh.Node("A", [i, k, k]), gh.Node("A", [k, j, k + 1]), gh.Node("A", [i, j, k]))

for k in range(1, p):
	for i in range(0, p-k):
		myG.op_pmv_d(gh.Node("A", [i, p - k, i + 1]), gh.Node("B", [p - k, p]), gh.Node("B", [i, k + i]))

myG.graph_print()
