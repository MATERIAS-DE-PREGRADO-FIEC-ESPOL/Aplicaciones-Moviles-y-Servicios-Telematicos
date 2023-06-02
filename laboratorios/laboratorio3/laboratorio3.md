---
remote_theme: pages-themes/leap-day@v0.2.0
plugins:
- jekyll-remote-theme
---
[Regresar](/Aplicaciones-Moviles-y-Servicios-Telematicos/)

# Prácticas de laboratorio 3

### **Objetivo de Aprendizaje:**
Desarrollar aplicaciones móviles sencillas considerando las características de la programación de dispositivos móviles.
### **Recursos:**
Android Studio, REST API del curso, REST API privada, bases de datos PostgreSQL usando formato JSON.
### **Duración:**
8 horas

## Instruciones:

Crear una aplicación que interactúe con 3 tipos de base de datos utilizadas actualmente durante el desarrollo de aplicaciones móviles:
1.	Base de datos externa PostgreSQL para el inicio de sesión y la consulta de datos
2.	Uso de token de autorización
3.	Base de datos privadas con REST APIs disponibles para desarrollo.
Para lograr la integración de aplicaciones móviles con bases de datos externas y privadas utilizando REST API y autorización de seguridad mediante web tokens.

## Actividades:

**Paso 1: Crear un nuevo proyecto en Android Studio**

1.	Al abrir Android Studio seleccione **“New project”.**

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

2.	Seleccionar el tipo de proyecto: Para esta práctica escogeremos la pestaña Phone and Tablet **> Empty Activity**. 
**Nota:** Otro tipo de actividades viene por defecto con componentes no necesarios para este taller.

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

3.	Configuración inicial del proyecto.

- [Name]: Colocaremos el nombre de nuestra app. (Recuerde que este nombre será reflejado en el PlayStore al momento de publicarlo). Para este laboratorio, usaremos **amst_labA_appapi** donde A es el número de la práctica de laboratorio.
- [PackageName]: Paquete principal de código java, se obtiene automáticamente del nombre.
- [Save Location]: DirecciÓn donde se ubica el proyecto en nuestra PC.
- [Languaje]: jav
<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

4.	Seleccionamos FINISH. Como resultado se creará un proyecto vacío, solo presentado el mensaje “Hello World”.

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

**Paso 2: Crear interfaz de usuario**

Para esta aplicación crearemos una interfaz de usuario de inicio de sesión y un menú principal. Al momento de abrir la aplicación, se ejecutará MainActivity.java y activity_main.xml

1.	Dentro del archivo activity_main.xml que se encuentra en la ruta app > res > layout, vamos a colocar los siguientes elementos:
- (1 Layout vertical) para el arreglo de los elementos
- (1 EditText) un titulo
- (2 Inputs) Ingresar usuario y contraseña
- (1 button) Botón de ingreso

**Vista de inicio de sesión:** 


<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

### Preguntas de desafío:
- ¿Qué atributo me permitiría cambiar el tipo de letra de mi ventana? (Escriba la línea de código que usaría).
- ¿Que hace el atributo type? (mencione otros 5 valores que puede tener el atributo type diferentes al que se usa en el código).

2.	Crear una segunda actividad a mi aplicación para redirigir al usuario cuando este ha completado con éxito el inicio de sesión.
- Para crear una nueva actividad, damos clic derecho en “app”.
- Seleccionar New > Activity > Empty Activity.


<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>


- Ingresamos un el nombre para la nueva actividad [menu], lo que generara dos archivos:
i.	Menu.java
ii.	Menu.xml

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>


3.	Creamos un menú básico (15 minutos):
- (1 Layout vertical) para el arreglo de los elementos
- (1 EditText) un título
- (4 Botones) un título


<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

4.	Creamos una transición de una actividad a otra para (De inicio de sesión -> Menú principal)
- Seleccionamos el botón de Iniciar sesion > atributo(onClick) (dentro de activity_main.xml)
- Escribirnos el nombre de la función irMenuPrincipal
- Creamos la función irMenuPrincipal dentro de MainActivity.java

**Paso 3: Inicio de sesión con Base de datos externa (REST API).**

Una REST API o API de desarrollo permite interactuar con una base de datos externa por medio de llamados HTTP, devolviendo información en formato Json


<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

