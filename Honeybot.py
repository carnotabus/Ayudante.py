# Hecho por vulkano en modo de práctica
import os
os.system("clear")
print("\n Bienvenido al ayudante vul, yo te ayudare a crear\n multiples carpetas en una ruta especifica o multiples\n archivos de la extension que quieras!!!!")
print("\n Para comenzar necesito que me indiques\n que haras carpetas o ficheros (archivos)?")
p1 = int(input(" 1) Carpetas\n 2) Ficheros\n [Respuesta --> "))

if p1 == 1:
	print("\n Existe 2 opciones......\n 1) Crear multiples carpetas con el mismo nombre\n 2) Crear multiples carpetas con diferentes nombres")
	r1 = int(input(" [Respuesta: "))
	if r1 == 1:
		numnom = 0
		numero = 0
		cantidad = int(input("\n Cuantas carpetas desea crear?: "))
		nombre = input("\n ¿Que nombre desea que tengan la/s carpeta/s?\n (si el nombre es largo porfavor use el _ ejemplo: nombre_largo)\n PD: --no puede crear carpetas con el mismo nombre--: ")
		ruta = input("\n indiquenos la ruta destinada donde se crearan\n las carpetas (ejemplo: ruta/carpeta_prueba): ")
		while numero != cantidad:
			os.system(f"mkdir -m 777 {nombre}{numnom}")
			os.system(f"mv {nombre}{numnom} {ruta}")
			numnom += 1
			numero += 1

	if r1 == 2:
		num = 0
		nombre = "hola"
		ruta = input("\n Indiquenos la ruta destinada donde se crearan\n las carpetas (ejemplo: ruta/carpeta_prueba): ")
		while nombre != "n":
			os.system("clear")
			print(f"\n Hasta el momento ha creado {num} carpeta/s")
			nombre = input("\n ¿Que nombre desea que tenga la/s carpeta/s?\n (si el nombre es largo porfavor use el _ ejemplo: nombre_largo)\n PD: --no puede crear carpetas con el mismo nombre--\n para parar de crear carpetas escriba 'n': ")
			os.system(f"mkdir -m 777 {nombre}")
			os.system(f"mv {nombre} {ruta}")
			os.system(f"rmdir {ruta}/n")
			num += 1








if p1 == 2:
	print("\n Existe 2 opciones......\n 1) Crear multiples archivos con el mismo nombre\n 2) Crear multiples archivos con diferentes nombres")
	r1 = int(input(" [Respuesta: "))
	if r1 == 1:
		numnom = 0
		numero = 0
		cantidad = int(input("\n Cuantos archivos desea crear?: "))
		nombre = input("\n ¿Que nombre desea que tengan los archivos?\n (si el nombre es largo porfavor use el _ ejemplo: nombre_largo)\n PD: --no puede crear archivos con el mismo nombre--: ")
		ruta = input("\n Indiquenos la ruta destinada donde se crearan\n los archivos (ejemplo: ruta/carpeta): ")
		ext = input("\n Indiquenos que extension tendra el archivo ejemplo(txt o py): ")
		while numero != cantidad:
			os.system(f"touch {nombre}{numnom}.{ext}")
			os.system(f"mv {nombre}{numnom}.{ext} {ruta}")
			numnom += 1
			numero += 1

	if r1 == 2:
		num = 0
		nombre = "hola"
		ruta = input("\n Indiquenos la ruta destinada donde se crearan\n los archivos (ejemplo: ruta/carpeta_prueba): ")
		ext = input("\n Indiquenos que extension tendra el archivo ejemplo(txt o py): ")
		while nombre != "n":
			os.system("clear")
			print(f"\n Hasta el momento ha creado {num} archivos")
			nombre = input("\n ¿Que nombre desea que tenga el archivo?\n (si el nombre es largo porfavor use el _ ejemplo: nombre_largo)\n PD: --no puede crear archivos con el mismo nombre--\n para parar de crear archivos escriba 'n': ")
			os.system(f"touch {nombre}.{ext}")
			os.system(f"mv {nombre}.{ext} {ruta}")
			os.system(f"rm -r {ruta}/n.{ext}")
			num += 1

os.system("clear")
print("\n Gracias por usarme!!! espero haberte ayudado!!! :D")

