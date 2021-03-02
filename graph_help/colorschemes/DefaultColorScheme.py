import sys

if sys.version_info.major == 2:
  from abc import ABCMeta
  class ABC:
    __metaclass__ = ABCMeta
elif sys.version_info.major == 3:
  from abc import ABC


class DefaultColorScheme(ABC):
  def __init__(self):
    self.colors = dict()
    self.colors['background'] = 'white'
    self.colors['fontcolor'] = 'white'
    self.colors['initv'] = 'black'
    self.colors['initm'] = 'black'
    self.colors['inv'] = 'red'
    self.colors['pmv'] = 'magenta'
    self.colors['pmm1'] = 'blue'
    self.colors['pmm2'] = 'blue'
    self.colors['pmm_d'] = 'darkgreen'
    self.colors['pmv_d'] = 'darkolivegreen3'
    self.colors['sls'] = 'cyan3'

  def __getitem__(self, arg):
    return self.colors[arg]


