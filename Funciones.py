#importando clases 
#Naves, Lanzadera, No-Tripulada y Tripulada
from Clases import Lanzadera, Naves
from Clases import No_Tripulada
from Clases import Tripulada


# Declaración de variables

#NombreNaveaCrear - String
#CategoriaaCrear - String
#AnoaCrear - String
#NacionalidadaCrear - String
#CombustibleaCrear -String
#MisionaCrear - String
#EmpujeaCrear - String
#PotenciaaCrear - String
#CapacidadcargaaCrear - String
#NaveactivaaCrear - String
#SensoresaCrear  - String
#CapacidadtripulantesaCrear - String

NombreNaveaCrear = ""
CategoriaaCrear = ""
AnoaCrear = ""
NacionalidadaCrear = ""
CombustibleaCrear = ""
MisionaCrear = ""
EmpujeaCrear = ""
PotenciaaCrear = ""
CapacidadcargaaCrear = ""
NaveactivaaCrear = ""
SensoresaCrear = ""
CapacidadtripulantesaCrear = ""




# Creación de Hangares de Naves por defecto.

Hangar = [['Saturno V','Lanzadera','1973','USA','Propelente quimico','Transportar nave tripulada', '3500 kN','3500x5 kN'],
          ['Proton','Lanzadera','2001','Rusia','Quimico solido','Transporte de satelites','2700 kN','1745x6 kN'],
          ['H-IIA','Lanzadera','2001','Japon','Propelente quimico','Transporte de sondas','2300 kN','1500x6 kN'],
          ['Cassini-Huygens','No Tripulada','1997','USA, Europa, Italia','Propelente quimico','Transmitir informacion','45,39 Kg\n','50,32 Kg'],
          ['Mariner IV','No Tripulada','1964','USA','Propelente quimico','Transmitir informacion','22,44 Kg', '30,65 Kg'],
          ['Helios','No Tripulada','2009','USA, Alemania','Propelente quimico','Transmitir informacion','70,4 Kg','67,5 Kg'],
          ['LEM Apolo','Tripulada','1968','USA','Propelente quimico','Transportar astronautas a la luna','15,6 kN','20kN'],
          ['Salyut I','Tripulada','1971','Rusia','Quimico solido','Observacion cientifica','5,8 kN','4,3kN'],
          ['Vostok I','Tripulada','1960','Rusia','Quimico solido','Vuelos tripulados','13,4 kN','14kN']]

# Creación de Hangar de Naves Lanzadera por defecto.

HangarLanzadera = [['Saturno V','Lanzadera','1973','USA','Propelente quimico','Transportar nave tripulada', '3500 kN','3500x5 kN'],
                  ['Proton','Lanzadera','2001','Rusia','Quimico solido','Transporte de satelites','2700 kN','1745x6 kN'],
                  ['H-IIA','Lanzadera','2001','Japon','Propelente quimico','Transporte de sondas','2300 kN','1500x6 kN']] 

# Creación de Hangar de Naves NoTripuladas por defecto.

HangarNoTripulada = [['Cassini-Huygens','No Tripulada','1997','USA, Europa, Italia','Propelente quimico','Transmitir informacion','45,39 Kg\n','50,32 Kg'],
                     ['Mariner IV','No Tripulada','1964','USA','Propelente quimico','Transmitir informacion','22,44 Kg', '30,65 Kg'],
                     ['Helios','No Tripulada','2009','USA, Alemania','Propelente quimico','Transmitir informacion','70,4 Kg','67,5 Kg']]

# Creación de Hangar de Naves Tripuladas por defecto.

HangarTripulada = [['LEM Apolo','Tripulada','1968','USA','Propelente quimico','Transportar astronautas a la luna','15,6 kN','20kN'],
                   ['Salyut I','Tripulada','1971','Rusia','Quimico solido','Observacion cientifica','5,8 kN','4,3kN'],
                   ['Vostok I','Tripulada','1960','Rusia','Quimico solido','Vuelos tripulados','13,4 kN','14kN']]



