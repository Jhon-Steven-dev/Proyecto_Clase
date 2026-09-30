# NotasTotal = 0 # Variable global para almacenar la suma de las notas

# for i in range(1, 3+1): #Iniciamos el ciclo for para iterar 3 veces, ya que necesitamos 3 notas
#     Nota = float(input(f"Ingrese la nota {i}: ")) # Solicitamos al usuario que ingrese la nota correspondiente a la iteración actual
#     NotasTotal += Nota # Acumulamos la nota ingresada a la variable NotasTotal para calcular el promedio posteriormente

# promedio = NotasTotal / 3 # Calculamos el promedio dividiendo la suma total de las notas entre 3, que es la cantidad de notas ingresadas
# print(f"El promedio de las notas ingresadas es: {promedio}") # Mostramos el promedio calculado al usuario


# ################################################################################################

# for i in range(0, 20+1):
#     print(f"El valor de i es: {i}") # Iniciamos un ciclo for que se repetirá 21 veces, para mostrar los números del 0 al 20

# for i in range(20, -1, -1): # Iniciamos un ciclo for que se repetirá 21 veces, para mostrar los números del 20 al 0 en orden descendente
#     print(f"El valor de i es: {i}")


tablaC=int(input("Ingrese la tabla de multiplicar que desea ver: ")) 
for i in range(1, 11):
    print(f"{tablaC} x {i} = {tablaC*i}") 