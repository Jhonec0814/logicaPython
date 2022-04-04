productos=[]
opcion=1


while(opcion !=0):
    producto={}
    opcion=int(input("Digite una opcion: "))
    if(opcion ==1):
        producto['codigo']=input('digite el codigo del producto: ')
        producto['nombre']=input('digite el nombre del producto: ')
        producto['precio']=int(input('digite el precio del producto: '))

        productos.append(producto)

    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        print("")
    else:
        print("")            