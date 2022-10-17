def binarysearch(lista, target):
    inf, sup = 0, len(lista) - 1 # inicializo los indices limites de la lista
    while inf <= sup:
        mid = inf + (sup-inf) // 2    # indice medio redondeado para abajo
        print(inf,sup,mid)
        if lista[mid] == target:
            return mid
        if lista[mid] < target:
            inf = mid + 1       # me quedo con la 2 mitad
        else: sup = mid - 1     # me quedo con la primer mitad
    return -1

def main():
    lista = [91, 62, 37, 53, 77, 47, 100, 4, 25, 98, 86, 88, 56, 82, 89, 76, 59, 13, 73, 75]
    lista.sort()
    target = 91
    ind = binarysearch(lista,target)
    print( lista[ind] if ind!=-1 else 'no se encontro' ,target)

if __name__ == '__main__':
    main()
