import os

def crear_directorios(ruta_principal='/home/kali/Desktop/maquinas HTB/cicada'):
    # Definir la estructura de directorios
    directorios = ['Pyloads', 'nmap', 'scripts']

    # Crear el directorio base con el nombre de la máquina si no existe
    if not os.path.exists(ruta_principal):
        os.makedirs(ruta_principal)
        print(f"Directorio base '{ruta_principal}' creado.")
    else:
        print(f"El directorio base '{ruta_principal}' ya existe.")

    # Crear subdirectorios dentro del directorio base
    for directorio in directorios:
        path = os.path.join(ruta_principal, directorio)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directorio '{path}' creado.")
        else:
            print(f"El directorio '{path}' ya existe.")

# Crear los directorios en la ruta especificada
crear_directorios()
