import random
numPerros = 0
datosPoliperros = {
  "nombre" : [],
  "huellaDactilar": []
}
fotosPoliperros = {
  "foto" : []
}

print("-------------POLIPERROS -------------")
print("-------------Bienvenido(a)-------------")
print("¿Qué acción desea realizar?")
print("1) Registrar poliperros")
print("2) Mostrar poliperros")
print("3) Registrar foto del poliperros")
print("4) Actualizar datos del poliperro")
print("5) Salir")
tipoAccion = int(input("Ingrese la opción: "))

"""def actualizarname(huella):
  if nuevoHuella==datosPoliperros["huellaDactilar"]:"""


def actualizarNombre(huella):
   
    if huella in datosPoliperros["huellaDactilar"]:
        indice=(datosPoliperros["huellaDactilar"].index(huella))
        print(indice)
        print("Ingrese el nuevo nombre: ")
        nuevoNombre = input("Nombre: ")
        print(nuevoNombre)
        datosPoliperros["nombre"][indice]=nuevoNombre

        #datosPoliperros["nombre"].append(nuevoNombre)
    else:
      print("La huella no se encontro")


while tipoAccion != 5:
  if tipoAccion == 1:
    print("Caso 1")
    numPerros = int(input("Ingresa el número de poliperros: "))
    for i in range(numPerros):
      print("Ingresa los datos del poliperro", i+1)
      nombre = input("Nombre: ")
      huellaDactilar = input("Huella: ")
      datosPoliperros["nombre"].append(nombre)
      datosPoliperros["huellaDactilar"].append(huellaDactilar)

  elif tipoAccion == 2:
    print("Caso 2")
    for i in range(numPerros):
      print("----------------------------------")
      print("Mostrar los datos del Poliperro ", i+1)
      print("\t*Nombre", datosPoliperros["nombre"][i])
      print("\t*Huella Dactilar", datosPoliperros["huellaDactilar"][i])
      if "foto" in datosPoliperros:
        print("\t*Foto", datosPoliperros["foto"][i])
      print("----------------------------------")
      
  elif tipoAccion == 3:
    print("Caso 3")
    for i in range(numPerros):
      print("Ingrese la foto del poliperro")
      print("¿El poliperro dispone de foto?")
      foto = input("Ingrese si o no: ")
      if foto == "si":
        foto = input("Foto: ")
        fotosPoliperros["foto"].append(foto)
      else:
        fotosPoliperros["foto"].append("Foto-prueba.png")
      datosPoliperros.update(fotosPoliperros)
  elif tipoAccion == 4:
    buscar = input("Ingrese la huella dactilar del poliperro: ")
    actualizarNombre(buscar)

  print("¿Qué acción desea realizar?")
  print("1) Registrar poliperros")
  print("2) Mostrar poliperros")
  print("3) Registrar foto del poliperros")
  print("4) Actualizar datos del poliperro")
  print("5) Salir")
  tipoAccion = int(input("Ingrese la opción: "))
  
print("Muchas gracias")







