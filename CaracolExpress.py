import os
os.system("cls")
listipo = ['PAQUETE'] #Puede ser sobre o paquete
lisnomdest=['SEBASTIAN'] #Solo primer nombre
lisrutdest=['20362266-K'] #Rut debe tener guión como penultimo
lispesokg=[5.0] #En kg, puede ser con decimal
lisprecio=[15000] #Se debe añadir junto con los demas datos
lisciudad=['CONCEPCION',]
menu = """
    Bienvenido a CaracolExpress
----------------------------------
1.Registrar Encomienda
2.Buscar Encomiendas por Rut
3.Listar Encomiendas
4.Salir
----------------------------------

"""
def grabar():
 os.system("cls")
 while True:
    try:
        tipo=str(input("Ingrese tipo de encomienda. Puede ser SOBRE o PAQUETE, y debe estar en mayusculas: "))
        if tipo.isupper() == False:
            print("Tipo ingresado no es válido. Intente nuevamente.")
        else:
            listipo.append (tipo)
            os.system("cls")
            break
    except NameError:
        print("Ha occurido un error. Intente nuevamente.")
 while True:
    try:       
        nomdest=input("Ingrese el primer nombre del destinatario. Debe estar en mayusculas: ")
        if len(nomdest) < 2 or len(nomdest) > 30 or nomdest.isupper() == False:
            print("El nombre ingresado no es valido. Intente nuevamente.")
        else:
            if nomdest.isupper() == True:
                lisnomdest.append(nomdest)
                os.system("cls")
                break
    except:
        print("Ha ocurrido un error. Intente nuevamente.")
 while True:
    try:
        contguion = 0
        rutdest=input("Ingrese el rut del destinatario. Sin puntos, y con guión: ")
        for i in range(len(rutdest)):
            if rutdest[i] == '-':
                contguion += 1
        if contguion == 1 and rutdest[-2] == '-':
            lisrutdest.append(rutdest)
            os.system("cls")
            break            
    except:
        print("Ha ocurrido un error. Intente nuevamente.")
 while True:
    try:
        peso=float(input("Ingrese el peso de la encomienda en kg, con un decimal: "))
        if peso > 0.1:
            lispesokg.append(peso)
            break
        else:
            print("El peso ingresado es muy bajo. Ingrese un peso mayor a 0.1 kg.")
    except:
        print("Ha ocurrido un error. Intente nuevamente.")
 while True:
    try:
        precio=int(input("Ingrese el precio de la encomienda. Debe ser mayor a $2000: "))
        if precio > 2000:
            lisprecio.append(precio)
            os.system("cls")
            break
        else:
            print("El precio ingresado es muy bajo. Intente nuevamente. ")
    except:
        print("Ha ocurrido un error. Intente nuevamente.")
 while True:
     try:
         ciudad=input("Ingrese la ciudad de destino. Debe estar todo en mayusculas: ")
         if len(ciudad) > 3 and ciudad.isupper() == True:
             lisciudad.append(ciudad)
             os.system("cls")
             break
         else:
             print("La ciudad ingresada es invalida. Intente nuevamente.")
     except:
         print("Ha ocurrido un error. Intente nuevamente.")    
def buscarporrut():
    os.system("cls")
    rut=input("Ingrese rut a buscar, sin puntos y con guión: ")
    print(f"Encomiendas asociadas a rut {rut} \n:")
    print("TIPO      | NOMBRE DESTINATARIO  | RUT DESTINATARIO    |PESO EN KG| PRECIO | CIUDAD                | ")
    print("----------+----------------------+---------------------+----------+--------+-----------------------|")
    for i in range(len(listipo)):
        print(f"{listipo[i]:9s} | {lisnomdest[i]:20s} | {lisrutdest[i]:19s} | {lispesokg[i]:5f} | {lisprecio[i]:6d} | {lisciudad[i]:21s} |")
        print("----------+----------------------+---------------------+----------+--------+-----------------------|")
def listaencomiendas():
    os.system("cls")
    print("TIPO      | NOMBRE DESTINATARIO  | RUT DESTINATARIO    |PESO EN KG| PRECIO | CIUDAD                | ")
    print("----------+----------------------+---------------------+----------+--------+-----------------------|")
    for i in range(len(listipo)):
        print(f"{listipo[i]:9s} | {lisnomdest[i]:20s} | {lisrutdest[i]:19s} | {lispesokg[i]:5f} | {lisprecio[i]:6d} | {lisciudad[i]:21s} |")
        print("----------+----------------------+---------------------+----------+--------+-----------------------|")
    volv=input("Presione Enter para volver atras")

while True:
    try:
        os.system("cls")
        opc=int(input(menu))
        if opc == 1:
            grabar()
        if opc == 2:
            buscarporrut()
        if opc == 3:
            listaencomiendas()
        if opc == 4:
            os.system("cls")
            print("Gracias por usar CaracolExpress.")
            print("Programa creado en python por Sebastian Santa Maria")
            print("V1.0")
    except:
        print("Ha ocurrido un error. Intente nuevamente. ")