def iniciar_sesion():
    usuario="nicolas_perez"
    contraseña="nico1234"

    nombre_usuario=input("ingrese su nombre de usuario: ")
    contra=input("ingrese su contraseña: ") 

    if usuario == nombre_usuario and contraseña == contra:
      return True 
    else:
       return False
if __name__ == "__main__":
   iniciar_sesion()