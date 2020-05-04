from abc import ABC, abstractmethod
class Figura(ABC):
    def __init__(self,nombre):
        self.nombre = nombre
    
    @abstractmethod
    def area(self):
        pass
    def perimetro (self):
        pass
class Rectangulo (Figura):
    def __init__(self,nombre, base,altura):
        super().__init__(nombre)
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