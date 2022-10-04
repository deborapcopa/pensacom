#%% Ejercicio 3

import random        

def random_vector(n:int)->list:
  '''
  Entradas:
  n: número de elementos de la lista a generar
  Salidas:
  x: lista cuyos elementos son variables aleatorias gaussianas (media = 0, desvio = 1)
  '''
  x=[]
  for j in range(n):
    x.append(random.gauss(0,1))
  return x

def count_x(x:list, bmin:float, bmax:float)->int:
  '''
   Entradas:
   x: lista de numeros
   bmin: limite inferior (no incluido)
   bmax: límite superior (incluido). Supone bmin < bmax
   Retorno: 
   count: cantidad de muestras de x que están dentro del intervalo definido entre bmin y bmax
  '''
  count=0
  for xi in x:
      if bmin < xi <= bmax:
        count +=1  
  return count
  
def hist(x:list,m:int)->list:
  '''
   Entradas
   --------
   x: lista de números
   m: número positivo de intervalos (bins) en los que se divide uniformemente el rango total de x [xmin;xmax]
   Retorno
   -------
   h: lista de largo m cuyos elementos contienen la cantidad de muestras de x
      en cada intervalo en el que se partió todo el espacio de x
  '''
  xmin, xmax = min(x), max(x)
  wbin=(xmax-xmin)/m   # ancho de cada bin
  h=[]
  for k in range(m):
    inf = xmin+k*wbin # limite inferior del k-esimo bin
    sup = xmin+(k+1)*wbin # limite superior del k-esimo bin
    h.extend([count_x(x, inf, sup)]) # o bien, h.append(count_x(x, inf, sup)) 
  return h

def hist_ascii(h:list):
  '''
   Entrada:
    h: lista de números enteros
   Descripción: imprime en consola una tira de caracteres proporcional al valor de cada entero en h 
   Retorno: None  
  '''
  char_style = chr(9619) #'▓' # caracter unicode para imprimir histograma
  n_chars = 80 # cantidad máxima de caracteres por línea 
  scale = n_chars/max(h)
  for elem in h:
    p = round(elem*scale)
    print(p * char_style)  # imprime nro de caracteres proporcional a cada h[k]

def main():
    # Cálculo del hstograma (barras cuya altura representan frecuencia de aparicion de c/muestra en cada bin)
    n = 5000  # cantidad de muestras aleatorias 
    m = 50    # número de bins totales
    x = random_vector(n)  # vector de numeros aleatorios (tipo float)

    h = hist(x, m)       # histograma
    hist_ascii(h)         # gráfico  

# funciones de test
def test_random_vector():
  print('\nTest de random_vector:')

  if len(random_vector(5)) != 5:
    print('Error del largo')
  else: print('OK')

  L = random_vector(10)
  if type(random.choice(L)) != float:
    print('Error de tipo')
  else: print('OK')

def test_count_x():
  print('\nTest de count_x:')

  L = [1,2,3,4,5,6,7,8] 
  if count_x(L,2,7) != 5:
    print('Error de cuenta en intervalo')
  else: print('OK')

  L = [1,2,3,4,5,6,7,8] 
  if count_x(L,9,70) != 0:
    print('Error de cuenta fuera de intervalo')
  else: print('OK')

  L = [1,2,3,4,5,6,7,8] 
  if count_x(L,-1,10) != 8:
    print('Error de cuenta dentro del intervalo completo')
  else: print('OK')

  L = [] 
  if count_x(L,-1,10) != 0:
    print('Error de cuenta de lista vacia')
  else: print('OK')

def test_hist():
  L = [1,2,3,4,5,6,7,80] 
  if hist(L,3) != [6,0,1]:
    print('Error de generacion de bins')
  else: print('OK')

def test_hist_ascii():
  L = [1,2,3,4,5,6,7,8] 
  hist_ascii(L)

if __name__ == "__main__":
  main()
