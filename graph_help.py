from abc import ABC, abstractmethod
from graphviz import Digraph

class AbstractNode(ABC):
  def __init__(self, name, coord):
    super().__init__()
    if type(coord) is not list:
      raise TypeError
    self.name = name
    self.coord = coord

  @abstractmethod
  def get_id(self):
    pass

  @abstractmethod
  def get_label(self):
    pass


class Node(AbstractNode):
  def __init__(self, name, coord):
    super().__init__(name, coord)
    if len(coord) < 2:
      raise IndexError

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


class NodeSimple(AbstractNode):
  def get_id(self):
    id_ = self.name
    for i in range(len(self.coord)):
      id_ += "-" + str(self.coord[i])
    return id_

  def get_label(self):
    return self.get_id()


class Graph:
  def __init__(self, gname):
    self.G = Digraph(gname)

  def graph_print(self):
    print(self.G)

  def __add_node(self, node, color):
    if not isinstance(node, AbstractNode):
      raise TypeError
    self.G.node(node.get_id(), node.get_label(), color = color, style='filled', fontcolor='white')

  def __add_dependency(self, fro, to):
    if not isinstance(fro, AbstractNode):
      raise TypeError
    if not isinstance(to, AbstractNode):
      raise TypeError
    self.G.edge(fro.get_id(), to.get_id())

  def op_vector_init(self, v):
    if not isinstance(v, AbstractNode):
      raise TypeError
    self.__add_node(v, 'black')

  def op_matrix_init(self, m):
    if not isinstance(m, AbstractNode):
      raise TypeError
    self.__add_node(m, 'black')

  def op_matrix_inv(self, m_in, m_inv):
    if not isinstance(m_in, AbstractNode):
      raise TypeError
    if not isinstance(m_inv, AbstractNode):
      raise TypeError
    self.__add_node(m_inv, 'red')
    self.__add_dependency(m_in, m_inv)

  def op_pmv(self, m, v):
    if not isinstance(m, AbstractNode):
      raise TypeError
    if not isinstance(v, AbstractNode):
      raise TypeError
    v_incr = v.incr_last_coord()
    self.__add_node(v_incr, 'magenta')
    self.__add_dependency(v, v_incr)
    self.__add_dependency(m, v_incr)

  def op_pmm1(self, m1, m2):
    """m1 = m1 * m2"""
    if not isinstance(m1, AbstractNode):
      raise TypeError
    if not isinstance(m2, AbstractNode):
      raise TypeError
    m_incr = m1.incr_last_coord()
    self.__add_node(m_incr, 'blue')
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)

  def op_pmm2(self, m1, m2):
    """m2 = m1 * m2"""
    if not isinstance(m1, AbstractNode):
      raise TypeError
    if not isinstance(m2, AbstractNode):
      raise TypeError
    m_incr = m2.incr_last_coord()
    self.__add_node(m_incr, 'blue')
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)

  def op_pmm_d(self, A, B, C):
    """C = C - A * B"""
    if not isinstance(A, AbstractNode):
      raise TypeError
    if not isinstance(B, AbstractNode):
      raise TypeError
    if not isinstance(C, AbstractNode):
      raise TypeError
    m_incr = C.incr_last_coord()
    self.__add_node(m_incr, 'darkgreen')
    self.__add_dependency(A, m_incr)
    self.__add_dependency(B, m_incr)
    self.__add_dependency(C, m_incr)

  def op_pmv_d(self, A, b, c):
    """c = c - A * b"""
    if not isinstance(A, AbstractNode):
      raise TypeError
    if not isinstance(b, AbstractNode):
      raise TypeError
    if not isinstance(c, AbstractNode):
      raise TypeError
    v_incr = c.incr_last_coord()
    self.__add_node(v_incr, 'olivedrab2')
    self.__add_dependency(A, v_incr)
    self.__add_dependency(b, v_incr)
    self.__add_dependency(c, v_incr)




