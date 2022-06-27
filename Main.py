#  Programa principal para la resolución reto técnico SofkU

# importamos archivo Funciones
import Funciones as Funciones


#Ciclo del menú principal
while True:
    print("\n\nBienvenido al Hangar Cabo Cañaveral.\n\n\n")
    print("Escoge una de las siguientes opciones:\n")
    print("\t 1) Crear nave\n")
    print("\t 2) Buscar nave\n")
    print("\t 3) Ver Hangar\n")
    print("\t 4) Salir del programa \n\n")    
        
    opcion = int(input ("Digita aqui la accion deseada:\t")) # @opcion - Variable opcion que captura la acción deseada por el usuario
    
    bandera = Funciones.Menu(opcion) # @bandera - Variable bandera que captura el número de regreso de la opciones deseadas
      
    if bandera != 0: #Evalua si bandera es diferentes de cero para salir del ciclo o continuar su ejecución
        break

# FIN