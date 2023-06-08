# Práctica de Laboratorio 05

**Objetivo de Aprendizaje:** Desarrollar aplicaciones móviles híbridas sencillas considerando las características de la programación de dispositivos móviles.
**Recursos:** Android Studio
++Duración:** 10 horas


## Introducción:

Flutter es un conjunto de herramientas de interfaz de usuario multiplataforma que está diseñado para permitir la reutilización de código en sistemas operativos como iOS y Android, al mismo tiempo que permite que las aplicaciones interactúen directamente con los servicios de la plataforma subyacente. El objetivo es permitir que los desarrolladores entreguen aplicaciones de alto rendimiento que se sientan naturales en diferentes plataformas, adoptando las diferencias donde existen mientras comparten la mayor cantidad de código posible.

**Beneficios de Flutter**

•	Alta productividad al ser multiplataforma

•	Desarrollo rápido y sencillo 

•	Compatibilidad

•	De código abierto

**Desventajas de Flutter**

•	Las aplicaciones creadas con Flutter tienden a ser pesadas.

•	Pocas librerías de terceros 
Limitaciones de Flutter

•	Flutter está usando un lenguaje de programación llamado Dart. 

•	Complejidad limitada

### **Actividades:**

**Paso 1: Instalar Flutter**
Requerimientos
Antes de continuar hay que tener en cuenta los siguientes requerimientos para instalar Flutter.

**Hardware**

En primera instancia se recomienda un sistema con:
•	Mínimo 8gb de ram.
•	Espacio libre en disco: 6 gb mínimo.
•	*Si posee tarjeta de video mucho mejor debido a que el emulador del dispositivo Android consume muchos recursos.

**Software**
Windows:
•	Windows 7 SP1 o posterior (64 bits), x86-64 
•	Windows Powershell 5.0 o posterior. (Preinstalado en Windows 10)
•	Git for Windows 2.x (Debe permitir ejecutar comandos “git” en el command promt o powershell)

**MacOS:**
•	MacOS (64-bit)
•	Xcode (Incluye git, aunque puede ser instalado por separado)

**Linux:**
•	Linux (64-bit)

1.	Descargar el archivo SDK en su última versión estable en el siguiente enlace, ahí podrán encontrar los diferentes archivos para cada tipo de sistema operativo.:
- 	https://flutter.dev/docs/development/tools/sdk/releases
2.	Extraemos el archivo zip.
- En Windows podemos dar click derecho al archivo y damos en extraer todo.
- En MacOS podemos dar click derecho al archivo y dar click en abrir, con esto de descomprimirá el archivo.
- La carpeta extraída la alojamos en la siguiente localización. (En caso de no existir el directorio, crearlo).
- En Windows: - \Users\<tu-nombre-de-usuario>\Documents.
- En Mac: <Disco Principal>/Users/<tu-nombre-de-usuario>/development
4.	Debemos agregar el path a las variables del sistema:
- Windows
- En el inicio buscamos panel de control y lo abrimos.
- la parte derecha superior seleccionamos Ver por: “Iconos grandes”
- Luego damos click en Sistema.

- Dependiendo de la versión de Windows puede que se mantenga en el mismo panel de control o se inicie una nueva ventana de configuración.

- En esta nueva ventana buscaremos “Configuración avanzada del sistema”, si se mantuvo en el panel de control aparecerá en un panel izquierda. En el otro caso de que se haya abierto la ventana de configuración esta opción está en el panel derecho.

- Se abrirá la ventana de Propiedades del sistema, ahí daremos click en variables de entorno.

- En el cuadro inferior de “Variables del sistema” buscaremos la variable llamada “Path” y le daremos doble click.

- Se abrirá una nueva ventana, ahí presionaremos en el botón nuevo.
- Escribiremos la ruta donde se alojó la carpeta de flutter. Ejemplo: C:\Users\<tu-nombre-de-usuario>\Documents\flutter\bin
- Daremos en aceptar en las ventanas hasta cerrarlas todas.
- MacOS.
- Abriremos una terminal.
- Nos dirigiremos al directorio del usuario con el comando: cd /Users/<tu-nombre-de-usuario>
- Una vez dentro, realizaremos el comando vim .bash_profile
- Presionamos la tecla i para empezar a editar el archivo creado.
- Escribiremos: export PATH=”$PATH:/Users/<tu-nombre-de-usuario>/development/flutter/bin” (el path agregado debe coincidir con el path donde se encuentra la carpeta de flutter alojada.)
- Para salir de vim escribiremos “:wq!”
- Cerramos y volvemos a abrir la terminal.

