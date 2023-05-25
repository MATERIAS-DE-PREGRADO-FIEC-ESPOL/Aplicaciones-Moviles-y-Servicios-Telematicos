---
remote_theme: pages-themes/cayman@v0.2.0
---
[Regresar](/Aplicaciones-Moviles-y-Servicios-Telematicos/)

# Práctica de laboratorio 1
# DESARROLLO DE UNA APLICACIÓN MÓVIL USANDO CONTROLES AVANZADOS

## 🎯 Objetivo de Aprendizaje
Desarrollar aplicaciones móviles considerando las características de la programación en dispositivos móviles.
**Recursos:** Android Studio, GIT (software), GitHub (online).
**Duración:** 5 horas

**Instrucciones**
Desarrolle un aplicativo móvil usando componentes avanzados como menú, y cargue el código fuente en un repositorio de GitHub.

**Actividades**

Nota: Solo un integrante por grupo realiza las actividades del paso 1 al 3.

Paso 1: Crear un nuevo proyecto en Android Studio. (2 puntos)

1.	Al abrir Android Studio, podemos crear, abrir o importar proyectos. Seleccione “New Project”.

<p align="center">
  <img src="../imagenes/amst_lab1_newproject.png" alt="newproyect" width="90%">
</p>

2.	Seleccionar el tipo de proyecto: Para esta práctica escogeremos la pestaña **Phone and Tablet > Empty Activity.** Otro tipo de actividades viene por defecto con componentes no necesarios para este taller.

<p align="center">
  <img src="../imagenes/amst_lab1_emptyactivity.png" alt="emptyactivity" width="90%">
</p>

3.	Configuración inicial del proyecto.

a -	[Name]: Colocaremos el nombre de nuestra app. (Recuerde que este nombre será reflejado en el PlayStore al momento de publicarlo). Para este taller, usaremos appAMST[númeroGrupo]. 

b.	[PackageName]: Paquete principal de código java, se obtiene automáticamente del nombre.

c.	[Save Location]: Dirección donde se ubica el proyecto en nuestra PC

d.	[Language]: Java

e.	[Minimum SDK]: Escoger el primero que aparece en la lista. (API 16: Android 4.1)

f.	Marcar la opción Use legacy Android.support libraries.

4.	Seleccionamos Finish.

<p align="center">
  <img src="../imagenes/amst_lab1_appAMST0.png" alt="appAMST" width="90%">
</p>

(*) Como resultado se creará un proyecto, el cual solo presenta el mensaje “Hello World”.



5.	Seleccione en la ruta app > res > layout > activity_main.xml.

6.	En la parte superior seleccione la pestaña “Design” para comenzar a diseñar la interfaz de usuario de la aplicación usando controles personalizados.

7. En la pestaña de Design encontrará la “Palette” que contiene los controles para agregar a la aplicación, si conoce el nombre del control puede iniciar una búsqueda.


8.	Crear la interfaz de usuario con: 2 cuadros de texto (Plain Text), uno para el nombre del usuario y otro para la clave del usuario; y 2 botones (Button), uno para logearse y otro para registrarse como nuevo usuario.

9. Para visualizar el código en formato xml en la ruta app > res > layout > activity_main.xml, en la parte superior seleccione la pestaña de Code. En caso de no completar el paso 7, puede agregar el siguiente código para reemplazar:

**Archivo: activity_main.xml**

10.	Seleccionar la ruta app > java> com.example.mediconline > MainActivity.java donde se programa las funcionalidades de la aplicación en lenguaje Java.

**Archivo: MainActivity.java**

11.	Dar clic derecho en la ruta app > java y seleccione New > Activity > Empty Activity para crear una nueva actividad con el nombre de formulario_registro. Con esto se crearán dos archivos:
	formulario_registro.java
	activity_formulario_registro.xml



