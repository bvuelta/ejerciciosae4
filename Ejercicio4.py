import os

nombrearchivo = "datos.dat"
# Contenido esperado
esperado = b"0123456789ABCDEF"

# Si el archivo no existe, lo creamos
if not os.path.exists(nombrearchivo):
    with open(nombrearchivo, "wb") as f:
        f.write(esperado)
    print(f"Archivo '{nombrearchivo}' creado con contenido de prueba.")

# Abrimos el archivo en solo lectura
fd = os.open(nombrearchivo, os.O_RDONLY)
print(f"Descriptor abierto: {fd}")

# Movemos el puntero 5 bytes desde el inicio
offset = 5
os.lseek(fd, offset, os.SEEK_SET)
print(f"Puntero desplazado {offset} bytes desde el inicio.")

# Leemos 3 bytes desde la nueva posición
num = 3
data = os.read(fd, num)
print(f"Bytes leídos: {data}  (esperado: b'567')")

# Cerramos el descriptor
os.close(fd)
print("Descriptor cerrado")
