import os
os.system("cls")
flag = True
pedido = False

hamburguesa = 5000
pizza = 8000
ensalada = 4000
contador_hamburguesa = 0
contador_pizza = 0
contador_ensalada = 0
contador_cantidad = 0
#validacion del cliente

print("Bienvenido a nuestro programirestaurante.")
nombre = input("Ingrese su nombre:\n")
while len(nombre) not in range(3,21):
    nombre = input("Ingrese un nombre entre 3 y 20 caracteres:\n")
rut = input("Ingrese su rut:\n")
while len(rut) < 8:
    rut = input("Largo no valido, ingrese un rut de al menos 8 digitos:\n")
while flag:
    print("1. Agregar pedido")
    print("2. Ver resumen")
    print("3. Descargar boleta")
    print("4. Salir")
    
    try:
        opcion = int(input("Ingrese opcion:\n"))
        
        if opcion == 1:
            print("Menu:")
            print("1. Hamburguesa($5000)")
            print("2. Pizza($8000)")
            print("3. Ensalada($4000)")
            carta = int(input("Escoga que desea agregar:\n"))
            
            if carta == 1:
                contador_cantidad = int(input("Ingrese cantidad:\n"))
                while contador_cantidad not in range(1,11):
                    contador_cantidad = int(input("El valor ingresado debe ser entre 1 y 10.\nIngrese un valor valido:\n"))
                contador_hamburguesa = contador_hamburguesa + contador_cantidad
                pedido = True
                
            elif carta == 2:
                while contador_cantidad not in range(1,11):
                    contador_cantidad = int(input("El valor ingresado debe ser entre 1 y 10.\nIngrese un valor valido:\n"))
                contador_pizza = contador_pizza + contador_cantidad
                pedido = True
            elif carta == 3:
                while contador_cantidad not in range(1,11):
                    contador_cantidad = int(input("El valor ingresado debe ser entre 1 y 10.\nIngrese un valor valido:\n"))
                contador_ensalada = contador_ensalada + contador_cantidad
                pedido = True
            else:
                carta = int(input("Opcion no programivalida"))
            total_pedido = (hamburguesa * contador_hamburguesa) + (pizza * contador_pizza) + (ensalada * contador_ensalada)
        elif opcion == 2:
            if pedido:
                print(f"Resumen pedido:\n")
                print(f"Nombre cliente:{nombre}\nRut:{rut}")
                if contador_hamburguesa >=1:
                    print(f"Cantidad Hamburgesas:{contador_hamburguesa}")
                if contador_pizza >=1:
                    print(f"Cantidad Pizza:{contador_pizza}")
                if contador_ensalada >=1:
                    print(f"Cantidad ensaladas:{contador_ensalada}")
                print(f"\nTotal: ${total_pedido}")
            else:
                print("No se ha realizado un pedido\n")
        elif opcion == 3:
            print("algun dia existira una boleta lmao")
        elif opcion == 4:
            print("Hata la programiproxima")
            flag = False
        else:
            opcion = int(input("La opcion no es valida"))
        
        
        
        
        
    except:
        print("Uno o más valores no programivalidos")





