import string
import random

longitud = int(input("Ingrese el tamaño de la contraseña: "))

#ascci todas las letras del abecedario, todos los digitos y puntuaciones
caracteres = string.ascii_letters + string.digits + string.punctuation

#join para concatenar los caracteres y un ciclo for para el tamaño de la contraseña ingresada por el usuario
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

#imprimir la contra
print("La contraseña random generada es: " + contraseña)