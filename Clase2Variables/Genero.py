import os
import time 
os.system('cls')

Opcion = int(input("Ingrese el numero segun corresponda: \n1.Hombre: \n2.Mujer:\n3.Semaforo: \n4.Salir \n: "))
time.sleep(2)
os.system('cls')
if Opcion == 1:
    NombreHombre = input("Ingrese el nombre: ")
    Edad = input("Ingrese la edad: ")
    Profesion = input("Ingrese la profesión: ")
    print(f"El usuario ingresado es: {NombreHombre} con edad {Edad} y su profesión es {Profesion}")
elif Opcion == 2:
    NombreMujer = input("Ingrese el nombre: ")    
    Profesion = input("Ingrese la profesión: ")
    print(f"El usuario ingresado es: {NombreMujer} y su profesión es {Profesion}")
elif Opcion == 3:
    print("*"*41)
    print(f"{"*"*2} Escogiste la opción del Semaforo :) {"*"*2}")
    print("*"*41)
    time.sleep(2)
    os.system('cls')
    print("Marca el número segun el color del semaforo: ")
    Estado = int(input("1.Verde\n2.Amarillo\n3.Rojo\n"))
    time.sleep(2)
    os.system('cls')
    if Estado == 1:
        print("Avanzar :) ")
    elif Estado == 2:
        print("Precaución :/ ")
    elif Estado == 3:
        print("Detenerse :| ")
    else:
        print("Seleccione una opción valida")
    time.sleep(2)
    os.system('cls')
elif Opcion == 4:
    exit()
else:
    print("Seleccione una opción valida")

print('''
        ============================================
        ||                                        ||
        ||          FIN DEL PROGRAMA              ||
        ||                                        ||
        ============================================
''')