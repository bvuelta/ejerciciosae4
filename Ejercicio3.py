# Ejercicio 3

import os
import errno

nombrearchivo = "registro.txt"

# Abrimos el archivo en modo lectura
try:
    fd = os.open(nombrearchivo, os.O_RDONLY)
    print(f"Descriptor abierto para lectura: {fd}")
    # Leemos 10 bytes del archivo
    n = 10
    data = os.read(fd, n)
    # Imprimimos los datos leídos
    print(f"Datos leídos ({n} bytes): {data}")
    # Cerramos el descriptor
    os.close(fd)
    print("Descriptor cerrado correctamente.")
except OSError as e:
    if e.errno == errno.ENOENT:
        print(f"Error: El archivo '{nombrearchivo}' no existe. Ejecuta primero el ejercicio 2.")
    else:
        print(f"Error al leer el archivo: {e}")
