import sys
from abc import abstractmethod

if sys.version_info.major == 2:
  from abc import ABCMeta
  class ABC:
    __metaclass__ = ABCMeta
elif sys.version_info.major == 3:
  from abc import ABC

class AbstractNode(ABC):
  def __init__(self, name, coord):
    super(AbstractNode, self).__init__()
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

  def __str__(self):
    return self.name + " " + str(self.coord)


class Node(AbstractNode):
  def __init__(self, name, coord):
    super(Node, self).__init__(name, coord)
    if len(coord) < 2:
      raise IndexError

  def incr_last_coord(self):
    new_coord = list(self.coord)
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

