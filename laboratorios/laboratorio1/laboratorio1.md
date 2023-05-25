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

2.	Seleccionar el tipo de proyecto: Para esta práctica escogeremos la pestaña Phone and Tablet > Empty Activity. Otro tipo de actividades viene por defecto con componentes no necesarios para este taller.

<p align="center">
  <img src="../imagenes/amst_lab1_emptyactivity.png" alt="emptyactivity" width="90%">
</p>

3.	Configuración inicial del proyecto.
a.	[Name]: Colocaremos el nombre de nuestra app. (Recuerde que este nombre será reflejado en el PlayStore al momento de publicarlo). Para este taller, usaremos appAMST[númeroGrupo]. 
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

Paso 2: Crear un repositorio (30 puntos).

1.	Dentro de la carpeta del proyecto creado en el paso anterior, abra la línea de comandos de GIT (GIT CLI). Podemos encontrarlo dando clic derecho en la carpeta y escogiendo la opción “GIT BASH HERE”.


