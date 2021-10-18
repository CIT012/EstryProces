from collections import namedtuple

registros=[]
registrost = namedtuple('Descripcion', ['cantidad', 'costo'])
registros1=("Llantas 1, 10, 1000")
registros2=("Llantas 2, 20, 1200")
registros.append(registros1)
registros.append(registros2)
diccionario={}
diccionario[1001]=registros1
diccionario[1002]=registros2

opcion=True
while opcion==True:
    print("Menu")
    print("1:Registrar un venta")
    print("2:Consultar registro de una venta")
    print("3.Salir")
    menu=(input("Digite su opcion: "))
    if menu=='1':
        registrar=input("Escriba los detalles del registro: (Descripcion, Cantidad, Costo): ")
        for l in registros:
            registros.append(registrar)
            diccionario[1003]=registrar
            print(registrar)
            break
        iva=registrar.costo * 0.16
        total=iva+registrar.costo
        print(iva,total)
        print(registros)
    elif menu=='2':
        consultar=input("Digite el codigo del registro a buscar (1001-1010): ")
        print(diccionario[consultar])
    elif menu=='3':
        print("Fin.")
    else:
        print("Digite una opcion valida")
        break