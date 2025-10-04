from abc import ABC, abstractmethod
class PersonaUniversitaria(ABC):
    def __init__(self, nombre, id_universidad):
        self.nombre = nombre
        self.id_universidad = id_universidad

    @abstractmethod
    def mostrar_rol(self):
        pass

class Estudiante(PersonaUniversitaria):
    def __init__(self, nombre, id_universidad, carrera):
        super().__init__(nombre, id_universidad)
        self.carrera = carrera

    def mostrar_rol(self):
        return f"{self.nombre} es un estudiante de {self.carrera}."

class Profesor(PersonaUniversitaria):
    def __init__(self, nombre, id_universidad, especialidad):
        super().__init__(nombre, id_universidad)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"{self.nombre} es profesor especializado en {self.especialidad}."

estudiante = Estudiante("Ana López", "U1234", "Ingeniería de Sistemas")
profesor = Profesor("Dr. Ramírez", "U5678", "Base de Datos")

print(estudiante.mostrar_rol())
print(profesor.mostrar_rol())
