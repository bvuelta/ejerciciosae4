# Ejercicio 5

import os
import sys

# Intentamos hacer fork; si la plataforma no soporta fork, avisamos
if not hasattr(os, "fork"):
    print("La plataforma no soporta os.fork(). Este ejercicio requiere un sistema Unix-like.")
    sys.exit(1)

# Llamada a fork: devuelve 0 en el hijo y el PID del hijo en el padre
ret = os.fork()

if ret == 0:
    # Estamos en el proceso hijo
    print("Soy el proceso hijo con PID:", os.getpid())
    # Salimos inmediatamente del proceso hijo sin ejecutar código restante
    os._exit(0)
else:
    # Estamos en el proceso padre, 'ret' contiene el PID del hijo
    print("Soy el proceso padre con PID:", os.getpid())
    print("Mi hijo tiene el PID:", ret)
    
    try:
        pid, status = os.waitpid(ret, 0)
        print(f"Hijo {pid} finalizado con estado {status}.")
    except ChildProcessError:
        print("No hay hijo que esperar o ya ha sido reaped.")

