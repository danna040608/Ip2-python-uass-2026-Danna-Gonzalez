# #Ejercicio 1
# def estadisticas(numeros):
#     mayor = max(numeros)
#     menor = min(numeros)
#     promedio = sum(numeros) / len(numeros)
#     return mayor,menor,promedio

# #Programa principal
# numeros = [10,20,30,40,50]
# maximo,minimo,promedio = estadisticas(numeros)
# print(f"Mayor:{maximo}\nMenor:{minimo}\nPromedio:{promedio}")

# #EJERCICIO 2
# def buscar(lista,valor):
#     for nombre in lista:
# #         if nombre == valor:
# #             return True
# #     return False

# # #Programa principal
# # alumnos = ["Ana","Luis","Carlos"]
# # nombre = input("Ingrese el nombre a buscar: ")
# # resultado = buscar(alumnos,nombre)
# # print(resultado)

# #Ejercicio 3
# def eliminar_duplicados(lista):
#     return set(lista)

# #Programa principal
# numeros = [1,2,2,3,3,3,4]
# print(eliminar_duplicados(numeros))

# #Ejercicio 4
# def contar_frecuencia(lista):
#     frecuencia = {}
#     for elemento in set(lista):
#         frecuencia [elemento] = lista.count(elemento)
#     return frecuencia

# #Programa principal
# letras = ["a","b","a","c","a","b"]
# resultado = contar_frecuencia(letras)
# print(resultado) 


# #EJERCICIO 5
# def calcular_promedio(notas):
#    promedio = sum(notas)/len(notas)
#    return promedio
# def estado(promedio):
#    if promedio >=60:
#       return "Aprobado"
#    else:
#       return"Reprobado"

# #Programa principal
# notas = [70,80,90,60]
# promedio = calcular_promedio(notas)
# print(f"Pomedio:{promedio}")
# print(f"Estado: {estado(promedio)}")

# #EJERCICIO 6
# agenda = {
#    "Juan":"098111111",
#    "Ana":"0982222"
# }
# def agregar_contacto():
#    nombre = input("Ingrese el nombre: ")
#    numero = input("Ingrese el número de teléfono: ")
#    agenda[nombre]=numero
#    print("Contacto agregado correctamente")
# def buscar_contacto():
#    nombre =input("Ingrese el nombre a buscar:")
#    if nombre in agenda:
#       print(f"Teléfono de{nombre}:{agenda[nombre]}")
#    else:
#       print("Contacto no encontrado")
# def mostrar_contacto():
#    if len(agenda) == 0:
#       print("La agenda esta vacia")
#    else:
#       print("\n---Contactos---")
#       for nombre,teléfono in agenda.items():
#          print(f"{nombre}:{teléfono}")

# #Programa principal 
# while True:
#    print("\nAGENDA TELEFÓNICA")
#    print("1.Agregar contacto")
#    print("2.Buscar contacto")
#    print("3.Mostrar contacto")
#    print("4.Salir")

#    opcion = input("Seleccione una opció")
#    if opcion == "1":
#       agregar_contacto()
#    elif opcion == "2":
#       buscar_contacto()
#    elif opcion == "3":
#       mostrar_contacto()
#    elif opcion == "4":
#       print("Saliendo del programa")
#       break
#    else:
#       print("Opción inválida")    
            


# #EJERCICIO 7
# def producto_mas_caro(productos):
#     producto_caro = productos[0]
#     for producto in productos:
#         if producto[1] > producto_caro[1]:
#             producto_caro = producto    
#     return producto_caro

# #Programa principal 
# productos =[
#           ("Teclado",150000),
#           ("Mause",80000),
#           ("Monitor",1200000) 
# ]
# nombre,precio = producto_mas_caro(productos)
# # print(f"Producto:{nombre}\nPrecio:{precio}")    

# #EJERCICIO 8
# inventario ={
#     "Teclado",10,
#     "Mause",5,
#     "Monitor",2
# }  
# def agregar_stock(producto,cantidad):
#     if producto in inventario:
#         inventario[producto] += cantidad
#         print(f"Se agrega {cantidad} unidades de{producto}")
#     else:
#         inventario[producto] = cantidad
#         print(f"Producto {producto} agregado con{cantidad} unidades")
# def vender_producto(producto,cantidad):
#     if producto in inventario:
#         if inventario[producto] >= cantidad:
#             inventario[producto] -= cantidad
#             print(f"Venta realizada:{cantidad} de {producto}")
#         else:
#             print(f"No hay suficiente stock de {producto}.Disponible:{inventario[producto]}")    
#     else:
#         print(f"El producto{producto} no existe en el inventario") 

# def consultar_stock(producto):
#     if producto in inventario:
#         return inventario[producto]
#     else:
#         return 0

# def mostrar_inventario():
#     print("\nInventario actual: ")
#     for producto,cantidad in inventario.items():
#         print(f"{producto}:{cantidad} unidades")
#     print()
# mostrar_inventario()
# agregar_stock("Mouse",3)
# vender_producto("Teclado",2)
# print(f"Stock de monitor:{consultar_stock("Monitor")}")
# print(f"Stock de mause:")

#EJERCICIO 9
def mejor_alumno(alumnos):
    mejor = alumnos[0]
    for alumno in alumnos:
        if alumno[1] > mejor[1]:
           mejor = alumno
    return mejor
def peor_alumno(alumnos):
    peor = alumnos[0]
    for alumno in alumnos:
        if alumno[1] < peor[1]:
            peor = alumno
    return peor
def promedio_general(alumnos):
    suma = 0
    for alumno in alumnos:
        suma += alumno[1]
        promedio = suma /len(alumnos)
    return promedio            
#Promedio principal 
alumnos =[
    ("Juan",85),
    ("Ana",95),
    ("Pedro",70)
]
nombre_sobresaliente,nota_sobresaliente = mejor_alumno(alumnos)
nombre_rezagado,nota_rezagado = peor_alumno(alumnos)
promedio = peor_alumno(alumnos)
print(f"Mejor alumno:{nombre_sobresaliente} ({nota_sobresaliente})\nPeor alumno:{nombre_rezagado} ({nota_rezagado})\nPromedio general:{promedio}")