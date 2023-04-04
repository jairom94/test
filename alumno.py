class Alumno():
    nombre=''
    nota=0
    def __init__(self,nombre, nota):
        self.nombre=nombre
        self.nota=nota
    def isApproved(self):
        if self.nota >= 7:
            return 'Aprovado'
        return 'Desaprovado'

alumno1 = Alumno('Samuel',8.3)
print('El Alumno:',alumno1.nombre,'está',alumno1.isApproved())
