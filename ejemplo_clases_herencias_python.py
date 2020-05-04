from abc import ABC, abstractmethod
class Figura(ABC):
    def _init_(self,nombre):
        self.nombre = nombre
    
    @abstractmethod
    def area(self):
        pass
    def perimetro (self):
        pass
class Rectangulo (Figura):
    def _init_(self,nombre, base,altura):
        super()._init_(nombre)
        self.base = base
        self.altura = altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return 2*(self.base+self.altura)

rect = Rectangulo("Rectangulo",3.0,2.0)
cuad = Rectangulo("Cuadrado Unitario", 1.0,1.0)
print("El rectangulo" +rect.nombre+ "tiene area"+str(rect.area())+" y perimetro "+str(rect.perimetro()))
print("El rectangulo" +cuad.nombre+ "tiene area"+str(cuad.area())+" y perimetro "+str(cuad.perimetro()))