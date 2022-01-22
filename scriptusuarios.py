import os
import time


tipo = str
os.system("clear")

while True:
    print("Menu")
    print("1) Crear usuario administrador")
    print("2) Crear usuario normal")
    print("3) Salir del script")
    tipo = str(input("Elige el tipo de usuario: \n"))
    os.system("cat /etc/passwd > usuarios.txt")

    if tipo == "1":
        with open('usuarios.txt', 'r') as file:
            data = file.read()
        nombre = str(input("Ingresa el nombre del usuario \n"))
        verificador = nombre + ":"
        if verificador in data:
            print("Este usuario ya existe")
            time.sleep(1)
        else:
            uadd = "useradd -m " + nombre
            upsw = "passwd " + nombre
            admin = "usermod -aG admin " + nombre
            os.system(uadd)
            os.system(upsw)
            os.system(admin)
            grupo = str(input("Ingrese el grupo del usuario \n"))
            addgp = "addgroup " + grupo
            addusg = "usermod -aG " + grupo + " " + nombre
            os.system(addgp)
            os.system(addusg)
            os.system("clear")
    elif tipo == "2":
        with open('usuarios.txt', 'r') as file:
            data = file.read()
        nombre = str(input("Ingresa el nombre del usuario \n"))
        verificador = nombre + ":"
        if verificador in data:
            print("Este usuario ya existe")
            time.sleep(1)
        else:
            uadd = "useradd -m " + nombre
            upsw = "passwd " + nombre
            os.system(uadd)
            os.system(upsw)
            grupo = str(input("Ingrese el grupo del usuario \n"))
            addgp = "addgroup " + grupo
            addusg = "usermod -aG " + grupo + " " + nombre
            os.system(addgp)
            os.system(addusg)
            os.system("clear")
    elif tipo == "3":
        break
    else:
        print("Elige una opcion correctamente")
        time.sleep(1)
        os.system("clear")
