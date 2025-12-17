# Ejercicio 1

import os  # Importamos el módulo os que expone llamadas al sistema en Python

# Obtenemos el ID del proceso actual (PID)
pid = os.getpid()
# Imprimimos el PID por pantalla con contexto
print(f"PID del proceso actual: {pid}")

# Obtenemos el ID del proceso padre (PPID)
ppid = os.getppid()
# Imprimimos el PPID
print(f"PPID (proceso padre): {ppid}")

# Obtenemos el UID efectivo con el que se ejecuta el proceso
# Atención: en sistemas Windows esta función puede no existir; en Unix/Linux si
try:
    uid = os.geteuid()  # get effective uid (Unix)
except AttributeError:
    # Fallback a getuid si geteuid no está disponible
    try:
        uid = os.getuid()
    except AttributeError:
        uid = None

# Mostramos el UID si está disponible
if uid is not None:
    print(f"UID efectivo: {uid}")
else:
    print("UID no disponible")
