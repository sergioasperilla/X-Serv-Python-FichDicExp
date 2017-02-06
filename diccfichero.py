#!/usr/bin/python3

fich = open('/etc/passwd','r')
lineas = fich.readlines()
usuarios = {}

for linea in lineas:
	login = linea.split(':')[0]
	shell = linea.split(':')[-1][:-1]
	usuarios[login] = shell

try:
	x=input("Introduce un usuario:")
	print(x,usuarios[x])
except:
	print("No existe este usuario")

fich.close()
