class Categoria:
   def __init__(self, nombreCategoria1,nomnbreCategoria2,nombreCategoria3):
        self.nombreCategoria1 = nombreCategoria1
        self.nombreCategoria2= nomnbreCategoria2
        self.nombreCategoria3 = nombreCategoria3
   def verCategoria(self):
        return 'Las categorias streaming disponibles para ti son: \n{} \n{} \n{}'.format(self.nombreCategoria1,self.nombreCategoria2,self.nombreCategoria3)

print("==============================================================================="
     "\n||                     ¡Bienvenido Streaming View!                           ||"
     "\n===============================================================================")
categoria = Categoria('***Accion****', '***Comedia***', '***Terror****')
print (categoria.verCategoria())

