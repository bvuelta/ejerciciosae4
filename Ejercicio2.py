# Ejercicio 2

import os
import errno

# Nombre del archivo
nombrearchivo = "registro.txt"

# Flags
flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL

# Modo de permisos si se crea el archivo (rw/r/w)
mode = 0o644

# Intentamos abrir el descriptor de archivo usando os.open
try:
    fd = os.open(nombrearchivo, flags, mode)
    # Mensaje de confirmación
    print(f"Archivo '{nombrearchivo}' creado y abierto, descriptor: {fd}")
    # Contenido a escribir en bytes
    data = b"Linea de prueba de system call.\n"
    # Escribimos los bytes al descriptor con os.write
    bytes_escritos = os.write(fd, data)
    print(f"Bytes escritos: {bytes_escritos}")
    # Cerramos el descriptor con os.close
    os.close(fd)
    print("Descriptor cerrado correctamente.")
except OSError as e:
    # Si el archivo ya existe y se usó O_EXCL, se mandará un error EEXIST
    if e.errno == errno.EEXIST:
        print(f"Error: El archivo '{nombrearchivo}' ya existe. (errno.EEXIST)")
    else:
        print(f"Error al crear/escribir el archivo: {e}")
