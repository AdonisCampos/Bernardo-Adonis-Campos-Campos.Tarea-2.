class Jugador_2:
    def __init__(self,nombreDelJugador2,poder2):
        self.nombreDelJugador2 = nombreDelJugador2
        self.poder2 = poder2
    
    def VerJugador1(self):
        return 'El nombre del jugador 2 es: {} con un poder de: {} '.format(self.nombreDelJugador2,self.poder2)
segundoJugador = Jugador_2 ('Vegeta',100)
print (segundoJugador.VerJugador1())