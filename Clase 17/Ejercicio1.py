def minmax_search(lista):
    mini = maxi= lista[0]
    imin = imax = 0
    for i,l in enumerate(lista):
        if l > maxi: maxi,imax = l, i
        if l < mini: mini,imin = l, i
    return (maxi,imax),(mini,imin)

def main():
    lista = [91, 62, 37, 53, 77, 47, 100, 4, 25, 98, 86, 88, 56, 82, 89, 76, 59, 13, 73, 75]
    maxi , mini = minmax_search(lista)
    print(min(lista), mini ,max(lista), maxi)

if __name__ == '__main__':
    main()
