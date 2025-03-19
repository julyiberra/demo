#import string
import random

print("Generador de claves!")

#["a", "b", ..., "1", ..., "."]
#chars = string.ascii_letters + string.digits + string.punctuation
chars = ["a","b","c","-",".","|","d"]
password = ""
length = int(input("Ingrese la longitud de la contraseña: "))

for _ in range(length):
    password = password + random.choice(chars)

print("Contraseña generada:", password)