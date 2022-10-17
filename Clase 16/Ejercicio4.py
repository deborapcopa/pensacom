
def sum_vectors(v1:list, v2:list) -> list:
  '''
  Suma dos listas numericas, v1 y v2, de igual longitud 
  Devuelve el vector con la suma v1+v2
  '''
  assert isinstance(v1,list) and isinstance(v2,list),'the type of vectors must be list'
#   for v in v1:
#     if not(type(v) in [int,float]):
#         raise AssertionError('first vector must be numeric')
#   assert sum([isinstance(v,[int,float]) for v in v1]) == len(v1),'first vector must be numeric'
  assert all([isinstance(v,(int,float)) for v in v1]),'first vector must be numeric'
  assert all([isinstance(v,(int,float)) for v in v2]),'second vector must be numeric'

  assert len(v1) == len(v2),'operands must be same length'

  return [e1+e2 for e1,e2 in zip(v1,v2)]

def enter_vectors()-> list:
  '''
  Registra dos vectores por consola. 
  Las componentes ingresadas para cada vector 
  se separan con espacios (ej: 2 3 7 2.5 ).
  Retorna los dos vectores como listas de str
  '''
  v1 = input('Ingrese el vector v1: ').split()
  v2 = input('Ingrese el vector v2: ').split()
  return [float(v) for v in v1], [float(v) for v in v2]

def main():
    while True:
        try:
            v1,v2 = enter_vectors()
            v3 = sum_vectors(v1,v2)
        except AssertionError as e:
            print(e)
        except ValueError:
            print('Enter numeric values in vector')
        else:
            break
    print(v3)

if __name__ == '__main__':
    assert sum_vectors([1,0],[-1,2]) == [0,2]
    try:
        sum_vectors([1],[1,2])
    except AssertionError as e:
        assert isinstance(e, AssertionError)

