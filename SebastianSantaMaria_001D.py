import os
import numpy
os.system("cls")
from colorama import Fore,Style,Back

#listas

lisnom= []
lisrut = []
escenario = [[1,2,3,4,5,6,7,8,9,10],
             [11,12,13,14,15,16,17,18,19,20],
             [21,22,23,24,25,26,27,28,29,30],
             [31,32,33,34,35,36,37,38,39,40],
             [41,42,43,44,45,46,47,48,49,50],
             [51,52,53,54,55,56,57,58,59,60],
             [61,62,63,64,65,66,67,68,69,70],
             [71,72,73,74,75,76,77,78,79,80],
             [81,82,83,84,85,86,87,88,89,90],
             [91,92,93,94,95,96,97,98,99,100]]

#Menus

menuprin = """
    -Bienvenido a Creativos.cl-
--------------------------------------
1. Comprar Entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
--------------------------------------
"""
menutipoentradas = """
    -Seleccione un tipo de entradas-
-----------------------------
   Tipo              Valor
----------          --------
1.Patinum           $120.000
2.Gold              $80.000
3.Silver            $50.000
------------------------------
"""
#Funciones

def compraentrada():
    global contplat
    global contgold
    global contsilver
    while True: #Ingreso de nombre y apellido
        try:
            nom=str(input("Ingrese su nombre y apellido, capitalizando ambos: "))
            lisnom.append(nom)
            break
        except:
            print("Ha ocurrido un error. Intente nuevamente.\n")
    while True: #Ingreso de rut
        try:
            rut=str(input("Ingrese su rut, sin puntos y con guión: "))
            contguion = 0
            for i in range(len(rut)):
                if rut[i] == '-':
                    contguion+=1
            if contguion == 1 and rut[-2] == '-':
                lisrut.append(rut)
                break
            else:
                print("El rut ingresado es invalido. Intente nuveamente.\n")
        except:
            print("Ha ocurrido un error. Intente nuevamente.\n")
    while True: #Seleccion tipo y cantidad de entradas
        try:
            entradasdisp = 100
            opctipoent=int(input(menutipoentradas))
            if opctipoent == 1:
                cantplatinum=int(input("Ingrese cantidad de entradas a comprar, entre 1 y 3: "))
                if cantplatinum < 1 or cantplatinum > 3:
                    print("Cantidad ingresada es invalida. Intente nuevamente.\n")
                else:
                    contplat = 0
                    contplat += cantplatinum
                    tipoent = 'Platinum'
                    costoent = cantplatinum * 120000
                    entradasdisp -= cantplatinum
                    break
            elif opctipoent == 2:
                cantgold=int(input("Ingrese cantidad de entradas a comprar, entre 1 y 3: "))
                if cantgold < 1 or cantgold > 3:
                    print("Cantidad ingresada es invalida. Intente nuevamente.\n")
                else:
                    costoent = cantgold * 80000
                    tipoent = 'Gold'
                    global contgold
                    contgold = 0
                    contgold += cantgold
                    entradasdisp -= cantgold
                    break
            elif opctipoent == 3:
                cantsilver=int(input("Ingrese cantidad de entradas a comprar, entre 1 y 3: "))
                if cantsilver < 1 or cantsilver > 3:
                    print("Cantidad ingresada es invalida. Intente nuevamente.\n")
                else:
                    global contsilver
                    contsilver = 0
                    contsilver += cantsilver
                    tipoent = 'Silver'
                    costoent = cantsilver * 50000
                    entradasdisp -= cantsilver
                    break
            print(f"""
                      BOLETA
             -------------------------
             Nombre:{nom}
             Rut: {rut}
             Entrada: {tipoent}
             Valor a pagar: ${costoent}
             -------------------------
             """)
            input("Presione enter para continuar")
        except:
            print("Ha ocurrido un error. Intente nuevamente.\n")
    print(f"""
                      BOLETA
             -------------------------
             Nombre:{nom}
             Rut: {rut}
             Entrada: {tipoent}
             Valor a pagar: ${costoent}
             -------------------------
             """)
    input("Presione enter para continuar")

def gananciastotales(): 
 global totalplat
 totalplat = contplat * 120000
 global totalgold
 totalgold = contgold * 80000
 global totalsilver
 totalsilver = contsilver * 50000
 print(f"""
|Tipo Entrada  | Cantidad |  Total  |
+--------------+----------+---------+
|Platinum      |{contplat:10d}|{totalplat:9d}|
|Gold          |{contgold:10d}|{totalgold:9d}|
|Silver        |{contsilver:10d}|{totalsilver:9d}|
|Total         |{contplat + contgold + contsilver:10d}|{totalplat + totalgold + totalsilver:9d}|
+--------------+--------------------+""")

def atendientes():
    print(f"""
    |Nombre                  +Rut              +
    |------------------------|-----------------|""")
    for i in range(len(lisnom)):
        print(f"    |{lisnom[i]:24s}|{lisrut[i]:17s}|")
    input("Presione enter para volver al menu")

def salir():
    print ("""Gracias por usar Creativos.cl
    Aplicacion creada por Sebastian Santa María, fecha 10/07/23""")
while True:
    try:
        opc=int(input(menuprin))
        if opc == 1:
            compraentrada()
        elif opc == 2:
            print("opcion 2")
        elif opc == 3:
            atendientes()
        elif opc == 4:
            gananciastotales()
        elif opc == 5:
            salir()
            break
    except:
        print("Ha ocurrido un error. Intente nuevamente.\n")

print(lisnom)
print(lisrut)