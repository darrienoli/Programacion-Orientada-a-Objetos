from abc import ABC, abstractmethod  
class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    @abstractmethod
    def hacer_sonido(self):
        pass  
    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau 🐶"

    def moverse(self):
        return "El perro corre rápidamente."

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau 🐱"

    def moverse(self):
        return "El gato camina sigilosamente."

perro = Perro("Rex", 5)
gato = Gato("Michi", 3)

print(f"{perro.nombre}: {perro.hacer_sonido()} - {perro.moverse()}")
print(f"{gato.nombre}: {gato.hacer_sonido()} - {gato.moverse()}")
