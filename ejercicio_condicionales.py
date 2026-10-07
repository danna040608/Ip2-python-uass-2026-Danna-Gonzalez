#Ejecicio 1:
edad = int(input("Ingrese su edad: "))
documento = input("¿Posee documento de identidad?: ")


if edad >= 18 and documento == "si":
    print("Bienvenido")
elif edad <= 18 and documento == "no":
    print("No es mayor y no posee documento")  
elif edad < 18 :
    print("No es mayor") 
elif documento == "no":
    print("No posee documento")

#Ejercicio 2:
monto = int(input("Ingrese el monto total de su compra:"))

if monto > 500000:
    descuento = monto * 0.20
elif monto > 200000:
    descuento = monto * 0.10
else:
    descuento = 0

    print("No posee descuento") 
total = monto - descuento
print("Monto original:",monto)
print("Descuento aplicado:",descuento)
print("Total a pagar:", total) 

#Ejercicio 3:
color = input("Ingrese el color:")

if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Reducir la velocidad")
elif color == "rojo":
    print("Detenerse")
else:
    print("El color no es válido")

#Ejercicio 4:
bateria = int(input("¿Cuál es el porcentaje de bateria de su móvil:"))

if bateria <= 10:
    print("Porcentaje crítico")
elif bateria <= 30:
    print("Porcentaje baja")
elif bateria <= 80:
    print("Porcentaje normal")
elif bateria <= 100:
    print("Porcentaje alto")  
else:
    print("Porcentaje inválido") 

#Ejercicio 5:
temperatura= int(input("Ingrese la temperatura actual:"))
if temperatura < 10:
    print("Mucho frio")
elif temperatura <= 24:
    print("Templado")
elif temperatura <= 34:
    print("Caluroso")
else:
    print("Muy caluroso")    




