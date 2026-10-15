Ejercicio 1:
número = int(input("Ingrese un número entero positivo: ")) 
contador = 1
while contador <= número:
    print(contador)
    contador = contador + 1


#Ejercicio 2:
suma_total = 0
números = int(input("Ingrese un número: "))
while números != 0:
    suma_total = suma_total + números
    números = int(input("Ingrese otro número: "))
print("La suma total es:",suma_total)


#Ejercicio 3:
contraseña_correcta = "python123"
contraseña = input("Ingrese su contraseña: ")
while contraseña != contraseña_correcta:
    contraseña = input("Acceso denegado.Inténtalo nuevamente: ")
print("Acceso concedido")

#Ejercicio 4:
total_asistencia = 0
cantidad_clases = 0
asistencia = int(input("Ingrese la cantidad de estudiantes: "))
while asistencia != -1:
    total_asistencia = total_asistencia + asistencia
    cantidad_clases = cantidad_clases + 1
    asistencia = int(input("Ingrese la cantidad de estudiantes: "))
    promedio = total_asistencia / cantidad_clases
print("Total de asistencias: ",total_asistencia)
print("Cantidad de asistencia: ",cantidad_clases)
print("Promedio de asistencia: ",promedio)


#Ejercicio 5:
cantidad_productos = 0
total_pagar = 0
precio = int(input("Ingrese el precio de los productos: "))
while precio != 0:
    cantidad_productos = cantidad_productos + 1
    total_pagar = total_pagar + precio
    precio = int(input("Ingrese el precio de los productos:"))
print(f"Productos comprados: {cantidad_productos}")  
print(f"Total a pagar: {total_pagar}")  
