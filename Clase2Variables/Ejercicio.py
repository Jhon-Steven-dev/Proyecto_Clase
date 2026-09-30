import os

#os.system('cls')

# Un sistema recibe el nombre de una persona 
# y el programa académico al que pertenece. 
# Debe mostrar un mensaje de bienvenida que 
# incluya ambos datos. Considere que ninguno 
# de los dos campos puede quedar vacío

# NombrePersona = "Mario benedeti"
NombrePersona = input("Por favor ingrese su nombre completo: ").upper()
# Programa = "Desarrollo de software"
Programa = input("Ingrese su programa académico: ").upper()

Nivel = int(input("Ingrese el semestre en curso: "))
# print("Hola, bienvenido: " + NombrePersona + " al programa: " + Programa)
print(f"Hola, bienvenido: {NombrePersona} al programa: {Programa} nivel {Nivel}")





# Sume dos notas e imprima su promedio
CantidadNotas = 2
Nota1 = float(input("Ingrese la nota 1: "))
Nota2 = float(input("Ingrese la nota 2: "))
Resultado = (Nota1 + Nota2) / CantidadNotas
print(f"El resultado promedio es: {Resultado}")












