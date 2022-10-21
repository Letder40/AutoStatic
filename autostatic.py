#!/bin/bash 
import os

isroot = os.environ.get("USER")
if isroot != "root":
    print("debes ejecutarlo como root")
    exit(1)


option1 = input("Generar archivo de configuración en /etc/network/interfaces [Y] [n] ")

if option1 != "" and option1 != "Y" and option1 != "y":
    exit(0)
else:
    file = "/etc/network/interfaces"

    interfaz = input("Cual es tu interfaz primaria: \n-> ")
    address = input("address: \n-> ")
    gateway = input("gateway: \n-> ")
    network = input("network: \n-> ")
    broadcast = input("broadcast: \n-> ")
    netmask = input("netmask: \n-> ")

    if os.path.exists(file):
        command = "rm " + file
        os.system(command)
    
    f = open(file, "a")
    f.write("# Interfaz de loopback:\n")
    f.write("auto lo\niface lo inet loopback\n")
    f.write("# Interfaz primaria de red:\n")
    f.write("auto " + interfaz +  "\niface " + interfaz + " inet static\n")

    f.write("address " + address + "\n")
    f.write("gateway " + gateway + "\n")
    f.write("network " + network + "\n")
    f.write("broadcast " + broadcast + "\n")
    f.write("netmask " + netmask)
    
    f.close()


