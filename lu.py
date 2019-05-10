#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

from graphviz import Digraph
import graph_help as gh

p=4
myG = gh.Graph("lu" + " p = " + str(p))

for i in range(p):
	for j in range(p):
		myG.op_matrix_init(gh.Node("A", [i, j, 0]))
	
for k in range(0, p - 1):
	myG.op_matrix_inv(gh.Node("A", [k, k, k]), gh.Node("A", [k, k, k + 1]))
	for i in range(k+1, p):
		myG.op_pmm1(gh.Node("A", [k, i, k]), gh.Node("A", [k, k, k + 1]))
		for j in range(k+1, p):
			myG.op_pmm_d(gh.Node("A", [i, k, k]), gh.Node("A", [k, j, k + 1]), gh.Node("A", [i, j, k]))

myG.graph_print()
