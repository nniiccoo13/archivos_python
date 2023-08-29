import cachipun
import login

print("¡Bienvenido al juego de cachipun!")

if login.iniciar_sesion():
        cachipun.cachipun()
else:
        print("Vuelve para ingresar")
