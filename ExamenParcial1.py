# Universidad del Valle de Guatemala
# Departamento de Ingeniería
# Matematica Discreta seccion 10
# Fabián Estuardo Juárez Tello 21440
# Catedrático: Mario Castillo

#Crear las variables y listas a utilizar
dato = ""
U = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
CU = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
A = []
AF = []
B = []
BF = []

#Metodo que permite el ingreso de los datos para el conjunto A
def mostrar_ingreso_A(dato):
    while dato != "no" or dato !="No":
        dato = input('Desea ingresar un dato para el conjunto A?\n')
        if (dato =="si" or dato == "Si"):
            D = input('Ingrese el dato a tener en el conjunto A: ')
            A.append(D.lower())
        else:
            print('Ya ha ingresado todos los Datos del conjunto A \n\n')
            break
    print("Los elementos que posee el elemento A son: ")
    print(A)

#Metodo que permite el ingreso de los datos para el conjunto B
def mostrar_ingreso_B(dato2):
    while dato2 != "no":
        dato2 = input('\n\nDesea ingresar un dato para el conjunto B?\n')
        if (dato2 =="si" or dato2 == "Si"):
            D = input('Ingrese el dato a tener en el conjunto B: ')
            B.append(D.lower())
        else:
            print('Ya ha ingresado todos los Datos del conjunto B ')
            break
    print("Los elementos que posee el elemento B son:" )
    print(B)

#Metodo que permite mostrar los elementos para cada uno de los conjuntos en la conversion a binario, siendo
# 1 que si lo posee y 0 que no lo posee el conjunto a comparacion del conjunto universo
def mostrar_datos_Finales(A,B):
    print(U)
    print("Los elementos que posee el conjunto final de cada uno son: \n")
    #Metodo que recorre el conjunto A para la obtencion de los datos para el conjunto
    for element in U:
        if element in A:
            AF.append(1)
        else:
            AF.append(0)
    print("Conjunto A:")
    print(AF)
    #Metodo que recorre el conjunto B para la obtencion de los datos para el conjunto
    for element in U:
        if element in B:
            BF.append(1)
        else:
            BF.append(0)
    print("Conjunto B:")
    print(BF)

#Metodo que posee la creacion del menu y su muestra 
def mostrar_menu(opciones):
    print('\nSeleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

#Metodo que leera la opcion ingresada por el usuario y devolvera error si no ha escogido una valida
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

#Metodo que ejecutara la opcion escogida por el usuario
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

#Metodo que genera el menu en base a las opciones y las salidas que hay a mostrar
def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

#Metodo que se utilizara para llevar a cabo todos los procesos (sera el metodo main)
def menu_principal():
    mostrar_ingreso_A(dato)
    mostrar_ingreso_B(dato)
    mostrar_datos_Finales(A,B)
    opciones = {
        '1': ('Union', accion1),
        '2': ('Intersección', accion2),
        '3': ('Diferencia', accion3),
        '4': ('Complemento', accion4),
        '5': ('busqueda de un elemento especifico', accion5),
        '6': ('Salir',salir)
    }
    generar_menu(opciones, '5')

#Metodo que realizara la union de los conjuntos A y B
def accion1():
    UF = []
    print('\n\t\tHas elegido la Union')
    #recorrera el conjunto A y B y verificara que la menos uno de los 2 tenga el dato para colocar 1
    for i in range(36):
        if((AF[i]== 1 and BF[i]==1)or (AF[i]== 1 and BF[i]== 0) or (AF[i]== 0 and BF[i]==1)):
            UF.append(1)
        else:
            UF.append(0)
    print("\tConjunto Union de A y B:")
    print (UF)

#Metodo que realizara la interseccion de los conjuntos A y B
def accion2():
    IF = []
    print('\n\t\tHas elegido Intersección')
    #recorrera el conjunto A y B y verificara que ambos tengan el dato para colocar 1
    for i in range(36):
        if(AF[i]== 1 and BF[i]==1):
            IF.append(1)
        else:
            IF.append(0)
    print("\tConjunto Intersección de A y B:")
    print (IF)

#Metodo que realizara la Diferencia de los conjuntos A y B dependiendo cual escoja el usuario
def accion3():
    DF = []
    print('\n\t\tHas elegido Diferencia')
    conjunto = input("En que conjunto desea aplicar la diferencia?")
    if(conjunto == "A" or conjunto == "a"):
    #recorrera el conjunto A y B y verificara que solo A tenga el dato y B no
        for i in range(36):
            if(AF[i]== 1 and BF[i]==0):
                DF.append(1)
            else:
                DF.append(0)
        print("\tDiferencia de A hacia B:")
        print (DF)
    elif(conjunto == "B" or conjunto == "b"):
    #recorrera el conjunto A y B y verificara que solo B tenga el dato y A no
        for i in range(36):
            if(AF[i]== 0 and BF[i]==1):
                DF.append(1)
            else:
                DF.append(0)
        print("\tDiferencia de B hacia A:")
        print (DF)

#Metodo que realizara el complemento de los conjuntos A y B, segun la eleccion del usuario
def accion4():
    CF = []
    print('\n\t\tHas elegido Complemento')
    conjunto = input("En que conjunto desea aplicar el complemento?")
    if(conjunto == "A" or conjunto == "a"):
    #recorrera el conjunto A y verificara que datos le hacen falta a A que tiene el conjunto U
        for i in range(36):
            if(AF[i]==0 and CU[i]==1):
                CF.append(1)
            else:
                CF.append(0)
        print("\tEl complemento en A es:")
        print (CF)
    elif(conjunto == "B" or conjunto == "b"):
    #recorrera el conjunto B y verificara que datos le hacen falta a B que tiene el conjunto U
        for i in range(36):
            if(BF[i]== 0 and CU[i]==1):
                CF.append(1)
            else:
                CF.append(0)
        print("\tEl complemento en B es:")
        print (CF)
    
#Metodo que realizara la busqueda de un elemento en especifico de cualquiera de los 2 conjuntos, sera eleccion del usuario
def accion5():
    D = input('Ingrese el dato que desea buscar en el conjunto:')
    conjunto = input("En que conjunto desea buscar el dato?")
    if(conjunto == "A" or conjunto == "a"):
    #recorrera el conjunto A y verificara que el dato que se busca se encuentra
        for element in A:
            if(element in D):
                bandera = True
                break
        if (bandera == True):
            print(f"El elemento {D} si se ha encontrado en el conjunto {conjunto}!")# si se encuentra imprimira esto
        else:
            print(f"El elemento {D} no se ha encontrado en el conjunto {conjunto}!")# si no se encuentra imprimira esto
    elif(conjunto == "B" or conjunto == "b"):
    #recorrera el conjunto B y verificara que el dato que se busca se encuentra
        for element in B:
            if(element in D):
                bandera = True
                break
        if (bandera == True):
            print(f"El elemento {D} si se ha encontrado en el conjunto {conjunto}!")# si se encuentra imprimira esto
        else:
            print(f"El elemento {D} no se ha encontrado en el conjunto {conjunto}!")# si no se encuentra imprimira esto

#Metodo que cerrara el programa si el usuario lo elije
def salir():
    print('Saliendo')
    exit()

if __name__ == '__main__':
    menu_principal()