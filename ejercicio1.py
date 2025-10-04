class Automovil:
    def __init__(self, marca, modelo, color, año, placa):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.placa = placa
    
    def inspección(self):
        return f"El auto de modelo: {self.modelo}, marca: {self.marca} del año {self.año} y con placa {self.placa} paso la inspección correctamente."

    def __str__(self):
        return f"""AUTO: 
ATRIBUTOS:
Marca = {self.marca}
Modelo = {self.modelo}
Color: = {self.color}
Año = {self.año}
Placa = {self.placa}"""
    
    def __repr__(self):
        return f"""Auto:
ATIBUTOS:
Marca = {self.marca} (string) (Not null)
Modelo = {self.modelo} (integer) (Not null)
Color: = {self.color} (string) (Not Null)
Año = {self.año} (Integer) (Not Null)
Placa = {self.placa} (string) (Not null)
"""
auto1 = Automovil("toyota", "yaris", "negro", 2006, "KM-001") 
auto2 = Automovil("chevrolet", "onix", "plata", 2010, "JA-002")

print(auto1.inspección())
print(repr(auto1))
print(str(auto1))