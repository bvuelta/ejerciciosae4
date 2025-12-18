import os  # Importamos el módulo os que expone llamadas al sistema en Python

# Obtenemos el ID del proceso actual (PID)
pid = os.getpid()
# Imprimimos el PID por pantalla 
print(f"PID del proceso actual: {pid}")

# Obtenemos el ID del proceso padre 
ppid = os.getppid()
# Imprimimos el PPID
print(f"PPID (proceso padre): {ppid}")

# Obtenemos el UID efectivo con el que se ejecuta el proceso
try:
    uid = os.geteuid()  
except AttributeError:
    try:
        uid = os.getuid()
    except AttributeError:
        uid = None

# Mostramos el UID si está disponible
if uid is not None:
    print(f"UID efectivo: {uid}")
else:
    print("UID no disponible")
