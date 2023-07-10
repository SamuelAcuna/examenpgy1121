from os import system
system("cls")
from datetime import datetime
entradas = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
platinum = 120000
gold = 80000
silver = 50000
recaudacion = 0
rec_platino = 0
rec_gold = 0
rec_silver = 0
can_platino = 0
can_gold = 0
can_silver = 0
can_total = 0
def in_rut():
    rut = input("Ingrese el rut del asistente: ")
    if len(rut)>6 and len(rut)<9:
        if rut.isnumeric():
            return rut
        else:
            input("Entrada invalida............")
            return in_rut()
    else:
        input("Entrada invalida..........")
        return in_rut()
def in_numentradas():
    ent = input("Ingrese el numero de entradas a comprar: ")
    if ent.isnumeric():
        ent = int(ent)
        if ent>0 and ent<4:
            return ent
        else:
            input("Solo se puede comprar entre 1 y 3 entradas....")
            return in_numentradas()
    else:
        input("Entrada invalida............")
        return in_numentradas()
def mostrar_ubicaciones():
    system("cls")
    global entradas
    print("""
        __________________________________________________________
        |                                                        |
        |                      ESCENARIO                         |
        |                                                        |
        ----------------------------------------------------------
    
    """)
    for i in range(100):
        if entradas[i]=="":
            print(i+1,end="\t")
        else:
            print("X", end="\t")
        if i%10==9:
            print(end="\n")
def in_lugar():
    mostrar_ubicaciones()
    global can_gold,can_platino,can_silver,rec_gold,rec_platino,rec_silver
    lugar = input("Ingrese lugar a reservar: ")
    if lugar.isnumeric():
        lugar = int(lugar)
        if lugar>0 and lugar<101:
            i = lugar-1
            if entradas[lugar-1]=="":
                rut = in_rut()
                entradas[lugar-1]=rut
                if i<20:
                    if entradas[i]!="":
                        can_platino=can_platino+1
                        rec_platino=rec_platino+platinum
                elif i>=20 and i<50:
                    if entradas[i]!="":
                        can_gold=can_gold+1
                        rec_gold=rec_gold+gold
                else:
                    if entradas[i]!="":
                        can_silver=can_silver+1
                        rec_silver=rec_silver+silver
                input("Operacion realizada exitosamente.......")
            else:
                input("Ubicacion ya reservada......")
                return in_lugar()
        else:
            input("La ubicacion ingresada no existe.........")
            return in_lugar()
            




while True:
    system("cls")
    print(""" 
        1. Comprar entradas
        2. Mostrar ubicaciones disponibles
        3. Ver listado de asistentes
        4. Mostrar ganancias totales
        5. Salir
    """)
    op = input("Ingrese la funcion del programa a operar: ")
    if op == "1":
        print("Compra de entradas ")
        centradas = in_numentradas()
        for i in range(centradas):
            system("cls")
            in_lugar()
    elif op == "2":
        print("Ubicaciones disponibles ")
        mostrar_ubicaciones()
        input("Presione una tecla para continuar.......")
    elif op == "3":
        print("Listado de asistentes ")
        asistentes = sorted(entradas)
        print("Asistentes del concierto", end="\n\n")
        for i in range(100):
            if asistentes[i]!="":
                print(f" {asistentes[i]}")
            
        input("Presione una tecla para continuar.......")
    elif op == "4":
        print("Recaudacion a la fecha ")
        recaudacion = rec_silver+rec_gold+rec_platino
        can_total = can_silver+can_gold+can_platino
        print(f"""
            |   Tipo Entrada    |   Cantidad    |       Total           |
            |   Platinum        |       {can_platino}\t|\t\t${rec_platino}\t|
            |   Gold            |       {can_gold}\t|\t\t${rec_gold}\t|
            |   Silver          |       {can_silver}\t|\t\t${rec_silver}\t|
            |   Total           |       {can_total}\t|\t\t${recaudacion}\t|
        """)
        input("Presione una tecla para continuar.......")
    elif op == "5":
        system("cls")
        break
    else:
        input("Opcion invalida............")
print("Fin del programa")
print("Samuel Acuña", "     ", datetime.now())