La REST API que usaremos para este taller será https://amst-lab-api.herokuapp.com/db. Esta API está desarrollada en Django Python con autenticación JWT.  De esta manera, el teléfono puede acceder a grandes cantidades de información sin tener que alojarla de forma interna. A cambio requiere conexión a internet (lo cual en casos puede llegar a ser costosa).

1.	Dar permisos para el uso de internet. Nuestra aplicación debe permitir conectarse a internet por medio del teléfono. Para ello, agregamos la siguiente línea en el archivo manifesto (El archivo de configuraciones generales)
- El archivo se encuentra en app > manifests > AndroidManifest.xml
- Agregamos la siguiente línea (para conceder permisos de Internet): 


2.	Instalamos las dependencias necesarias (Librería Volley para request http).
- Agregamos la librería Volley en el archivo build.gradle que se encuentra en “Gradle Scripts” - build.gradle (modulo app).
- Agregamos la siguiente línea: 

a)	Una vez ingresada se actualizará el Gradle (Paquete de librerías) [En caso de no sincronizarse puede sincronizarlo manualmente con File > Sync Project with Grandle files].

**Paso 4: Inicio de sesión con Base de datos externa (REST API).**

Creamos la función Iniciar sesión en MainActivity.java
Ahora creamos la función que va a recibir como parámentros nuestro usuario y contraseña y retornará el token de seguridad o el mensaje de que el usuario no es válido.

1.	Creamos una variable lista (queue) de las solicitudes (request) a ejecutar.

2.	Debe crearse un usuario, accediendo al portal 


Usuario: estudiante, contraseña:stud3ntam5t

Cree un usuario, y esas serán las credenciales que usará para su aplicación (tabla Users > +Add).

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

Al hacer click en guardar el usuario estará creado. Aparecerá otro formulario. Modificar solamente los campos a continuación:

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

Dirigirse al final y aplastar el botón SAVE  


3.	Creamos la función IniciarSesion(). Para realizar la siguiente llamada HTTP:
Url: https://amst-lab-api.herokuapp.com/api/db/nuevo-jwt
Método: POST
Cuerpo: {username, password}
Retorno: {token de usuario}


MainActivity.java





Nota: Realice la importación de las librerías que sean necesarias.




Obtenemos el token en el menú

Archivo: Menu.java



**redes_sensores.java**
Creamos una nueva actividad, dando clic derecho en app > Activity > Empty Activity.
Ingresamos un el nombre para la nueva actividad [RedSensores], lo que generara dos archivos:
a.	RedSensores.java
b.	red_sensores.xml

Utilizaremos imágenes para indicar los diferentes sensores. Puede utilizar imágenes de internet: Formato png menos a 500mb. Estas imágenes deben ser agregadas al siguiente directorio: app >  res > drawable

**RedSensores.java**



Nota: Realice la importación de las librerías que sean necesarias.


Actividad de redes de sensores (XML)


**Diseño de la aplicación móvil de sensado de temperatura, humedad y peso.**


Preguntas de desafío:
c)	¿Qué son los métodos POST y GET?
d)	¿Qué otros métodos como esos existen?
e)	¿Qué es Django y para qué sirve?

Tareas de Desafío:
1.	Realizar una actividad que me permita enviar nuevos valores de humedad, peso y temperatura a la base de datos actual. Pista: Utilice el método POST como en el inicio de sesión, pero en vez de crear el token, enviar los parámetros de los nuevos valores y la función getHeaders del método get usado. 
2.	Usar la ruta: https://amst-lab-api.herokuapp.com/api/sensores/




## FORMATO DEL TRABAJO

El trabajo autónomo será desarrollado en el siguiente formato:

- Nombre del archivo: AMST_Trabajo Autónomo A_Grupo B_Apellido1_Apellido2_Apellido3…
- (*) Siendo A el número del trabajo y B el número del grupo
- Nombre de la materia y paralelo 1
- Título del trabajo: Ejemplo: Trabajo Autónomo A - Tema
- Nombre de la profesora
- Número de grupo
- Nombres/Apellidos de los integrantes del grupo que hayan desarrollado el trabajo
- Fecha de inicio y fin del trabajo
- Resultados de las actividades planteadas: Explicación de las actividades ejecutadas, incluyendo las imágenes del proceso. Además, incluir el enlace de su repositorio de github para la revisión del código fuente y el archivo ejecutable del app (*.apk).
- Conclusiones y Recomendaciones: Respecto a lo aprendido durante el desarrollo del trabajo.
- Referencias bibliográficas: Colocar los documentos, enlaces web o libros consultados.
