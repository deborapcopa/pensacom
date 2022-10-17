
def linear_search(alumnos,e,i):
    for data in alumnos:
        if data[i] == e:
            return data
    return ()

def search(alumnos,e,criterio):
    if criterio.lower() == 'l':
        return linear_search(alumnos,e,1)
    else:
        return linear_search(alumnos,e,2)

def main():
    alumnos=[('Tomas',2324,30123445),('Delfina',1323,40223247)]
    criterio, elem = input('Ingrese la busqueda: ').split()
    info = search(alumnos,int(elem),criterio)
    print('***Estudiante*** ')
    if len(info)!=0: 
        print( f'Nombre: {info[0]}\nLegajo: {info[1]}\nDNI: {info[2]}\n')
    else: print( f'Nombre: -\nLegajo: -\nDNI: -\n')

if __name__ == '__main__':
    main()
