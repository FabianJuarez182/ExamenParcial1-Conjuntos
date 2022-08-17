dato = ""
U = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
A = []
AF = []
B = []
BF = []
UF = []
IF = []
CF = []
DF = []

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

def mostrar_datos_Finales(A,B):
    print(U)
    print("Los elementos que posee el conjunto final de cada uno son: \n")
    for element in U:
        if element in A:
            AF.append(1)
        else:
            AF.append(0)
    print("Conjunto A:")
    print(AF)
    for element in U:
        if element in B:
            BF.append(1)
        else:
            BF.append(0)
    print("Conjunto B:")
    print(BF)

def mostrar_menu(opciones):
    print('\nSeleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


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


def accion1():
    print('\n\t\tHas elegido la Union')
    for i in range(36):
        if((AF[i]== 1 and BF[i]==1)or (AF[i]== 1 and BF[i]== 0) or (AF[i]== 0 and BF[i]==1)):
            UF.append(1)
        else:
            UF.append(0)
    print("\tConjunto Union de A y B:")
    print (UF)


def accion2():
    print('\n\t\tHas elegido Intersección')
    for i in range(36):
        if(AF[i]== 1 and BF[i]==1):
            IF.append(1)
        else:
            IF.append(0)
    print("\tConjunto Union de A y B:")
    print (IF)

def accion3():
    print('\n\t\tHas elegido Diferencia')



def accion4():
    print('\n\t\tHas elegido Complemento')

    

def accion5():
    D = input('Ingrese el dato que desea buscar en el conjunto:')
    conjunto = input("En que conjunto desea buscar el dato?")
    if(conjunto == "A" or conjunto == "a"):
        for element in A:
            if(element in D):
                bandera = True
                break
        if (bandera == True):
            print(f"El elemento {D} si se ha encontrado {conjunto}!")
        else:
            print(f"El elemento {D} no se ha encontrado en el conjunto {conjunto}!")
    elif(conjunto == "B" or conjunto == "b"):
        for element in B:
            if(element in D):
                bandera = True
                break
        if (bandera == True):
            print(f"El elemento {D} si se ha encontrado {conjunto}!")
        else:
            print(f"El elemento {D} no se ha encontrado en el conjunto {conjunto}!")


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()