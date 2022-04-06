#Haz un juego de dos jugadores piedra papel o tijera.Piedra gana a tijera(1 gana 3);tijera gana a papel(3 gana 2);papel gana a piedra(2 gana 1).
PREGUNTA="¿[1]=piedra,[2]=papel o [3]=tijera?"
#opcion1=input(f"{PREGUNTA} Jugador 1: " )
#opcion2=input(f"{PREGUNTA} Jugador 2: ")
encontrado=False
encontrado2=False
while  not encontrado:

    opcion1=input(f"{PREGUNTA} Jugador 1: " )
    if opcion1=="1" :
        encontrado=True
        print("piedra")
    elif opcion1=="2":
        encontrado=True
        print("papel")
    elif opcion1=="3":
        encontrado=True
        print("tijera")
    else:
        print("Opción no valida")   

while  not encontrado2:
    opcion2=input(f"{PREGUNTA} Jugador 2: " )
    if opcion2=="1" :
        encontrado2=True
        print("piedra")
    elif opcion2=="2":
        encontrado2=True
        print("papel")
    elif opcion2=="3":
        encontrado2=True
        print("tijera")
    else:
        print("Opción no valida") 
    

if(opcion1==opcion2):
    print("Empate")
elif (opcion1=="1" and opcion2=="3") or (opcion1=="3" and opcion2=="2") or (opcion1=="2" and opcion2=="1"):
    print("Gana jugador 1")
else:
    print("Gana jugador 2")