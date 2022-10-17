import numpy as np

def db(p):
  '''
  Recibe un valor de potencia p [watts] y lo devuelve en decibeles [dB]
  '''
  assert isinstance(p,float),f'Must be numeric, not {type(p)}'
  assert p>=0,'Domain error'
  return 10 * np.log10(p)

def db2(p):
  '''
  Recibe un valor de potencia p [watts] y lo devuelve en decibeles [dB]
  '''
  if not isinstance(p,float):
    raise TypeError(f'Must be numeric, not {type(p)}')
  if not p>=0:
    raise ValueError('Domain error')
  return 10 * np.log10(p)

