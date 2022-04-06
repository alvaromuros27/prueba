#Hacer el ejercicio anterior pero con funciones.

def num_adecuado(jugador):
    #opcion1=input(f"{PREGUNTA} Jugador 1: " )
    #opcion2=input(f"{PREGUNTA} Jugador 2: ")
    PREGUNTA="¿[1]=piedra,[2]=papel o [3]=tijera?"
    encontrado=False
    while  not encontrado:

        opcion=input(f"{jugador} {PREGUNTA} " )
        if opcion=="1" :
            encontrado=True
            print("piedra")
        elif opcion=="2":
            encontrado=True
            print("papel")
        elif opcion=="3":
            encontrado=True
            print("tijera")
        else:
            print("Opción no valida")   
    return opcion


def comprobar(op1, op2,j1,j2):
    if(op1==op2):
            print("Empate")
    elif (op1=="1" and op2=="3") or (op1=="3" and op2=="2") or (op=="2" and op2=="1"):
            print(f"Gana {j1}")
    else:
            print(f"Gana {j2}")


jugador1=input("¿Como te llamas? ")
opcion1=num_adecuado(jugador1)
jugador2=input("¿Como te llamas? ")
opcion2=num_adecuado(jugador2)

comprobar(opcion1, opcion2,jugador1,jugador2)