# funcion Menu - Un menú para crear una nave en las 3 categorias de naves existente.
# @opcionR - int
# Return  int

def Menu(opcionR):
    opcion = opcionR
    if opcion >= 1 and opcion <= 4:
        if opcion == 1:
            print("Escoge la nave que desees crear:\n\n")
            print("\t 1) Crear Nave Lanzadera\n")
            print("\t 2) Crear Nave No Tripulada\n")
            print("\t 3) Crear Nave Tripulada\n")
            categoria = int(input("Digita aquí la acción deseada:\t"))
            Crear_Nave(categoria)
            return 0
        if opcion == 2:
            print("Escoge la opcion que desees crear:\n\n")
            print("\t 1) Buscar por nombre\n")
            print("\t 2) Buscar por categoria\n")
            print("\t 3) Buscar por año de lanzamiento\n")
            print("\t 4) Buscar por pais de creación\n")
            buscarNave = int(input("Digita aquí la acción deseada\t"))  
            Buscar_Nave(buscarNave)
            return 0
        if opcion == 3:
            print("Escoge el hangar que deseas ver:\n\n")
            print("\t 1) Hangar Completo\n")
            print("\t 2) Hangar Hangar de Naves Lanzadera\n")
            print("\t 3) Hangar de Naves No Tripuladas\n")
            print("\t 4) Hangar de Naves Tripuladas\n")
            hangar = int(input("Digita aquí la acción deseada\t"))
            accesohangar(hangar)
            return 0
        if opcion == '4':
            return 1
    else:
            print("\nEscoge una opción válida.\n\n")
            return 0    
        



# Crear_Nave - Funcion que instancia los objetos nave creados por el usuario
# @categoria - Int
# Return Void

def Crear_Nave(cateogoria):
    opcioncrear = cateogoria
    
    if opcioncrear >= 1 and opcioncrear <=3:
        if opcioncrear == 1:
            nombreLanzadera = input('Nombre de la lanzadera:\t')
            categrialanzadera = 'Lanzadera'
            anolanzadera = input('Año de fabricación:\t')
            paislanzadera = input('País que desarrolla la Nave:\t')
            combustiblelanzadera = input('Combustible que utiliza:\t')
            misionlanzadera = input('Misión de la lanzadera:\t')
            empoujelanzadera = input('Digite el empuje de la nave:\t')
            potencialanzadera = input('Digite la potencia de la nave:\t')
            #capacidadlanzadera = input('Digite la capacidad de carga de la nave:\t')
            nuevalanzadera = Lanzadera(nombreLanzadera,categrialanzadera,anolanzadera,paislanzadera,combustiblelanzadera,misionlanzadera,empoujelanzadera,potencialanzadera)
            lanzadera = nombreLanzadera,categrialanzadera,anolanzadera,paislanzadera,combustiblelanzadera,misionlanzadera,empoujelanzadera,potencialanzadera
            Hangar.append([lanzadera])
            HangarLanzadera.append([lanzadera])
            print('\nSe ha añadido una nueva lanzadera al hangar\n')

        if opcioncrear == 2:
            nombrenotripulada = input('Nombre de la nave no tripulada:\t')
            categrianotripulada = 'No Tripulada'
            anonotripulada = input('Año de lanzamiento:\t')
            paisnotripulada = input('País que desarrolla la Nave:\t')
            combustiblenotripulada = input('Combustible que utiliza:\t')
            misionnotripulada = input('Misión de la nave no tripulada:\t')
            empoujenotripulada = input('Digite el empuje de la nave:\t')
            potencianotripulada = input('Digite la potencia de la nave:\t')
            nuevaNoTripulada = No_Tripulada(nombrenotripulada,categrianotripulada, anonotripulada,paisnotripulada,combustiblenotripulada,misionnotripulada,empoujenotripulada,potencianotripulada)
            no_tripulada = nombrenotripulada,categrianotripulada, anonotripulada,paisnotripulada,combustiblenotripulada,misionnotripulada,empoujenotripulada,potencianotripulada
            Hangar.append([no_tripulada])
            HangarNoTripulada.append([no_tripulada])
            print('Se ha añadido una nueva nave no tripulada al hangar\n')

        if opcioncrear == 3:
            nombretripulada = input('Nombre de la nave tripulada:\t')
            categriatripulada = 'Tripulada'
            anotripulada = input('Año de lanzamiento:\t')
            paistripulada = input('País que desarrolla la Nave:\t')
            combustibletripulada = input('Combustible que utiliza:\t')
            misiontripulada = input('Misión de la nave tripulada:\t')
            empoujetripulada = input('Digite el empuje de la nave:\t')
            potenciatripulada = input('Digite la potencia de la nave:\t')
            nuevaTripulada = Tripulada(nombretripulada,categriatripulada,anotripulada,paistripulada,combustibletripulada,misiontripulada,empoujetripulada,potenciatripulada)
            tripulada = nombretripulada,categriatripulada,anotripulada,paistripulada,combustibletripulada,misiontripulada,empoujetripulada,potenciatripulada
            Hangar.append([tripulada])
            HangarTripulada.append([tripulada])
            print('Se ha añadido una nueva nave tripulada al hangar\n')


