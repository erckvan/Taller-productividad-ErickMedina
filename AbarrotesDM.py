def registrar_producto(cantidad, productos, precio):
    ac = int(input('Ingrese la cantidad de su producto: '))
    ap = input('Ingrese el nombre de su producto: ')
    apre = int(input('Ingrese el precio de su producto: '))

    cantidad.append(ac)
    productos.append(ap)
    precio.append(apre)

# Uso de la función en el bucle principal:
while True:
    print("""
    (1) Añadir productos
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos
    (5) Salir
    """)

    respuesta = int(input('Ingrese su opción: '))

    if respuesta == 1:
        registrar_producto(cantidad, productos, precio)
    elif respuesta == 2:
        # Código para buscar productos
        pass
    elif respuesta == 3:
        # Código para modificar productos
        pass
    elif respuesta == 4:
        # Código para ver productos
        pass
    elif respuesta == 5:
        print('Gracias por utilizar nuestro sistema. ¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 5.')
