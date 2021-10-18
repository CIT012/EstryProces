from collections import namedtuple

registros=[]
registros = namedtuple("Descripcion", "Cantidad, Costo")
registros1=("Llantas 1, 10, 1000")
resgitros2=("Llantas 2, 20, 1200")
registros.append=registros1
registros.append=resgitros2
diccionario=[]
diccionario[1]=registros1
diccionario[2]=resgitros2
diccionario.keys=diccionario[1,2]
opcion=True
while opcion==True:
    print("Menu")
    print("1:Registrar un venta")
    print("2:Consultar registro de una venta")
    print("3.Salir")
    menu=(input("Digite su opcion: "))

    if menu=='1':
        registrar=input("Escriba los detalles del registro: (Descripcion, Cantidad, Costo)")
        for registrar in registros:
            registros.append=registrar
            diccionario[3]=registrar
            print(registrar)
            break
    elif menu=='2':
        consultar=input("Digite el codigo del registro a buscar: (1-10")
        for consultar in diccionario.keys:
            print(diccionario[consultar])
    elif menu=='3':
        print("Fin.")
    else:
        print("Digite una opcion valida")
        break