import pytest
import subprocess

def pytest_sessionfinish(session, exitstatus):
    # Esta función se ejecutará después de que se completen todas las pruebas
    
    try:
        comando = "cat /proc/self/cgroup"
        comando = "docker ps"
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
        container_id = resultado.stdout.strip()
        print('hola')
        print(resultado)
        
        # comando = ["docker", "cp", f"{container_id}:/app/report.html", '/mnt/c/Users/Administrador.JS-PORT/Desktop/Empleo/bcnc_new/bcnc/']
        # subprocess.run(comando, check=True)

    except subprocess.CalledProcessError as e:
        # Captura y maneja errores si el comando falla
        print("Error al ejecutar el comando:", e)