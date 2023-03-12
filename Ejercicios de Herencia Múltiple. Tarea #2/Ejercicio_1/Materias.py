class Materias:
    def __init__(self,nombreMateria, ciclo):
        self.nombreMateria=  nombreMateria
        self.ciclo= ciclo
    
    def verInformacion(self):
        return 'Nombre de la materia es: {} y el ciclo es: {}'.format(self.nombreMateria,self.ciclo)
materia1 = Materias('Matematica II', 2)
print (materia1.verInformacion())