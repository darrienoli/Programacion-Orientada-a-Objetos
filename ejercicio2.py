class Perro: #Clase Padre
    def __init__(self, nombre, raza, genero, edad, tamaño, peso, color):
        self.nombre = nombre
        self.raza = raza
        self.genero = genero
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.color = color

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Género: {self.genero}")
        print(f"Edad: {self.edad} años")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")


class Gato(Perro):  # Hereda de Perro (clase hijo o subclase)
    def __init__(self, nombre, raza, genero, edad, tamaño, peso, color, nivel_independencia, garras_retractiles):
        # Heredamos los atributos del Perro
        super().__init__(nombre, raza, genero, edad, tamaño, peso, color)
        # Agregamos los atributos únicos del gato
        self.nivel_independencia = nivel_independencia
        self.garras_retractiles = garras_retractiles

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Nivel de independencia: {self.nivel_independencia}")
        print(f"Garras retráctiles: {'Sí' if self.garras_retractiles else 'No'}")


# Ejemplo de uso:
perro1 = Perro("Rex", "Labrador", "Macho", 5, "Grande", 30, "Marrón")
gato1 = Gato("Michi", "Persa", "Hembra", 3, "Pequeño", 4, "Blanco", "Alto", True)

print("🐶 Información del perro:")
perro1.mostrar_info()

print("\n🐱 Información del gato:")
gato1.mostrar_info()
