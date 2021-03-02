from .DefaultColorScheme import DefaultColorScheme

class DarkColorScheme(DefaultColorScheme):
  def __init__(self):
    self.colors = dict()
    self.colors['background'] = 'black'
    self.colors['fontcolor'] = 'black'
    self.colors['initv'] = 'white'
    self.colors['initm'] = 'white'
    self.colors['inv'] = 'red'
    self.colors['pmv'] = 'magenta'
    self.colors['pmm1'] = 'blue'
    self.colors['pmm2'] = 'blue'
    self.colors['pmm_d'] = 'darkgreen'
    self.colors['pmv_d'] = 'darkolivegreen3'
    self.colors['sls'] = 'cyan3'

