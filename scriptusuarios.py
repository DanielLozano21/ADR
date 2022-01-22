import os

tipo = str

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
        else:
            uadd = "useradd -m " + nombre
            upsw = "passwd " + nombre
            admin = "usermod -aG admin " + nombre
            os.system(uadd)
            os.system(upsw)
            os.system(admin)


    elif tipo == "2":
        nombre = str(input("Ingresa el nombre del usuario \n"))
        password = str(input("Ingresa la contraseña \n"))
        grupo = str(input("Ingresa el nombre del grupo \n"))

        uadd = "useradd -m" + nombre

    elif tipo == "3":
        quit
    else:
        print("Elige una opcion correctamente")
