def agregarPasajeeos(pasajeros):
     '''Agregar pasajeros a la lista y retornarla'''
     nombre = input('Nombre - x|X para terminar')
     while nombre.upper() != 'x':
         dni = input('DNI:')
         destino = input('Ciudad de destino:')
         pasajeros.append((nombre,dni,destino))
         nombre = input('Nombre = x|X para terminar:') 
     return pasajeros
def agregarCiudades(ciudades):
     '''Agregar ciudades a la lista y retornarla'''
     ciudades = input('Ciudad = x|X para terminar:')
     while ciudad.upper() != 'x':
          pais = input('Pais:')
          ciudades.append((ciudad,pais))
          ciudad = input('ciudad - x|X para terminar:')
     return ciudades
def buscarCiudad(pasajeros,dni):
     '''Dado un DNI de pasajeros ,lo busca en la lista  y retorna la ciudad a la que viajó'''
     for viaje in pasajeros:
         if pasajeros[2] == dni:
          return pasajeros[2]
     return "DNI no encontrado..."   
def mostrarCantidad (pasajeros,ciudad):
     '''Dada una ciudad,cuenta sua pasajeros'''
     contador = 0
     for viaje in pasajeros:
          if viaje[2].lower() == ciudad.lower():
               contador += 1
     return contador               
def buscarPais (pasajeros,ciudad,dni):
     '''Dado un DNI,ve a que pais viaja'''
     ciudad_destino = ""
     for viaje in pasajeros:
          if viaje[1] == dni:
               ciudad_destino = viaje[2]
               break
     if not ciudad_destino:
          return 'DNI no encotrado'
     for c in ciudad_destino:
          if c[0].lower() == ciudad_destino.lower():
               return c[1]
     return 'Ciudad destino no registrado en la lista de ciudades.'
def cantidadPasajeros(pasajeros,ciudad,pais):
     '''Dado un pais,cuenta sus pasajeros'''
     ciudades_del_pais =[]
     for c in ciudad:
       if c[1].lower() == pais.lower():
            ciudades_del_pais.append(c[0].lower())
     contador = 0
     for viaje in pasajeros:
          if viaje[2].lower() in ciudades_del_pais:
               contador += 1
     return contador                    
          
               
pasajeros = []
ciudad = []

while True:
    print('Bienvenidos a Aerolíneas UASS,favor selecciopne una opcion:')
    print('1. Agregar pasajeros')
    print('2. Agregar ciudades')
    print('3. Buscar ciudad destino mediante DNI')
    print('4. Mostrar cantidad de pasajeros por ciudad destino')
    print('5. Buscar pais destino mediante DNI')
    print('6. Mostrar cantidad de pasajeros por pais destino')
    print('7. Salir del programa')
    # El usuario la opcion del menú
    opcion = int(input('Seleccione la opcion a ejecutar: '))
    if opcion == 1:
        print('Agregar pasajeros')
        pasajeros = agregarPasajeeos(pasajeros)
        print('Listado actual de pasajeros..')
        print(pasajeros)
    elif opcion == 2:
          print('Agregar ciudades') 
          ciudades = agregarCiudades(ciudad)
          print(f'Lista de ciudades registradas{[ciudades]}')
    elif opcion == 3:
         print('Buscar ciudad destino')
         dni = input('DNI para buscar ciudad destino:')
         print(buscarCiudad(pasajeros,dni)) 
    elif opcion == 4:
         print('Mostrar cantidad de pasajero por ciudad')
         ciudad = input('Ingrese la ciudad destino:')
         total = mostrarCantidad(pasajeros,ciudad)
         print(f'La cantidad de pasajeros que viajan a {ciudad}:{total}')
    elif opcion == 5:
         print('Buscar pais destino mediante DNI')
         dni = int(input('Ingrese el DNI a buscar: '))
         pais = buscarPais(pasajeros,ciudad,dni)
         print(f'El pasajero viaja a:{pais}')
    elif opcion == 6:
         print('Cantidad de pasajeros por pais destino')
         pais_buscado =input('Ingrese el pais destino: ')
         total_pais = cantidadPasajeros(pasajeros,ciudad,pais)
         print(f'La cantida de pasajeros por pais es:{pais_buscado}:{total_pais}')
    elif opcion == 7:
         print('El programa termina..')
         break
    else:
         print('Opcion inválida, elije 1 a 7..')               
    