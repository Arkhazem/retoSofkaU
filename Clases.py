# archivo que registra las clases del programa
#Clases a encontrar:
#  -Naves (madre)
#     -Lanzadera 
#     -No_Tripulada
#     -Tripulada




#inicia codificación de clases

#Clase padre Naves
#Atributos:
#   nombreNave: nombre que recibe la nave - String
#   categoriaNave: Categoria a la pertenece la nave - integer 
#   anoNave: Año de lanzamiento de la nave
#   combustibleNave: Combustible con el que funciona la nave - string
#   nacionalidadNave: El país que fabrico la nave - string
#   misionNave: El objetivo por el cual se lanzo la nave - string
#   empujeNave: La fuerza de empuje de los motores de la nave - integer
#   potenciaNave: Potencia de la nave

class Naves: 
    def __init__(self, nombreNave, categoriaNave, anoNave, nacionalidadNave, combustibleNave, misionNave, empujeNave, potenciaNave):
        self.nombreNave = nombreNave    
        self.categoriaNave = categoriaNave
        self.anoNave = anoNave
        self.nacionalidadNave = nacionalidadNave 
        self.combustibleNave = combustibleNave 
        self.misionNave = misionNave
        self.empujeNave = empujeNave
        self.potenciaNave = potenciaNave 
        


#Clase Lanzadera heredera de Naves


class Lanzadera(Naves): 
    pass  


#Clase No_Tripulada heredera de Naves 

class No_Tripulada(Naves): 
    pass



#Clase Tripuladas heredera de Naves

class Tripulada(Naves): 
       pass     
       
