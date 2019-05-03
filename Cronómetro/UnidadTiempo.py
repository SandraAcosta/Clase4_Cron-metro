class UnidadTiempo():
    def __init__(self):# self referencia a objeto por dentro de la clase
        self.valor = 0
        self.tope = 0

    def avanzar(self):
        if self.valor < self.tope:
            self.valor += 1
        else:
            self.valor = 0 #tope el valor vuele a 0

    def retroceder(self):
        if self.valor == 0:
            self.valor = self.tope
        else:
            self.valor -= 1

    def getvalor(self):
        return self.valor
    
    def setValor(self,a):
        self.valor = a

    def getTope (self):
        return self.tope
        
        
        
