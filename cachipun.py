import random
import random as r
def cachipun():
    opciones= 3
    
    opciones= ["piedra","papel","tijera"]
    jugador= input("Ingrese una opción (piedra,papel,tijera): ").lower()

    if jugador not in opciones:
        print("Opción no válida")

    else:
        oponente= random.choice(opciones)
        print(f"El oponente escogió: {oponente}")
   
        if (jugador == "piedra" and oponente ==" tijera") or (jugador== "papel" and oponente== "piedra") or (jugador=="tijera" and oponente==" papel"):
            print("Ganaste")
   
        elif  jugador == oponente:
            print("Empate")
       
        else:
            print("Perdiste")
if __name__ == "__main__":
   cachipun()