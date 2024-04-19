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
- Configuracion
- Uso
- Contribucion
- Roadmap

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

##Configuracion

Configura el servidor web como Nginx o Apache para que actúe como un proxy que pueda manejar HTTPS, redireccionamiento, balanceo de carga, y servir contenido estático.

Crear la base de datos AbarrotesDM

Copia los archivos de la aplicación al servidor o clona el repositorio de código fuente en el servidor de desarrollo.

Configura variables de entorno necesarias para la producción, como cadenas de conexión a bases de datos.











