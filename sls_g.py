#https://pypi.org/project/graphviz/
#https://graphs.grevian.org/
#https://graphviz.readthedocs.io/en/stable/examples.html

from graphviz import Digraph

G2 = Digraph('dep_graph')
labels = {}

p=4

for i in range(p):
	n_name="B{}-{}".format(i, 0)
	labels[n_name] = "B{}".format(i)
	G2.node(n_name, labels[n_name], color = 'black', style='filled', fontcolor='white')
	for j in range(p):
		n_name="A{}-{}-{}".format(i, j, 0)
		labels[n_name] = "A{}-{}".format(i, j)
		G2.node(n_name, labels[n_name], color = 'black', style='filled', fontcolor='white')
	
for k in range(0, p):
	n_name="inv{}".format(k)
	labels[n_name] = "A{}-{}".format(k, k)
	G2.node(n_name, labels[n_name], color = 'red', style='filled', fontcolor='white')
	G2.edge("A{}-{}-{}".format(k, k, k), n_name)

	n_name="B{}-{}".format(k, k+1)
	labels[n_name] = "B{}".format(k)
	G2.node(n_name, labels[n_name], color = 'magenta', style='filled', fontcolor='white')
	G2.edge("inv{}".format(k), n_name)
	G2.edge("B{}-{}".format(k, k), n_name)
	
	for i in range(k+1, p):
		n_name="A{}-{}-{}".format(k, i, k+1)
		labels[n_name] = "A{}-{}".format(k, i)
		G2.node(n_name, labels[n_name], color = 'blue', style='filled', fontcolor='white')
		G2.edge("inv{}".format(k), n_name)
		G2.edge("A{}-{}-{}".format(k, i, k), n_name)
	
	for i in range(k+1, p):
		n_name="B{}-{}".format(i, k+1)
		labels[n_name] = "B{}".format(i)
		G2.node(n_name, labels[n_name], color = 'olivedrab2', style='filled', fontcolor='white')
		G2.edge("B{}-{}".format(i, k), n_name)
		G2.edge("B{}-{}".format(k, k+1), n_name)
		G2.edge("A{}-{}-{}".format(i, k, k), n_name)
		for j in range(k+1, p):
			n_name="A{}-{}-{}".format(i, j, k+1)
			labels[n_name] = "A{}-{}".format(i, j)
			G2.node(n_name, labels[n_name], color = 'darkgreen', style='filled', fontcolor='white')
			G2.edge("A{}-{}-{}".format(i, j, k), n_name)
			G2.edge("A{}-{}-{}".format(i, k, k), n_name)
			G2.edge("A{}-{}-{}".format(k, j, k+1), n_name)

for k in range(1, p):
	for i in range(0, p-k):
		n_name="B{}-{}".format(i, k+1+i)
		labels[n_name] = "B{}".format(i)
		G2.node(n_name, labels[n_name], color = 'olivedrab2', style='filled', fontcolor='white')
		G2.edge("B{}-{}".format(i, k+i), n_name)
		G2.edge("B{}-{}".format(p-k, p), n_name)
		G2.edge("A{}-{}-{}".format(i, p-k, i+1), n_name)
	
print(G2.source)
