from graphviz import Digraph

class Node:
  def __init__(self, name, coord):
    if type(coord) is not list:
      raise TypeError
    if len(coord) < 2:
      raise IndexError
    self.name = name
    self.coord = coord

  def incr_last_coord(self):
    new_coord = self.coord.copy()
    new_coord[len(new_coord) - 1] += 1
    return Node(self.name, new_coord)

  def get_id(self):
    id_ = self.name
    for i in range(len(self.coord)):
      id_ += "-" + str(self.coord[i])
    return id_

  def get_label(self):
    l = self.name
    for i in range(len(self.coord) - 1):
      l += "-" + str(self.coord[i])
    return l


class Graph:
  def __init__(self, gname):
    self.G = Digraph(gname)

  def graph_print(self):
    print(self.G)

  def __add_node(self, node, color):
    if type(node) is not Node:
      raise TypeError
    self.G.node(node.get_id(), node.get_label(), color = color, style='filled', fontcolor='white')

  def __add_dependency(self, fro, to):
    if type(fro) is not Node:
      raise TypeError
    if type(to) is not Node:
      raise TypeError
    self.G.edge(fro.get_id(), to.get_id())

  def op_vector_init(self, v):
    if type(v) is not Node:
      raise TypeError
    self.__add_node(v, 'black')

  def op_matrix_init(self, m):
    if type(m) is not Node:
      raise TypeError
    self.__add_node(m, 'black')

  def op_matrix_inv(self, m_in, m_inv):
    if type(m_in) is not Node:
      raise TypeError
    if type(m_inv) is not Node:
      raise TypeError
    self.__add_node(m_inv, 'red')
    self.__add_dependency(m_in, m_inv)

  def op_pmv(self, m, v):
    if type(m) is not Node:
      raise TypeError
    if type(v) is not Node:
      raise TypeError
    v_incr = v.incr_last_coord()
    self.__add_node(v_incr, 'magenta')
    self.__add_dependency(v, v_incr)
    self.__add_dependency(m, v_incr)

  def op_pmm2(self, m1, m2):
    """m2 = m1 * m2"""
    if type(m1) is not Node:
      raise TypeError
    if type(m2) is not Node:
      raise TypeError
    m_incr = m2.incr_last_coord()
    self.__add_node(m_incr, 'blue')
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)


  def op_pmm_d(self, A, B, C):
    """C = C - A * B"""
    if type(A) is not Node:
      raise TypeError
    if type(B) is not Node:
      raise TypeError
    if type(C) is not Node:
      raise TypeError
    m_incr = C.incr_last_coord()
    self.__add_node(m_incr, 'darkgreen')
    self.__add_dependency(A, m_incr)
    self.__add_dependency(B, m_incr)
    self.__add_dependency(C, m_incr)

  def op_pmv_d(self, A, b, c):
    """c = c - A * b"""
    if type(A) is not Node:
      raise TypeError
    if type(b) is not Node:
      raise TypeError
    if type(c) is not Node:
      raise TypeError
    v_incr = c.incr_last_coord()
    self.__add_node(v_incr, 'olivedrab2')
    self.__add_dependency(A, v_incr)
    self.__add_dependency(b, v_incr)
    self.__add_dependency(c, v_incr)




