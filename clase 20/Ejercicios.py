#%%
# Implemente un código que cree la clase “Personaje” cuyos atributos son nombre, 
# edad y con el método saludar(). El método debe imprimir en pantalla: 
# "Hola, soy {Nombre} y tengo {edad} años"
# Cree dos Personajes diferentes y hágalos saludar

class Personaje:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f' Hola, como estas? soy {self.nombre} y tengo {self.edad} años')

    def __str__(self):
        return f'Soy {self.nombre} y tengo {self.edad} años'

def main():
    juana = Personaje('Juana',50)
    claudia = Personaje('Claudia',35)

    juana.saludar()
    claudia.saludar()
    print(juana)
    print(claudia)

if __name__ == '__main__':
    main()

# %%
# Modifique la clase del ejercicio anterior de forma tal que 
# pueda recibir una lista de frases. También defina el método 
# hablar() de modo tal que elija aleatoriamente una de las 
# frases y la imprima en pantalla.

# Cree dos personajes Homero y Bart, instanciandolos con las 
# siguientes listas:

import random

class Personaje:
    def __init__(self, nombre, edad,frases):
        self.nombre = nombre
        self.edad = edad
        self.frases = frases

    def hablar(self):
        print(random.choice(self.frases))

    def saludar(self):
        print(f' Hola, como estas? soy {self.nombre} y tengo {self.edad} años')
        
    def __str__(self):
        return f'Soy {self.nombre} y tengo {self.edad} años'

def main():
    frases_homero = ['¡No se rían de mí, pueden tener un hijo igual' ,
                    'La vida es un fracaso tras otro hasta que empiezas a desear que Flanders se muera', 
                    'Ese perro tiene la cola peluda!']

    frases_bart = ['¡Ay, caramba!' , '¡Yo no fui! ' , 
                  'No duermo, payaso me come']

    homero = Personaje('Homero',35, frases_homero)
    bart = Personaje('Bart',12, frases_bart)

    homero.hablar()
    bart.hablar()

if __name__ == '__main__':
    main()

# %%
# Defina nuevamente la clase pero incluyendo un método agregar_frase() 
# que permita agregar una frase.

# Cree un personaje nuevo, Lisa, instanciando solo el nombre y la edad. 
# Luego, utilice el método agregar_frases() para agregar las siguientes 
# frases

# frase 1:
# '¿Ser yo misma? He sido yo misma durante 8 años y no ha funcionado.'

# frase 2:
# 'No se dejen engañar! Es la misma tonta Stacy Malibú con un sombrero distinto, sigue teniendo todos los horrendos estereotipos de antes.'


import random

class Personaje:
    def __init__(self, nombre, edad, frases = []):
        self.nombre = nombre
        self.edad = edad
        self.frases = frases

    def set_phrase(self,frase):
        if type(frase) == str: self.frases.append(frase) 
        else: self.frases.extend(frase)

    def hablar(self):
        print(random.choice(self.frases) if len(self.frases) != 0 else '')

    def saludar(self):
        print(f' Hola, como estas? soy {self.nombre} y tengo {self.edad} años')
        
    def __str__(self):
        return f'Soy {self.nombre} y tengo {self.edad} años'

def main():
    frase1 = '¿Ser yo misma? He sido yo misma durante 8 años y no ha funcionado.'
    frase2 = ['Hola','No se dejen engañar! Es la misma tonta Stacy Malibú con un sombrero distinto, sigue teniendo todos los horrendos estereotipos de antes.']

    frases_homero = ['¡No se rían de mí, pueden tener un hijo igual' ,
                    'La vida es un fracaso tras otro hasta que empiezas a desear que Flanders se muera', 
                    'Ese perro tiene la cola peluda!']

    frases_bart = ['¡Ay, caramba!' , '¡Yo no fui! ' , 
                  'No duermo, payaso me come']

    homero = Personaje('Homero',35, frases_homero)
    bart = Personaje('Bart',12, frases_bart)

    homero.hablar()
    bart.hablar()

    lisa = Personaje('Lisa',8)
    print(lisa.frases)
    lisa.hablar()
    lisa.set_phrase(frase1)
    print(lisa.frases)
    lisa.hablar()
    lisa.set_phrase(frase2)
    print(lisa.frases)



if __name__ == '__main__':
    main()
