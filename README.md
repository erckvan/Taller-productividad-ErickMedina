# Taller-productividad-ErickMedina
Actualizar esta tarea con el codigo.

def registrar_producto(cantidad, productos, precio):
    ac = int(input('Ingrese la cantidad de su producto: '))
    ap = input('Ingrese el nombre de su producto: ')
    apre = int(input('Ingrese el precio de su producto: '))

    cantidad.append(ac)
    productos.append(ap)
    precio.append(apre)

print('Bienvenido a sistema Abarrotes doña Mary'.center(60, '-'))

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
