---
remote_theme: pages-themes/leap-day@v0.2.0
plugins:
- jekyll-remote-theme
---
[Regresar](/Aplicaciones-Moviles-y-Servicios-Telematicos/)

# Práctica de Laboratorio 2
## DESARROLLO DE UNA APLICACIÓN MÓVIL CON INTEGRACIÓN DE BASE DE DATOS EXTERNA EN GOOGLE

## 🎯 Objetivo de Aprendizaje
Demostrar el acceso a los recursos en red para la programación de aplicaciones móviles avanzadas.

**Recursos:**
Android Studio, Google Cloud, FireBase.

**Duración:**
 7 horas


**Instrucciones**
- Crear una aplicación móvil que interactúe con una base de datos no relacional durante el desarrollo de la aplicación móvil.

**Actividades**

### **Paso 1:** Integra el servicio de FireBase a tu aplicación de Android Studio. (15 puntos)

1.	Crea un proyecto en Android Studio nombrado ***appAMST_labA_firebase*** donde A será el número de laboratorio.

-	Asegúrese de que su Minimum API level sea API 16 (Jelly Bean) o mayor.

-	Para este curso, el lenguaje a utilizar será JAVA.

-	No marcar “Use legacy android.support libraries”.


<p align="center">
  <img src="../imagenes/amst_lab2_newproject.png" alt="appAMST" width="100%">
</p>

