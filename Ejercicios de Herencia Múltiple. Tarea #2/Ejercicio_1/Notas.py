from Materias import Materias
from Estudiante import Estudiante
from Materias import materia1
class Notas(Materias,Estudiante):
    notaLab = "8"
    notaParcial= "8"
    pass
    def VerNotas(): 
     return 'El estudiante: {},cursa la materia de: {} y sus notas son las siguientes: {} y {} en el primer computo'.format  (Estudiante.nombre,materia1.nombreMateria,Notas.notaLab,Notas.notaParcial )
notaFinal = Notas
print(notaFinal.VerNotas())