print('Bienvenido a sistema Abarrotes doña Mary'.center(60, '-'))
cantidad = []
productos = []
precio = []

while True:
    print("""
    (1) Añadir productos
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos
    (5) Realizar venta
    (6) Salir
    """)

    respuesta = int(input('Ingrese su opción: '))

    if respuesta == 1:
        ac = int(input('Ingrese la cantidad de su producto: '))
        ap = input('Ingrese el nombre de su producto: ')
        apre = float(input('Ingrese el precio de su producto: '))

        cantidad.append(ac)
        productos.append(ap)
        precio.append(apre)

    elif respuesta == 2:
        buscador = input('Ingrese el nombre del producto que quiere buscar: ')
        if buscador in productos:
            posicion = productos.index(buscador)
            print('La cantidad del producto es: ', cantidad[posicion])
            print('El nombre del producto es: ', productos[posicion])
            print('El precio del producto es: ', precio[posicion])
        else:
            print('Producto no encontrado.')

    elif respuesta == 3:
        pass

    elif respuesta == 4:
        print('Productos registrados:')
        for i in range(len(productos)):
            print(f"{productos[i]} - Cantidad: {cantidad[i]} - Precio unitario: {precio[i]}")

    elif respuesta == 5:
        total_venta = 0
        while True:
            producto_vendido = input('Ingrese el nombre del producto a vender o "fin" para terminar: ')
            if producto_vendido == 'fin':
                break
            if producto_vendido in productos:
                posicion = productos.index(producto_vendido)
                cantidad_vendida = int(input(f'Ingrese la cantidad a vender de {producto_vendido}: '))
                if cantidad_vendida <= cantidad[posicion]:
                    cantidad[posicion] -= cantidad_vendida
                    total_venta += precio[posicion] * cantidad_vendida
                    print(f"{cantidad_vendida} unidades de {producto_vendido} vendidas por ${precio[posicion] * cantidad_vendida}")
                    # Comprobar si la cantidad restante es menor a 50
                    if cantidad[posicion] < 50:
                        print(f"Alerta: Quedan menos de 50 unidades de {producto_vendido} en inventario.")
                else:
                    print('No hay suficiente cantidad de producto en inventario.')
            else:
                print('Producto no encontrado.')
        
        if total_venta > 0:
            print(f"Total de la venta: ${total_venta}")
            dinero_recibido = float(input('Ingrese la cantidad de dinero recibida del cliente: '))
            if dinero_recibido >= total_venta:
                cambio = dinero_recibido - total_venta
                print(f"El cambio a devolver es: ${cambio:.2f}")
            else:
                print("El dinero recibido es insuficiente para completar la transacción.")
                # Opcional: Devolver los productos al inventario en caso de dinero insuficiente

    elif respuesta == 6:
        print('Gracias por utilizar nuestro sistema. ¡Hasta luego!')
        break

    else:
        print('Opción no válida. Por favor, seleccione una opción del 1 al 6.')
