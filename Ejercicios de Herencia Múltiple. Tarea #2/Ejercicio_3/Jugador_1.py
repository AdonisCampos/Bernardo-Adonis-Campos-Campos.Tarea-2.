class Jugador_1:
    def __init__(self,nombreDelJugador1,poder):
        self.nombreDelJugador1 = nombreDelJugador1
        self.poder = poder
    
    def VerJugador1(self):
        return 'El nombre del jugador 1 es: {} con un poder de: {} '.format(self.nombreDelJugador1,self.poder)
    

print("********************************************************************************"
     "\n||                     ¡Bienvenido al juego de lucha!                         ||"
     "\n********************************************************************************")
primerJugador = Jugador_1 ('Goku',100)
print (primerJugador.VerJugador1())