from Categoria import Categoria
from Peliculas import Peliculas
from Categoria import categoria
class Cliente(Categoria,Peliculas):
    pass 
    def __init__(self,nombreUsuario):
     self.nombreUsuario = nombreUsuario
    
    def VerUsuario(self):
     return '***El usuario de esta cuenta en nuestra plataforma es: {}****'.format(self.nombreUsuario)

categoriaElegir=str(input("Ingrese la categoria que desea ver:"))
print('--------------------------------------------------------------------------------------------------------------')
if categoriaElegir == "Accion":
    print('Esta viendo la pelicula: {} esta pelicula pertenece a la categoria {} '.format(Peliculas.nombrePeliculaAccion,categoria.nombreCategoria1))
else:
    if categoriaElegir == "Comedia":
        print('Esta viendo la pelicula: {} esta pelicula pertenece a la categoria {} '.format(Peliculas.nombrePeliculComedia,categoria.nombreCategoria2))
    else:
        if categoriaElegir == "Terror":
            print('Esta viendo la pelicula: {} esta pelicula pertenece a la categoria {} '.format(Peliculas.nombrePeliculaTerror,categoria.nombreCategoria3))
        else:
            print("Por favor ingrese una categoria correcta.")

print('--------------------------------------------------------------------------------------------------------------')      
usuario1 = Cliente("BERNARDO ADONIS CAMPOS")
print(usuario1.VerUsuario())             
          
   