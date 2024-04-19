 x  # Descripción, problema identificado, solución, arquitectura

## Descripcion.

##### El proyecto consiste en un sistema de automatizacion de inventarios, y punto de venta para una pequeña tienda de abarrotes en la que cuentan con un sistema que solo les muestra el precio, pero no interactua con el inventario, no resta los produdctos vendidos y no permite realizar cobros, esto ultimo lo realizan de forma manual, el sistema de gestion de inventarios y ventas les permitira agilizar la operacion tanto al momento de la venta como al realizar inventarios, se configurara una base de datos en SQLite, y se realizara una interfaz intuitiva con botones de Venta, Cobrar, Cancelar, opcion de cobrar multipes veces un producto sin necesidad de escanearlo tantas veces.

## Problemas

##### La tienda ha tenido perdidas por cobrar mal, han negado productos derivada de un mal inventario pues no contemplan la demanda real o al contrario han tenido perdidas por productos caducados.

## Solucion

##### Implementar el sistema de gestion de inventarios y ventas el cual permitira el registro de ventas cobros incluyendo opciones para diferentes metodos de pago e inventarios.

## Arquitectura

##### Interfaz de usuario esta aun no se desarrolla por el tiempo pero se espera implementarla en el futuro para que los usuarios tengan a su disposicion las herramientas y ventajas que este sistema pretende darles.

##### Base de datos se utilizara SQLite para procesar los datos de transacciones e invenetarios.

##### Hardware necesario como pc de reciente modelo, impresora de recibos, cajones de dinero, lector de codigo de barras y terminal bancaria.

## Tabla de contenidos
- [Requerimientos](https://github.com/erckvan/Taller-productividad-ErickMedina/tree/develop?tab=readme-ov-file#requerimientos)
- [Instalacion](https://github.com/erckvan/Taller-productividad-ErickMedina/tree/develop?tab=readme-ov-file#instalacion)
- [Configuracion](https://github.com/erckvan/Taller-productividad-ErickMedina/blob/develop/README.md#configuracion) 
- [Uso](https://github.com/erckvan/Taller-productividad-ErickMedina/blob/develop/README.md#uso)
- [Contribucion]
- [Roadmap]

# Requerimientos

##### Se utilizara un servidor Gunicorn, se utilizara el framework Flask con el paquete flask-login y flask-wtf para desarrollar el sistema y la interfaz de usuario, y la base de datos SQLite para procesar los datos de las ventas e inventarios y la interaccion en tiempo real de ambas.

# Instalacion

##### Instalas Python, si aun no lo tienes descargalo e instalalo desde el sitio web oficial de Python [Python Downloads](https://www.python.org/downloads/) 
crea un entorno virtual 

python -m venv venv

Activa el entorno virtual

venv\Scripts\activate

Instalar Flask y Gunicorn

pip install Flas gunicorn

Asegúrate de que el servidor local tenga todas las dependencias del sistema necesarias instaladas, como Python, y el servidor de bases de datos SQLite

## Configuracion

Configura el servidor web como Nginx o Apache para que actúe como un proxy que pueda manejar HTTPS, redireccionamiento, balanceo de carga, y servir contenido estático.

Crear la base de datos AbarrotesDM

Copia los archivos de la aplicación al servidor o clona el repositorio de código fuente en el servidor de desarrollo.

Configura variables de entorno necesarias para la producción, como cadenas de conexión a bases de datos.

## Uso

Manual de usuario 

- Inicio de sesion y navegacion basica
  * Como acceder al sistema
  * Vista general de la interfaz del usuario (Cuando este desarrollada)
  * Descripcion de las principales areas de la aplicacion.

- Gestion de inventarios
  * Como ver el inventario existente
  * Instrucciones para modificar el inventario.
  * Instrucciones para modificar o eliminar productos existentes
  * Cómo realizar búsquedas y filtrar datos en el inventario

- Procesamiento de ventas
  * Cómo ingresar una nueva venta
  * Descripción de cómo agregar productos a una orden de venta
  * Explicación de los métodos de pago disponibles
  * Cómo finalizar una venta y generar recibos

Manuel de usuario administrador

- Requisitos del sistema
  * Especificaciones técnicas completas, incluyendo requisitos del servidor

- Configuracion inicial
  * Cómo instalar y configurar el sistema por primera vez
  * Configuración de parámetros esenciales como configuración de la base de datos

- Administracion de usuarios
  * Cómo crear y gestionar cuentas de usuario
  * Asignación de roles y permisos a los usuarios

- Gestión Avanzada de Inventarios
  * Procedimientos para ajustes de inventario masivos
  * Configuración de alertas de inventario (por ejemplo, notificaciones de bajo stock)

- Gestión de Datos
  * Procedimientos para la importación y exportación de datos
  * Cómo realizar copias de seguridad y restauración de datos

## Contribución











