#%% Ejercicio 1 (INSERCIÓN ITERATIVO)

def insertion_sort(lista):
    for i in range(1,len(lista)):
        for j in reversed(range(i)):
            if lista[j] <= lista[j+1]:
                break
            else:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def main():
    lista = [5,3,0,6,44,-45,2,0.0001,100000]
    print(lista)
    insertion_sort(lista)
    print(lista)

if __name__ == '__main__':
    main()

    
# %% Ejercicio 1 (INSERCIÓN RECURSIVO)

def comp(lista,j):
    if j>0 and lista[j]<lista[j-1]:
        lista[j],lista[j-1]=(lista[j-1],lista[j])
        comp(lista,j-1)

def insertion_sort_rec(lista,ind=1):
    if ind!=len(lista):
        comp(lista,ind)
        insertion_sort_rec(lista,ind+1)
            
def main():
    lista = [5,3,0,6,44,-45,2,0.0001,100000]
    print(lista)
    insertion_sort_rec(lista)
    print(lista)

if __name__ == '__main__':
    main()

# %% Ejercicio 1 (SELECCIÓN RECURSIVO 1)

def mini(lista):
    mini = lista[0]
    ind = 0
    for i,l in enumerate(lista):
        if l<mini:
            mini,ind = l,i
    return mini,ind

def selection_sort_rec(lista):
    # caso base 
    if len(lista)==1:
        return lista
    # si la lista tiene mas de 2, calcula el mínimo e intercambia 
    m,i = mini(lista)
    lista[0], lista[i] = lista[i], lista[0]
    # retorna una lista con el mínimo adelante y el resto ordenada
    return [lista[0]] + selection_sort_rec(lista[1:])
        
def main():
    lista = [7,3, 7, 9, 1, 5]
    print(lista)
    print(selection_sort_rec(lista))
    

if __name__ == '__main__':
    main()

# %% Ejercicio 1 (SELECCIÓN RECURSIVO 2)

def mini(lista):
    mini = lista[0]
    ind = 0
    for i,l in enumerate(lista):
        if l<mini:
            mini,ind = l,i
    return mini,ind

def selection_sort_rec(lista,ind=0):
    if ind!=len(lista)-1:
        m,i = mini(lista[ind:])
        lista[ind],lista[i+ind] = lista[i+ind],lista[ind]
        selection_sort_rec(lista,ind+1)
            
def main():
    lista = [5,3,0]
    print(lista)
    selection_sort_rec(lista)
    print(lista)

if __name__ == '__main__':
    main()

# %% Ejercicio 1 (BURBUJEO RECURSIVO)

def comp(lista,j=1):
    if j<=len(lista)-1:
        if lista[j-1] > lista[j]:
            lista[j],lista[j-1] = lista[j-1],lista[j]
        return comp(lista,j+1)
    return lista    #lista con el mayor al final

def bubble_sort_rec(lista,ind = None):
    if ind == None: ind = len(lista)-1
    if ind>0:
        lista[:ind+1] = comp(lista[:ind+1])
        bubble_sort_rec(lista,ind-1)
            
def main():
    lista = [5,3,0,6,44,-45,2,0.0001,100000]
    print(lista)
    bubble_sort_rec(lista)
    print(lista)

if __name__ == '__main__':
    main()

# %% Ejerecicio 2

def ordenar_listas(lista_old,campo):
    lista = lista_old[:]
    for i in reversed(range(len(lista))):
        for j in range(1,i+1):
            if lista[j-1][campo]>lista[j][campo]:
                lista[j],lista[j-1] = lista[j-1],lista[j]
    return lista

def main():
    d={'nombre':0,'puntos':1}
    listas = [['Surim',2],['Dacta',6],['Cronet',4]]
    campo = input('Seleccione [nombre/puntos]: ').lower()
    
    print(listas ,'\n', ordenar_listas(listas, d[campo]))

if __name__ == '__main__':
    main()

# %% Ejercicio 3

# En el campus está el archivo de prueba enigma.txt
def ordenar_dict(dic):
    lista = list(dict.items(dic))
    for i in reversed(range(len(lista))):
        for j in range(1,i+1):
            if lista[j-1][1]>lista[j][1]:
                lista[j],lista[j-1] = lista[j-1],lista[j]
    return list(reversed(lista))

def main():
    with open('ruinas_circulares.txt') as f:
        d = {}
        for line in f:
            lista = [pal.strip('-_.,:;?!¿¡\'()').lower() for pal in line.rstrip().split()]
            
            for pal in lista: 
                if pal not in d: d[pal]=1  
                else: d[pal]+=1

    lista = ordenar_dict(d)

    with open('ruinas_circulares_frec.txt','w') as f:
        for pal in lista:
            f.write(f'{pal[0]} {pal[1]}\n')

if __name__ == '__main__':
    main()
