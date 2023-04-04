class Vehiculo():
    color = 'Rojo'
    ruedas = 4
    puertas = 3

class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 2600

c = Coche()
print('El vechiculo es de color:', c.color)
print('El vehiculo tiene', c.puertas,'puertas y',c.ruedas,'ruedas.')
print('La velocidad max del vehiculo es:',c.velocidad,'km/h con un cilindraje de:',c.cilindrada)