# accesohangar - Funcion que imprime los naves del hangar por tipo o todas
# @hangar - Int
# Return Void

def accesohangar(hangar):
    opcionhangar = hangar
    
    if opcionhangar >= 1 and opcionhangar <=4:
        if opcionhangar == 1:
            print(Hangar)

        if opcionhangar == 2:
            print(HangarLanzadera)

        if opcionhangar == 3:
            print(HangarNoTripulada)
        
        if opcionhangar == 4:
            print(HangarTripulada)


# Buscar_Nave - Funcion que da al usuario un menú para buscar las naves por nombre, categoria, año y país
# @buscarNave - Int
# Return Void           

def Buscar_Nave(buscarNave):
    opcionbuscar = buscarNave
    
    if opcionbuscar >= 1 and opcionbuscar <=4:

        if opcionbuscar == 1:
            nombrebusqueda = input('Escriba el nombre que desea buscar\t')
            busqueda = buscarnombre(Hangar,nombrebusqueda)
            if busqueda == None:
                print('No existen elementos para esa busqueda')
            else:
                for buscar in busqueda:
                    mostrarbusquedanombre(buscar)

        if opcionbuscar == 2:
            categoriabusqueda = input('Escriba categoria que desea buscar\t')
            busqueda = buscarcategorias(Hangar,categoriabusqueda)
            if busqueda == None:
                print('No existen elementos para esa busqueda')
            else:
                for buscar in busqueda:
                    mostrarbusquedacategoria(buscar)

        if opcionbuscar == 3:
            anobusqueda = input('Escriba el ano de lanzamiento que desea buscar\t')
            busqueda = buscarano(Hangar,anobusqueda)
            if busqueda == None:
                print('No existen elementos para esa busqueda')
            else:
                for buscar in busqueda:
                    mostrarbusquedaano(buscar)
        
        if opcionbuscar == 4:
            paisbusqueda = input('Escriba el pais de fabricacion que desea buscar\t')
            busqueda = buscarpais(Hangar,paisbusqueda)
            if busqueda == None:
                print('No existen elementos para esa busqueda')
            else:
                for buscar in busqueda:
                    mostrarbusquedapais(buscar)


# buscarnombre - Funcion que da al usuario un menú para buscar las naves por nombre, categoria, año y país
# @Hangar - Int
# @elemento - string
# Return none or encontrados
 
def buscarnombre(Hangar, elemento):
    encontrados = []
    for busqueda in Hangar:
        if busqueda[0] == elemento:
            encontrados.append(busqueda)
    if len(encontrados) == 0:
        return None
        
    else:
        return encontrados

