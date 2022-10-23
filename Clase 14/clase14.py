#%%
# Implemente una función ingresar_contacto() que permita guardar contactos 
# en una agenda. El programa debe solicitar al usuario el ingreso de los 
# siguientes datos: Nombre, Apellido, Teléfono, Email y un campo de 
# Observaciones (que puede usarse de manera opcional). La información 
# solicitada debe guardarse en un archivo con formato CSV (ejemplo: 
# agenda.csv). Al abrir el archivo desde una hoja de cálculo deberá verse 
# algo como lo siguiente:
# Ayuda: el formato CSV es una archivo de texto, con extensión .csv, 
# que puede abrirse desde una hoja de cálculo, donde se separan las 
# columnas por comas ‘,’ y las filas por saltos de línea ‘\n’. 
# El texto debe verse como::
# Nombre, Apellido, Teléfono, Email, Observaciones
# Juliana, Fernandez, 4422-5566, jfern@yahoo.com.ar, gerencia
# José, Pérez, 1234-5678, jose.perez@gmail.com, empleado

def ingresar_contacto(lista:list)->list:
    agenda = [input(f'{l}: ').capitalize() for l in lista]
    return agenda

def guardar_contacto(lista:list,archivo:str):
    contacto = ','.join(lista) + '\n'
    with open(archivo,'a') as f:
        f.write(contacto)

def main():
    archivo = 'agenda.csv'

    lista = ['Nombre', 'Apellido', 'Teléfono', 'Email', 'Observaciones']

    with open(archivo,'a') as f:
        if f.tell()==0:
            f.write(','.join(lista)+'\n')

    while True:
        opc=input('Para ingresar un contacto aprete cualquier letra, "q" para salir: ')
        if opc == 'q':
            break
        else:
            contacto = ingresar_contacto(lista)
            guardar_contacto(contacto,archivo)

if __name__ == '__main__':
    main()


# %%
# Implemente una función que le solicite al usuario el nombre y apellido, lea el archivo 
# agenda.csv, busque al contacto y despliegue en pantalla un resumen con toda la 
# información sobre ese contacto. En la búsqueda, debe ser indistinto el uso de 
# mayúsculas y minúsculas. 

def read_csv(nombre:str,apellido:str,archivo:str)->list:
    with open(archivo,'r') as f:
        for line in f:
            lista = line.rstrip().split(',')
            if lista[0] == nombre.strip().capitalize() and lista[1] == apellido.strip().capitalize():
                return lista
    return []

def imprimir_contacto(contacto:list):
    if len(contacto) == 0:
        print('El contacto no esta en la agenda')
    else:
        lista = ['Nombre', 'Apellido', 'Teléfono', 'Email', 'Observaciones']
        for datos,campo in zip(contacto,lista):
            print(f'{campo}: {datos}')

def main():
    archivo = 'agenda.csv'

    ingreso= input('Ingrese un contacto para buscar: <nombre>,<apellido> ').split(',')
    if len(ingreso) != 2:
        print('Datos ingresados no validos')
    else:
        nombre,apellido = ingreso
        contacto = read_csv(nombre,apellido,archivo)
        imprimir_contacto(contacto)

if __name__ == '__main__':
    main()

#%%
# Implemente una función que lea el archivo csv de contactos y genere un archivo 
# en formato txt donde guarde un resumen de todos los contactos de la agenda con 
# el siguiente formato:

# Contacto 1
# Nombre: Pablo
# Apellido: Tartaletti
# Teléfono: 23432543
# Email: p.tarta@gmail.com
# Observaciones: -

def csv2txt(archivo_csv:str,archivo_txt:str)->list:

    with open(archivo_csv,'r') as f:
        titulos = f.readline().rstrip().split(',')
        with open(archivo_txt,'w') as ftxt:
            for i,line in enumerate(f,1):
                ftxt.write(f'Contacto {i}\n')
                print(line)
                lista = line.rstrip().split(',') 
                for titulo,campo in zip(titulos,lista):
                    ftxt.write(f'{titulo}: {campo}\n')
                ftxt.write('\n')

def main():
    archivo_csv = 'agenda.csv'
    archivo_txt = 'agenda.txt'
    csv2txt(archivo_csv,archivo_txt)

if __name__ == '__main__':
    main()

#%%
# Implemente un programa que permita despliegue un menú con las siguientes opciones:
# 1. Agregar contacto
# 2. Buscar contacto
# 3. Salir
# En la opción 1 debe ejecutarse la función del ejercicio 1, en la opción 2 la 
# función del ejercicio 2 y la 3 para cerrar el programa. Si se ejecutan las 
# opciones 1 y 2, luego de completar la rutina debe volver a desplegar el menú.

def read_csv(nombre:str,apellido:str,archivo:str)->list:
    with open(archivo,'r') as f:
        for line in f:
            lista = line.rstrip().split(',')
            if lista[0] == nombre.strip().capitalize() and lista[1] == apellido.strip().capitalize():
                return lista
    return []

def imprimir_contacto(contacto:list):
    if len(contacto) == 0:
        print('El contacto no esta en la agenda')
    else:
        lista = ['Nombre', 'Apellido', 'Teléfono', 'Email', 'Observaciones']
        for datos,campo in zip(contacto,lista):
            print(f'{campo}: {datos}')

def buscar_contacto(archivo):
    ingreso= input('Ingrese un contacto para buscar: <nombre>,<apellido> ').split(',')
    if len(ingreso) != 2:
        print('Datos ingresados no validos')
    else:
        nombre,apellido = ingreso
        contacto = read_csv(nombre,apellido,archivo)
        imprimir_contacto(contacto)

def ingresar_contacto(lista:list)->list:
    agenda = [input(f'{l}: ').capitalize() for l in lista]
    return agenda

def guardar_contacto(lista:list,archivo:str):
    contacto = ','.join(lista) + '\n'
    with open(archivo,'a') as f:
        f.write(contacto)

def agregar_contacto(archivo):
    lista = ['Nombre', 'Apellido', 'Teléfono', 'Email', 'Observaciones']

    with open(archivo,'a') as f:
        if f.tell()==0:
            f.write(','.join(lista)+'\n')

    contacto = ingresar_contacto(lista)
    guardar_contacto(contacto,archivo)

def main():
    archivo = 'agenda.csv'
    func = {'1': agregar_contacto,'2':buscar_contacto}
    while True:
        opc=input('\nIngrese una opcion:\n1. Agregar contacto\n2.Buscar contacto\n3.Salir\n>  ')
        if opc == '3':
            break
        elif opc in ['1','2']:
            func[opc](archivo)
        else:
            print('Opcion no valida')
if __name__ == '__main__':
    main()


# %%