2.	Acceder a la [consola de FireBase](https://console.firebase.google.com/) usando una cuenta de gmail o de FIEC. Luego selecciona ***Crear un nuevo proyecto*** en que se mostrará el siguiente proceso.

<p align="center">
  <img src="../imagenes/amst_lab2_firebase_new_project.png" alt="appAMST" width="100%">
</p>

<p align="center">
  <img src="../imagenes/amst_lab2_google_analytics.png" alt="appAMST" width="100%">
</p>

<p align="center">
  <img src="../imagenes/amst_lab2_googleanalytics_account.png" alt="appAMST" width="100%">
</p>

<p align="center">
  <img src="../imagenes/amst_lab2_readyproject.png" alt="appAMST" width="100%">
</p>

3.	Dentro del proyecto de FireBase creado recientemente, añadimos nuestra aplicación de Android en la consola, dando clic al icono de Android Studio.  

<p align="center">
  <img src="../imagenes/amst_lab2_appandroid.png" alt="appAMST" width="100%">
</p>

***En caso de que ya existan proyectos en el repositorio de Firebase, hacer clic en el siguiente botón de Agregar app:***

<p align="center">
  <img src="../imagenes/amst_lab2_menu_addapp.png" alt="appAMST" width="50%">
</p>

4.	Para completar los datos de la sección de Añadir Firebase a tu aplicación de Android, en Android Studio puedes encontrar el nombre del paquete de Android en el archivo de **build.gradde (module:app)** en la variable applicationId.

```
android {
    namespace 'com.example.appamst_laba_firebase'
    compileSdk 33

    defaultConfig {
        applicationId "com.example.appamst_laba_firebase"
        minSdk 16
        targetSdk 33
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
}
```

5.	En app > manifests > AndroidManifest.xml dar permisos de acceso a Internet:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <uses-permission android:name="android.permission.INTERNET" />
```

6. Para obtener el certificado de firma de depuración SHA-1 de Android Studio, debemos acceder a la ruta de File -> Settings -> Experimental. Luego, desmarcar la opción ***Only include test tasks in the Gradle task list generated during Gradle Sync***

<p align="center">
  <img src="../imagenes/amst_lab2_certificado_firma.png" alt="appAMST" width="100%">
</p>

7. Ahora para actualizar el proyecto, selecciona Files -> Sync Project with Gradle Files.

<p align="center">
  <img src="../imagenes/amst_lab2_syncproject.png" alt="appAMST" width="80%">
</p>

8.	Luego, ubicar la pestaña Gradle que se encuentra en la esquina superior derecha de la ventana, seleccionar la ruta Gradle -> app -> Tasks -> android -> signingReport, donde se encuentra el certificado de firma de depuración SHA-1.

<p align="center">
  <img src="../imagenes/amst_lab2_sha1.png" alt="appAMST" width="100%">
</p>

9.	Ahora si puede completar todos los datos (nombre del paquete, apodo, y el certificado de firma SHA-1 de depuración) en la consola de Firebase, ventana de Agrega Firebase a tú aplicación Android.

- Apodo: Es un identificador interno y conveniente que solo tú puedes ver en Firebase console.

- Certificado de firma SHA‑1 de depuración: Firebase Authentication.

- Importante: Para la autenticación, requiere agregar el certificado de firma SHA‑1 de depuración.


<p align="center">
  <img src="../imagenes/amst_lab2_addfirebasetoandroid.png" alt="appAMST" width="100%">
</p>

10.	Descargamos el archivo de configuración “Google-services.json”.

11.	En Android Studio cambiamos a la vista Proyecto y agregamos el archivo dentro de la carpeta app de nuestro proyecto, tal como se muestra en la imagen.

<p align="center">
  <img src="../imagenes/amst_lab2_googleservices.png" alt="appAMST" width="80%">
</p>


12.	Para que los SDK de Firebase puedan acceder a los valores de configuración de google-services.json, necesitas el complemento Gradle de los servicios de Google. Agrega el complemento como una dependencia buildscript a tu archivo build.gradle de nivel de proyecto. Luego, en el archivo build.gradle del módulo (nivel de app) agrega los complementos google-services y cualquier SDK de Firebase que quieras usar en tu app:

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>


Siempre que realices cambios en los archivos Gradle, recuerda volver a sincronizar tu proyecto para asegurarte el correcto funcionamiento de las nuevas librerías. Puedes dar clic en Sync Now en la parte superior derecha de la pantalla o dar clic en File > Sync Project with gradle files.


13.	Listo, ahora está sincronizado el proyecto y se puede ir a la consola.

<p align="center">
  <img src="../imagenes/amst_lab2_readygoogle.png" alt="appAMST" width="100%">
</p>

### **Paso 2:** Inicio de sesión con cuenta Google (10 puntos)

**Pre-requisito:** Habilitar el método de inicio de sesión mediante Google. Dentro de la consola del proyecto en FireBase seleccione del lado izquierdo la ruta de Build -> Authentication. Luego se mostrará el menú de Users, dar clic en el botón de Set up sign-in method y entre los proveedores adicionales habilitar ***Google***. 

<p align="center">
  <img src="../imagenes/amst_lab2_console_autenticacion.png" alt="appAMST" width="100%">
</p>

<p align="center">
  <img src="../imagenes/amst_lab2_console_proveedor.png" alt="appAMST" width="100%">
</p>

1.	Agregamos nuevas dependencias en build.gradle (module:app), y luego sincronizamos.

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

2.	Creamos una vista de inicio. Dentro de app/res/layout/activity_main.xml diseñamos la primera vista de la aplicación. Para esta vista agregaremos: ImageView, TextView, Button. Dentro de un Linear Layout.  

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

**Código de la vista**
Los componentes subrayados son aquellos que aún no han sido creados. Por eso debe agregar una imagen llamada google.png en src/main/res/drawable.

### **Paso 3:** Configurar Inicio de sesión (15 puntos)


1.	Agregamos las siguientes variables públicas a MainActivity.java (Importar las librerías que sean necesarias)




2.	En la función onCreate (Función que se ejecuta al momento de iniciar la acción), instanciamos la configuración de inicio de Google y firebase.







Nota: default_web_client_id puede llegar a mantenerse en error hasta compilar por primera vez el programa.

3.	Creamos la función pública de iniciar sesión dentro de la clase publica MainActivity. Dentro de esta función llamaremos al inicio de sesión por Google. (Importar las librerías que sean necesarias)



4.	Implementamos la función (sobrescrita) onActivityResult dentro de la clase publica MainActivity, que se ejecutara después verificar sesión. Obtendremos la información de sesión o mostraremos un error en el Log si el inicio de sesión ha fallado.




5.	Autenticamos sesión con Firebase (para acceder a la base de datos). Para ello usamos las credenciales de Google.




6.	Obtenemos el usuario de Firebase. Podemos obtener el nombre, email y foto a partir de la cuenta, lo que se usará en los siguientes pasos.


### **Paso 4:** Creación de perfil de usuario (15 puntos)

Ahora mostraremos la información de un del usuario en una nueva actividad e implementar.

1.	Creamos una nueva Actividad. Damos clic derecho en /app > New > Activity > Empty Activity.

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

2.	Asignamos un nombre a la Actividad como “PerfilUsuario”, y damos clic en finish. 

3.	En MainActivity.java, modificamos la función updateUI() agregando un Intent para empezar la nueva actividad y pasando la información del usuario. 


4.	En app/res/layout/activity_perfil_usuario.xml, diseñamos la vista para el perfil de usuario donde colocaremos la información que del cliente.

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

**Código**

5.	Para poder visualizar la imagen de perfil, agregamos la dependencia Picasso, en build.gradle(module:app)


6.	En app/java/PerfilUsuario.java, vamos a obtener la información del usuario y presentarla en la pantalla que se diseño:

En caso de problemas con el método with() usar get().

7.	Implementamos la función CerrarSesion para desvincular nuestra cuenta con la aplicación.


8.	Modificamos el MainActivity.java para borrar los datos de la sesión de Google.


### **Paso 5:** Implementar Base de datos (25 puntos)


Vamos a implementar una base de datos para guardar tweets de un usuario específico. 

1.	Agregamos la dependencia de base de datos

2.	Este paso es totalmente informativo, para la práctica seguirán al paso 3. Estructuraremos la base de datos. (Una base NO RELACIONAL, estructura de árbol). Para ello accedemos a: Firebase > Compilación > Realtime Database 

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

Nos ubicamos en Grupo y damos clic en [+] para agregar un nodo (child).
Nombre: Grupo	Valor: Vacio, damos click en [+] para agregar otro nodo

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

	
Se crea el siguiente árbol de estructura:

<p align="center">
  <img src="../imagenes/amst_lab2_.png" alt="appAMST" width="100%">
</p>

Así fue creado un árbol de estructura de forma gráfica. En los siguientes pasos se mostrará como hacerlo desde la aplicación.

3.	Declaramos la variable pública de referencia a la base de datos en la clase PerfilUsuario.java.

4.	Iniciamos la variable de la base de datos y ejecutamos las funciones de prueba dentro de la funcion onCreate.

5.	Implementamos las funciones IniciarBaseDeDatos, leerTweets (obteniendo datos de la base), publicar tweets (escribir en la base de datos). 
**Nota:** Modificar el nombre del grupo según corresponda.





### **Investigación:**
- ¿Cuáles son los beneficios de utilizar bases de datos no relacionales en aplicaciones móviles?
- ¿Qué funciones realiza la librería PICASSO?
- ¿Qué funciones realiza el build.gradle(app:module)?
- ¿Qué servicios ofrece FireBase?
- ¿Qué limitaciones tiene FireBase con respecto a la escabilidad en dispositivos móviles?

### **Desafíos (20 puntos)**:

- Mejorar el perfil de usuario del cliente. Investigar y mostrar toda la información disponible desde su cuenta de Gmail (como teléfono, bibliografía, etc).
- Agregar en la pantalla de inicio de sesión, otro proveedor de autenticación como Facebook o Twitter.
- Modifique la aplicación para que los tweets y la fecha sean ingresados por el usuario.
- Realizar un tweet por integrante en la rama designada en Firebase.
- Aplicar opciones de seguridad gratuitas ofrecidas por Google Cloud.

### **Formato del Trabajo**

La práctica de laboratorio será desarrollada en el siguiente formato:

- Nombre del archivo: AMST_LabA_Grupo B_Apellido1_Apellido2_Apellido3
- (*) Siendo A el número del trabajo y B el número del grupo
- Nombre de la materia y paralelo 1
- Título del trabajo: Ejemplo: Laboratorio A - Tema
- Nombre de la profesora
- Número de grupo
- Nombres/Apellidos de los integrantes del grupo que hayan desarrollado el trabajo
- Fecha de inicio y fin del trabajo
- Resultados de las actividades planteadas: Explicación de las actividades ejecutadas, incluyendo las imágenes del proceso. Colocar el enlace del repositorio de GitHub con su código fuente.
- Conclusiones y Recomendaciones: Respecto a lo aprendido durante el desarrollo del trabajo.
- Referencias bibliográficas: Colocar los documentos, enlaces web o libros consultados
