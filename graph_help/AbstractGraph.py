import sys
from .Node import AbstractNode
from abc import abstractmethod

if sys.version_info.major == 2:
  from abc import ABCMeta
  class ABC:
    __metaclass__ = ABCMeta
elif sys.version_info.major == 3:
  from abc import ABC


class AbstractGraph(ABC):

  @abstractmethod
  def graph_print(self):
    pass

  @abstractmethod
  def op_vector_init(self, v):
    if not isinstance(v, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_matrix_init(self, m):
    if not isinstance(m, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_matrix_inv(self, m_in, m_inv):
    if not isinstance(m_in, AbstractNode):
      raise TypeError
    if not isinstance(m_inv, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_pmv(self, m, v):
    """v = m * v"""
    if not isinstance(m, AbstractNode):
      raise TypeError
    if not isinstance(v, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_pmm1(self, m1, m2):
    """m1 = m1 * m2"""
    if not isinstance(m1, AbstractNode):
      raise TypeError
    if not isinstance(m2, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_pmm2(self, m1, m2):
    """m2 = m1 * m2"""
    if not isinstance(m1, AbstractNode):
      raise TypeError
    if not isinstance(m2, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_pmm_d(self, A, B, C):
    """C = C - A * B"""
    if not isinstance(A, AbstractNode):
      raise TypeError
    if not isinstance(B, AbstractNode):
      raise TypeError
    if not isinstance(C, AbstractNode):
      raise TypeError

  @abstractmethod
  def op_pmv_d(self, A, b, c):
    """c = c - A * b"""
    if not isinstance(A, AbstractNode):
      raise TypeError
    if not isinstance(b, AbstractNode):
      raise TypeError
    if not isinstance(c, AbstractNode):
      raise TypeError



