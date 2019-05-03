from Cronometro import *

c=Cronometro()
a = input ("Ingrese el tiempo en horas, minutos y segundos (hh:mm:ss:dd)")
c.setTiempo(a)
for i in range(100):
    c.retroceder()
    print c.getTiempo()
    
