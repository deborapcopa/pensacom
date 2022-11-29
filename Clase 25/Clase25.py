#%%
# El objetivo del ejercicio es poder crear objetos que guarden la información
#  de tiempo y realizar diferentes operaciones entre distintos objetos de la 
#  misma clase, pero sólo válidas durante el día actual.En primer lugar, 
#  defina una clase DayTime tal que pueda inicializarse con las horas, 
#  minutos y segundos del día definidas en la instanciación, o bien 0 horas, 
#  0 minutos y 0 segundos por omisión.
# Defina un método que gethour() que devuelva una cadena de texto con la hora 
# actual con el formato ‘hh:mm:ss’.
# Defina un método que muestre información descriptiva de la clase y otro que 
# muestre cómo fue instanciado el objeto actual.
# Genere un objeto clase DayTime definiendo sus atributos iniciales a partir
# de la hora actual. Luego imprima en la hora almacenada, la descripción del 
# objeto y su forma de instanciarlo. 
# Ayuda: con import datetime, puede obtenerse la hora actual 
# tnow = datetime.datetime.now(). 
# Luego las horas tnow.hour, minutos tnow.minute y segundos tnow.second.

import datetime

class DayTime:
    def __init__(self,h = 0, m = 0, s = 0):
        self.time = {'h':h,'m':m,'s':s}

    def __str__(self):
        return f'{self.time["h"]:02d}:{self.time["m"]:02d}:{self.time["s"]:02d}'

    def __repr__(self):
        return f'DayTime({self.time["h"]},{self.time["m"]},{self.time["s"]})'

    def __getitem__(self,item):
        return self.time[item]

    def __setitem__(self,item,value):
        assert item in ['h','m','s'], 'To set time must use \"h\",\"m\" or \"s\"'
        if item == 'h': assert 0 <= value <= 23, 'Hour must be less than 23 and positive'
        if item == 'm': assert 0 <= value <= 59, 'Minutes must be less than 59 and positive'
        if item == 's': assert 0 <= value <= 59, 'Seconds must be less than 59 and positive'

        self.time[item] = value

 # --------------comp----------------------
    def __eq__(self, o: object) -> bool:
        return True if self.time == o.time else False

    def __ne__(self, o: object) -> bool:
        return not self == o
        # return True if self.time != o.time else False

    def __lt__(self, o: object) -> bool:
        ss = self.time['s'] + self.time['m'] * 60  + self.time['h'] * 60**2 
        os = o.time['s'] + o.time['m'] * 60  + o.time['h'] * 60**2 
        return True if ss<os else False

        # if   self.time['h'] > o.time['h']: return False
        # elif self.time['h'] < o.time['h']: return True
        
        # elif self.time['m'] > o.time['m']: return False
        # elif self.time['m'] < o.time['m']: return True
        
        # elif self.time['s'] >= o.time['s']: return False
        # else: return True

    def __gt__(self, o: object) -> bool:
        return False if (self < o) or (self == o) else True
        # if   self.time['h'] > o.time['h']:   return True
        # elif self.time['h'] < o.time['h']: return False
        
        # elif self.time['m'] > o.time['m']: return True
        # elif self.time['m'] < o.time['m']: return False
        
        # elif self.time['s'] > o.time['s']: return True
        # else: return False

    def __le__(self, o: object) -> bool:
        return True if not self > o else False
        # if   self.time['h'] > o.time['h']:   return False
        # elif self.time['h'] < o.time['h']: return True
        
        # elif self.time['m'] > o.time['m']: return False
        # elif self.time['m'] < o.time['m']: return True
        
        # elif self.time['s'] > o.time['s']: return False
        # else: return True

    def __ge__(self, o: object) -> bool:
        return True if not self < o else False

    #     if   self.time['h'] > o.time['h']:   return True
    #     elif self.time['h'] < o.time['h']: return False
        
    #     elif self.time['m'] > o.time['m']: return True
    #     elif self.time['m'] < o.time['m']: return False
        
    #     elif self.time['s'] >= o.time['s']: return True
    #     else: return False   
 # -------------------------------------------
    def __add__(self,o:object):
        ss = self.time2sec() 
        os = o.time2sec()
        suma = ss+os
        
        assert suma < 24*60**2, 'EXCEEDING MAXIMUM DAY HOURS'
        h,m,s = self.sec2time(suma)
        return DayTime(h,m,s)        

    def time2sec(self):
        return self.time['s'] + self.time['m'] * 60  + self.time['h'] * 60**2 

    def sec2time(self,value):
        horas = value//60//60
        minutos = (value - horas *60*60) // 60
        segundos = value - minutos * 60 - horas *60*60
        return horas,minutos,segundos

    def __sub__(self,o:object):
        ss = self.time2sec() 
        os = o.time2sec()
        resta = ss-os
        
        assert resta >= 0, 'INVALID SUBTRACTION'
        h,m,s = self.sec2time(resta)
        return DayTime(h,m,s)

tnow = datetime.datetime.now()
t = DayTime(tnow.hour,tnow.minute,tnow.second)
print(t,'\n', repr(t),'\n', t['h'],'\n',t['m'],'\n',t['s'])
t['m'] = 2
print(t,'\n', repr(t),'\n', t['h'],'\n',t['m'],'\n',t['s'])

t = DayTime(5,2,21)
t2 = DayTime(5,2,21)
print(t>t2,'\n',t>=t2,'\n',t<t2,'\n',t<=t2,'\n', t == t2,'\n', t!=t2,'\n')
print(t+t2,'\n',t-t2)

# %%

class Empleado:
    def __init__(self,name:str,id:int,tin: object,tout: object):
        self.name = name
        self.id = id
        self.tin = tin
        self.tout = tout
        
t1in = DayTime(8,2,30)
t1out = DayTime(15,2,30)

t2in = DayTime(7,2,30)
t2out = DayTime(8,0,0)

t3in = DayTime(8,0,0)
t3out = DayTime(18,2,30)

E1 = Empleado('Pedro Fernandez', 10089,t1in,t1out)       
E2 = Empleado('Juan Perez', 10089,t2in,t2out)       
E3 = Empleado('Ana Goette', 10088,t3in,t3out)       
E = [E1,E2,E3]

tstart = DayTime(8,0,0)#horario de entrada
texit = DayTime(17,0,0)#horario de salida
ttot = texit-tstart #total de horas a trabajar

for e in E:
    if e.tin > tstart:
        print(f'El empleado {e.name} llego {e.tin - tstart} tarde')
    if e.tout - e.tin < ttot:
        print(f'El empleado {e.name} trabajo {ttot- (e.tout - e.tin)} menos')

# %%
