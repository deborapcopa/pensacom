#%% Ejercicio 1

from ast import Import
import math
def sqrt(x,n):
    if n == 0:
        return x
    fn_1 = sqrt(x,n-1)
    return (fn_1 + x/fn_1)/2

def main():
    x = 20
    n = 5
    print(sqrt(x,n) , math.sqrt(x)) 

if __name__ == '__main__': 
    main()
                
#%% Ejercicio 2

d ={i:str(i) for i in range(10)}|{10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

def dec2hex(n,lista):
    dig = n//16
    resto = n%16
    if  dig==0: lista.append(d[resto])
    else:
        dec2hex(dig,lista)
        lista.append(d[resto])

def main():
    dec = 650292535 
    hexa = ['0x']
    dec2hex(dec,hexa)
    print(''.join(hexa),hex(dec))

if __name__ == '__main__':
    main()

#%% Ejercicio 2

d ={i:str(i) for i in range(10)}|{10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}

def dec2hex(n):
    dig = n//16
    resto = n%16
    if  dig < 16: return '0x' + d[dig] + d[resto]
    return dec2hex(dig) + d[resto]

def main():
    dec = 650299645
    print(dec2hex(dec) , hex(dec))

if __name__ == '__main__':
    main()
    

# %% Ejercicio 4

def construir(level):
    if level == 1:
        return 1
    return level**2 + construir(level-1)

def construir_it(h):
    acum=0
    for i in range(1,h+1):
        acum += i**2
    return acum

def main():
    h = 4
    print(construir(h),construir_it(h))

if __name__ == '__main__':
    main() 
    

# %% Ejercicio 4

import random
N = 10
lista = [random.randrange(-100,100) for _ in range(N)]
# lista = [5,3,0,6,44,-45,2,0.0001,100000]
# lista = [1]

def mini(lista):
    if len(lista) == 1:
        return lista[0]
        
    mid = len(lista) // 2
    izq = mini(lista[:mid])
    der = mini(lista[mid:])

    return der if izq > der else izq

def main():
    print(mini(lista), min(lista))

if __name__ == '__main__':
    main() 
