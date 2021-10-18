from collections import namedtuple

registros=[]
registros = namedtuple("Descripcion", "Cantidad, Costo")
registros1=("Llantas 1, 10, 1000")
resgitros2=("Llantas 2, 20, 1200")
registros.append=registros1
registros.append=resgitros2
opcion=True
while opcion==True:
    print("Menu")
    print("1:Registrar un venta")
    print("2:Consultar registro de una venta")
    print("3.Salir")
    