# mostrarbusquedanombre - Funcion que imprime la nave  que se pudo encontrar en los registros del hangar
# @busqueda - string
# Return void  
def mostrarbusquedanombre(busqueda):
    if busqueda == None:
        print('No existen elementos para esta busqueda')
    else:
        print('Nombre Nave:\t', busqueda[0])
        print('Categoria de la nave:\t', busqueda[1])
        print('Año de lanzamiento:\t', busqueda[2])
        print('Pais donde fue fabricado:\t', busqueda[3])
        print('Combustible de la nave: \t',busqueda[4])
        print('Mision de la nave:\t',busqueda[5] )
        print('Empuje de la nave:\t',busqueda[6] )
        print('Potencia de la nave:\t',busqueda[7],'\n') 



# buscarcategoria - Funcion que busca naves creadas por categoría
# @Hangar - Int
# @elemento - string
# Return none or encontrados

def buscarcategorias(Hangar, elemento):
    encontrados = []
    for busqueda in Hangar:
        if busqueda[1] == elemento:
            encontrados.append(busqueda)
    if len(encontrados) == 0:
        return None
        
    else:
        return encontrados


# mostrarbusquedacategoria - Funcion que imprime la nave  que se pudo encontrar en los registros del hangar por categoria
# @busqueda - string
# Return void  
def mostrarbusquedacategoria(busqueda):
    if busqueda == None:
        print('No existen elementos para esta busqueda')
    else:
        print('Nombre Nave:\t', busqueda[0])
        print('Categoria de la nave:\t', busqueda[1])
        print('Año de lanzamiento:\t', busqueda[2])
        print('Pais donde fue fabricado:\t', busqueda[3])
        print('Combustible de la nave: \t',busqueda[4])
        print('Mision de la nave:\t',busqueda[5] )
        print('Empuje de la nave:\t',busqueda[6] )
        print('Potencia de la nave:\t',busqueda[7],'\n') 


# buscarano - Funcion que busca naves creadas por año
# @Hangar - Int
# @elemento - string
# Return none or encontrados     
def buscarano(Hangar, elemento):
    encontrados = []
    for busqueda in Hangar:
        if busqueda[2] == elemento:
            encontrados.append(busqueda)
    if len(encontrados) == 0:
        return None
        
    else:
        return encontrados


# mostrarbusquedaano - Funcion que imprime la nave  que se pudo encontrar en los registros del hangar por año
# @busqueda - string
# Return void        
def mostrarbusquedaano(busqueda):
    if busqueda == None:
        print('No existen elementos para esta busqueda')
    else:
        print('Nombre Nave:\t', busqueda[0])
        print('Categoria de la nave:\t', busqueda[1])
        print('Año de lanzamiento:\t', busqueda[2])
        print('Pais donde fue fabricado:\t', busqueda[3])
        print('Combustible de la nave: \t',busqueda[4])
        print('Mision de la nave:\t',busqueda[5] )
        print('Empuje de la nave:\t',busqueda[6] )
        print('Potencia de la nave:\t',busqueda[7],'\n') 



# buscarano - Funcion que busca naves creadas por país
# @Hangar - Int
# @elemento - string
# Return none or encontrados  
def buscarpais(Hangar, elemento):
    encontrados = []
    for busqueda in Hangar:
        if busqueda[3] == elemento:
            encontrados.append(busqueda)
    if len(encontrados) == 0:
        return None
        
    else:
        return encontrados


# ostrarbusquedapais - Funcion que imprime la nave  que se pudo encontrar en los registros del hangar por país
# @busqueda - string
# Return void          
def mostrarbusquedapais(busqueda):
    if busqueda == None:
        print('No existen elementos para esta busqueda')
    else:
        print('Nombre Nave:\t', busqueda[0])
        print('Categoria de la nave:\t', busqueda[1])
        print('Año de lanzamiento:\t', busqueda[2])
        print('Pais donde fue fabricado:\t', busqueda[3])
        print('Combustible de la nave: \t',busqueda[4])
        print('Mision de la nave:\t',busqueda[5] )
        print('Empuje de la nave:\t',busqueda[6] )
        print('Potencia de la nave:\t',busqueda[7],'\n') 




    