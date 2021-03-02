from .Node import AbstractNode
from .AbstractGraph import AbstractGraph
from . import colorschemes as cs
import pygraphviz as pgv

class Graph(AbstractGraph):
  def __init__(self, gname):
    self.G = pgv.AGraph(strict=False, directed=True)
    self.gname=gname
    self.fontsize = 10
    self.colorscheme = cs.DefaultColorScheme.DefaultColorScheme()

  def set_fontsize(self, fontsize):
    self.fontsize = fontsize

  def set_colorscheme(self, colorscheme):
    if colorscheme == 'dark':
      self.colorscheme = cs.DarkColorScheme.DarkColorScheme()
    else:
      self.colorscheme = cs.DefaultColorScheme.DefaultColorScheme()
    self.G.graph_attr.update(bgcolor = self.colorscheme['background'])

  def graph_print(self):
    print(self.G.string())

  def graph_write(self):
    self.G.write(self.gname + ".dot")

  def __add_node(self, node, op):
    self.G.add_node(node.get_id(), label=node.get_id(), color=self.colorscheme[op], style='filled', fontcolor=self.colorscheme['fontcolor'], op=op, fontsize=self.fontsize)

  def __add_dependency(self, fro, to):
    self.G.add_edge(fro.get_id(), to.get_id())

  def op_vector_init(self, v):
    super(Graph, self).op_vector_init(v)
    self.__add_node(v, 'initv')

  def op_matrix_init(self, m):
    super(Graph, self).op_matrix_init(m)
    self.__add_node(m, 'initm')

  def op_matrix_inv(self, m_in, m_inv):
    super(Graph, self).op_matrix_inv(m_in, m_inv)
    self.__add_node(m_inv, 'inv')
    self.__add_dependency(m_in, m_inv)

  def op_pmv(self, m, v):
    super(Graph, self).op_pmv(m, v)
    v_incr = v.incr_last_coord()
    self.__add_node(v_incr, 'pmv')
    self.__add_dependency(v, v_incr)
    self.__add_dependency(m, v_incr)

  def op_pmm1(self, m1, m2):
    """m1 = m1 * m2"""
    super(Graph, self).op_pmm1(m1, m2)
    m_incr = m1.incr_last_coord()
    self.__add_node(m_incr, 'pmm1')
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)

  def op_pmm2(self, m1, m2):
    """m2 = m1 * m2"""
    super(Graph, self).op_pmm2(m1, m2)
    m_incr = m2.incr_last_coord()
    self.__add_node(m_incr, 'pmm2')
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)

  def op_pmm_d(self, A, B, C):
    """C = C - A * B"""
    super(Graph, self).op_pmm_d(A, B, C)
    m_incr = C.incr_last_coord()
    self.__add_node(m_incr, 'pmm_d')
    self.__add_dependency(A, m_incr)
    self.__add_dependency(B, m_incr)
    self.__add_dependency(C, m_incr)

  def op_pmv_d(self, A, b, c):
    """c = c - A * b"""
    super(Graph, self).op_pmv_d(A, b, c)
    v_incr = c.incr_last_coord()
    self.__add_node(v_incr, 'pmv_d')
    self.__add_dependency(A, v_incr)
    self.__add_dependency(b, v_incr)
    self.__add_dependency(c, v_incr)

  def op_sls(self, m, v):
    super(Graph, self).op_sls(m, v)
    v_incr = v.incr_last_coord()
    self.__add_node(v_incr, 'sls')
    self.__add_dependency(v, v_incr)
    self.__add_dependency(m, v_incr)

  def graph_print_dep(self, show=['']):
    for n in self.G.nodes():
      if not n.attr['op'] in show and show != ['']: continue
      print()
      print(n + " -- " + n.attr['op'])
      for e in self.G.edges(n):
        if e[0] == n:
          print("   -> " + e[1] + " -- " + self.G.get_node(e[1]).attr['op'])
        else:
          print("   <- " + e[0] + " -- " + self.G.get_node(e[0]).attr['op'])

