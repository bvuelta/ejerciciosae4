import os
import sys

# Intento fork
if not hasattr(os, "fork"):
    print("La plataforma no soporta os.fork(). Este ejercicio requiere un sistema Unix-like.")
    sys.exit(1)

# Llamada a fork
ret = os.fork()

if ret == 0:
    print("Soy el proceso hijo con PID:", os.getpid())
    # Salimos del proceso hijo
    os._exit(0)
else:
    # Estamos en el proceso padre
    print("Soy el proceso padre con PID:", os.getpid())
    print("Mi hijo tiene el PID:", ret)
    
    try:
        pid, status = os.waitpid(ret, 0)
        print(f"Hijo {pid} finalizado con estado {status}.")
    except ChildProcessError:
        print("No hay hijo")

