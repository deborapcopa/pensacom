
def busqueda_rango(xlist, xmin, xmax):
    '''
    xlist: lista de números ordenada.
    xmin y xmax: límites del intervalo.
    '''
    lista_encontrados=[]
    for i,elem in enumerate(xlist):      # iteramos la lista (desde el minimo)
        if valor_min< elem <= valor_max: # elemento actual está en el rango?
            lista_encontrados.append(i)  # si elemento está, lo agregamos
    if  len(lista_encontrados)==0:       # Si hay 0 encontrados, devolvemos -1
      return -1
    else: 
      return lista_encontrados

def main():
  
    x = [91, 62, 37, 53, 77, 47, 100, 4, 25, 98, 86, 88, 56, 82, 89, 76, 59, 13, 73, 75]
    x.sort()
    valor_min= 2
    valor_max= 70

    rango = busqueda_rango(x,valor_min,valor_max)
    msj = x[rango[0]:rango[-1]+1] if not rango ==-1 else 'Ninguno' # 
    print(f'Los elementos son: {msj}\n{x}')
    print(rango[0],rango[-1]+1)

if __name__ == '__main__':
    main()
