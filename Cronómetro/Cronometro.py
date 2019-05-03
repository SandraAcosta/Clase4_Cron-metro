from Hora import *
from Minuto import *
from Segundo import *
from Decima import *

class Cronometro ():
    def __init__(self):
        self.h = Hora()
        self.m = Minuto()
        self.s = Segundo()
        self.d = Decimas()

    def avanzar (self):
        self.d.avanzar()
        if self.d.getvalor() == 0:
            self.s.avanzar()
            if self.s.getvalor() == 0:
                self.m.avanzar()
                if self.m.getvalor() == 0:
                    self.h.avanzar()
                    
    def getTiempo (self):
        return "{:02d}".format(self.h.getvalor())+":"+ "{:02d}".format(self.m.getvalor())+":"+"{:02d}".format(self.s.getvalor())+":"+"{:02d}".format(self.d.getvalor())

    def retroceder(self):
        self.d.retroceder()
        if self.d.getvalor() == self.d.getTope():
            self.s.retroceder()
            if self.s.getvalor() == self.s.getTope():
                self.m.retroceder()
                if self.m.getvalor() == self.m.getTope():
                    self.h.retroceder()

    def setTiempo (self,a):
        tiempo=a.split(":")
        self.h.setValor(int (tiempo[0]))
        self.m.setValor(int (tiempo[1]))
        self.s.setValor(int (tiempo[2]))
        self.d.setValor(int (tiempo[3]))
       
        

    
