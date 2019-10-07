from .Node import AbstractNode
from .AbstractGraph import AbstractGraph
from Pegasus.DAX3 import *
import sys
import random

class Graph(AbstractGraph):
  def __init__(self, gname, options):
    self.gname = gname
    self.bs = int(options.datasize / options.N)
    self.G = ADAG(gname)
    self.jobs = dict()
    random.seed(1)

  def graph_print(self):
    self.G.writeXML(sys.stdout)

  def __create_job(self, node, name):
    nid = node.get_id()
    if nid in self.jobs:
      raise NotImplementedError
    self.jobs[nid] = Job(namespace=self.gname, name=name)
    self.G.addJob(self.jobs[nid])
    return self.jobs[nid]

  def __add_dependency(self, fro, to):
    p_id = fro.get_id()
    c_id = to.get_id()
    self.G.addDependency(Dependency(parent = self.jobs[p_id], child = self.jobs[c_id]))


  def op_vector_init(self, v):
    super(Graph, self).op_vector_init(v)
    j = self.__create_job(v, "initv")
    a = File(v.get_label())
    j.uses(a, link=Link.OUTPUT)
    j.addArguments(str(self.bs), str(random.random()), a)

  def op_matrix_init(self, m):
    super(Graph, self).op_matrix_init(m)
    j = self.__create_job(m, "initm")
    a = File(m.get_label())
    j.uses(a, link=Link.OUTPUT)
    j.addArguments(str(self.bs), str(self.bs), str(random.random()), a)

  def op_matrix_inv(self, m_in, m_inv):
    super(Graph, self).op_matrix_inv(m_in, m_inv)
    j = self.__create_job(m_inv, "inv_gj")
    self.__add_dependency(m_in, m_inv)
    a = File(m_in.get_label())
    j.uses(a, link=Link.INPUT)
    inv = File(m_inv.get_label())
    j.uses(inv, link=Link.OUTPUT)
    j.addArguments(str(self.bs), a, inv)

  def op_pmv(self, m, v):
    super(Graph, self).op_pmv(m, v)
    v_incr = v.incr_last_coord()
    j = self.__create_job(v_incr, "pmv")
    self.__add_dependency(v, v_incr)
    self.__add_dependency(m, v_incr)
    a_f = File(m.get_label())
    j.uses(a_f, link=Link.INPUT)
    v_f = File(v.get_label())
    j.uses(v_f, link=Link.INOUT)
    j.addArguments(str(self.bs), a_f, v_f)

  def op_pmm1(self, m1, m2):
    """m1 = m1 * m2"""
    super(Graph, self).op_pmm1(m1, m2)
    m_incr = m1.incr_last_coord()
    j = self.__create_job(m_incr, "pmm1")
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)
    m1_f = File(m1.get_label())
    j.uses(m1_f, link=Link.INOUT)
    m2_f = File(m2.get_label())
    j.uses(m2_f, link=Link.INPUT)
    j.addArguments(str(self.bs), m1_f, m2_f)

  def op_pmm2(self, m1, m2):
    """m2 = m1 * m2"""
    super(Graph, self).op_pmm2(m1, m2)
    m_incr = m2.incr_last_coord()
    j = self.__create_job(m_incr, "pmm2")
    self.__add_dependency(m1, m_incr)
    self.__add_dependency(m2, m_incr)
    m1_f = File(m1.get_label())
    j.uses(m1_f, link=Link.INPUT)
    m2_f = File(m2.get_label())
    j.uses(m2_f, link=Link.INOUT)
    j.addArguments(str(self.bs), m1_f, m2_f)

  def op_pmm_d(self, A, B, C):
    """C = C - A * B"""
    super(Graph, self).op_pmm_d(A, B, C)
    m_incr = C.incr_last_coord()
    j = self.__create_job(m_incr, "pmm_d")
    self.__add_dependency(A, m_incr)
    self.__add_dependency(B, m_incr)
    self.__add_dependency(C, m_incr)
    A_f = File(A.get_label())
    j.uses(A_f, link=Link.INPUT)
    B_f = File(B.get_label())
    j.uses(B_f, link=Link.INPUT)
    C_f = File(C.get_label())
    j.uses(C_f, link=Link.INOUT)
    j.addArguments(str(self.bs), A_f, B_f, C_f)

  def op_pmv_d(self, A, b, c):
    """c = c - A * b"""
    super(Graph, self).op_pmv_d(A, b, c)
    v_incr = c.incr_last_coord()
    j = self.__create_job(v_incr, "pmv_d")
    self.__add_dependency(A, v_incr)
    self.__add_dependency(b, v_incr)
    self.__add_dependency(c, v_incr)
    A_f = File(A.get_label())
    j.uses(A_f, link=Link.INPUT)
    b_f = File(b.get_label())
    j.uses(b_f, link=Link.INPUT)
    c_f = File(c.get_label())
    j.uses(c_f, link=Link.INOUT)
    j.addArguments(str(self.bs), A_f, b_f, c_f)


