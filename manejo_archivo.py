#EJERCICO 1:
with open("productos.txt","w",encoding="utf-8") as archivo:
    for a in range(5):
        nombre = input('Ingrese el nombre del producto ' + str(a + 1) + ':')
        precio = input('Ingrese el precio del producto ' + nombre + ':' )
        archivo.write(nombre + '-' + precio + '\n')
print('¡ARCHIVO CREADO!') 

#EJERCICIO 2:
with open("productos.txt","r",encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

#EJERCICIO 3:
nombre = input('Ingrese el nombre de la persona: ')
edad = input('Ingrese la edad de la persona: ')
with open("registro.txt","a",encoding="utf-8") as archivo:
    archivo.write(f'Nombre: {nombre},Edad: {edad}\n')
print('Datos agregados correctamente') 

#EJERCICIO 4:
suma = 0
contador = 0
with open("numeros.txt","r",encoding="utf-8") as archivo:
    for linea in archivo:
        linea_nueva = linea.strip()
        if linea_nueva:
            suma += int(linea_nueva)
            contador += 1
if contador > 0:
    promedio = suma /contador
else:
    promedio = 0                   
with open("resultado.txt","w",encoding="utf-8") as archivo:
    archivo.write(f'Promedio: {promedio}')
print(f'El promedio calculado: {promedio}') 

#EJERCICIO 5:
with open("origen.txt","r",encoding="utf-8") as origen:
    with open("destino.txt","w",encoding="utf-8") as destino:
        for linea in origen:
            destino.write(linea)
print('Contenido copiado correctamente')            
