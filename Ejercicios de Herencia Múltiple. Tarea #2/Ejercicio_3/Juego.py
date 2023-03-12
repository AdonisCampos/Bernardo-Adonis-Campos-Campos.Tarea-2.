from Jugador_1 import Jugador_1
from Jugador_2 import Jugador_2
from Jugador_1 import primerJugador
from Jugador_2 import segundoJugador
class Juego(Jugador_1,Jugador_2):
    pass
    elegirJugador=str(input("¿Que jugador dara el primer golpe?:"))
    print('--------------------------------------------------------------------------------------------------------------')
    if elegirJugador == "jugador1":
        restarVida1 = (primerJugador.poder-70)
        totalDeVida1 = (primerJugador.poder-30)
        print( 'El jugador: {} golpeo al jugador: {} se le quita de vida: {}% ahora solo tiene: {}%'.format(primerJugador.nombreDelJugador1,segundoJugador.nombreDelJugador2,restarVida1,totalDeVida1))
    else:
       if elegirJugador == "jugador2":
        restarVida2 = (segundoJugador.poder2-70)
        totalDeVida2= (segundoJugador.poder2-30)
        print( 'El jugador: {} golpeo al jugador: {} se le quita de vida: {}% ahora solo tiene: {}%'.format(segundoJugador.nombreDelJugador2,primerJugador.nombreDelJugador1,restarVida2,totalDeVida2))
       else:
        print("Ingrese un jugador valido")
