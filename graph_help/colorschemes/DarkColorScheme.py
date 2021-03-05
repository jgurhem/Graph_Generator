from .DefaultColorScheme import DefaultColorScheme

class DarkColorScheme(DefaultColorScheme):
  def __init__(self):
    self.colors = dict()
    self.colors['background'] = 'black'
    self.colors['edge'] = 'white'
    self.colors['fontcolor'] = 'black'
    self.colors['initv'] = 'grey65'
    self.colors['initm'] = 'grey65'
    self.colors['inv'] = 'red'
    self.colors['pmv'] = 'magenta'
    self.colors['pmm1'] = 'blue'
    self.colors['pmm2'] = 'blue'
    self.colors['pmm_d'] = 'darkgreen'
    self.colors['pmv_d'] = 'darkolivegreen3'
    self.colors['sls'] = 'cyan3'

