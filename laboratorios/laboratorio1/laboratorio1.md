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

- [Name]: Colocaremos el nombre de nuestra app. (Recuerde que este nombre será reflejado en el PlayStore al momento de publicarlo). Para este taller, usaremos appAMST[númeroGrupo]. 

-	[PackageName]: Paquete principal de código java, se obtiene automáticamente del nombre.

-	[Save Location]: Dirección donde se ubica el proyecto en nuestra PC

-	[Language]: Java

- [Minimum SDK]: Escoger el primero que aparece en la lista. (API 16: Android 4.1)

4.	Seleccionamos Finish.

<p align="center">
  <img src="../imagenes/amst_lab1_appAMST0.png" alt="appAMST" width="90%">
</p>

(*) Como resultado se creará un proyecto, el cual solo presenta el mensaje “Hello World”.

5.	Seleccione en la ruta app > res > layout > activity_main.xml.

6.	En la parte superior seleccione la pestaña “Design” para comenzar a diseñar la interfaz de usuario de la aplicación usando controles personalizados.

<p align="center">
  <img src="../imagenes/amst_lab1_emptylayout.png" alt="appAMST" width="90%">
</p>


7. En la pestaña de Design encontrará la “Palette” que contiene los controles para agregar a la aplicación, si conoce el nombre del control puede iniciar una búsqueda.

<p align="center">
  <img src="../imagenes/amst_lab1_palette.png" alt="appAMST" width="30%">
</p>


8.	Crear la interfaz de usuario con: 2 cuadros de texto (Plain Text), uno para el nombre del usuario y otro para la clave del usuario; y 2 botones (Button), uno para logearse y otro para registrarse como nuevo usuario.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>


9. Para visualizar el código en formato xml en la ruta app > res > layout > activity_main.xml, en la parte superior seleccione la pestaña de Code. En caso de no completar el paso 7, puede agregar el siguiente código para reemplazar:

**Archivo: activity_main.xml**
```
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity"
    tools:ignore="MissingConstraints">

    <LinearLayout
        android:orientation="vertical"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:padding="20dip"
        tools:ignore="MissingConstraints">

        <EditText
            android:id="@+id/edtUsuario"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:hint="Usuario" />

        <EditText
            android:id="@+id/edtClave"
            android:layout_width="fill_parent"
            android:layout_height="wrap_content"
            android:hint="Clave" />

        <Button
            android:id="@+id/btnLogin"
            android:layout_height="wrap_content"
            android:layout_width="wrap_content"
            android:text="Login"
            android:layout_gravity="center_horizontal"
            android:paddingLeft="15dip"
            android:paddingRight="15dip"
            android:onClick="login"/>

        <Button
            android:id="@+id/btnRegistro"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:onClick="registrarse"
            android:paddingLeft="15dip"
            android:paddingRight="15dip"
            android:text="Registrarse" />

    </LinearLayout>

</androidx.constraintlayout.widget.ConstraintLayout>
```

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

10.	Seleccionar la ruta app > java> com.example.mediconline > MainActivity.java donde se programa las funcionalidades de la aplicación en lenguaje Java.

**Archivo: MainActivity.java**

```
package com.example.appamst0;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText edtUsuario, edtClave;
    private Button btnLogin, btnRegistro;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Referencias a los controles del diseño
        edtUsuario = (EditText) findViewById(R.id.edtUsuario);
        edtClave = (EditText) findViewById(R.id.edtClave);

        btnLogin = (Button) findViewById(R.id.btnLogin);
        btnRegistro = (Button) findViewById(R.id.btnRegistro);
    }

    public void registrarse(View view) {
        Intent intent = new Intent(this, formulario_registro.class);
        startActivity(intent);
    }

    public void login(View view) {
        Toast toast=Toast.makeText(getApplicationContext(),"Usted no cuenta con un usuario",Toast.LENGTH_SHORT);

        toast.show();
    }

    public void onClick(View v) {
        if(v.getId() == R.id.btnLogin){
            Log.d("mensaje","ïngreso");

        }else if(v.getId() == R.id.btnRegistro) {
        }
    }
}
```


<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

11.	Dar clic derecho en la ruta app > java y seleccione New > Activity > Empty Activity para crear una nueva actividad con el nombre de formulario_registro. Con esto se crearán dos archivos:
+	formulario_registro.java
+	activity_formulario_registro.xml

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>


12.	Modifique el archivo formulario_registro.java para poder enviar la notificación de registro.

**Archivo: formulario_registro.java**

13. En la ruta res > layout seleccione el archivo activity_formulario_registro.xml registro en la pestaña “Text” que contiene el código xml del formulario de registro para los nuevos usuarios que deseen utilizar la aplicación.

**Archivo: activity_formulario_registro.xml**

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

### Paso 2: Ejecución de la aplicación móvil. (30 puntos)

14.	Ejecutar el aplicativo móvil “mediconline” seleccionando el device selecter al lado de la opción Run ‘app’, en la cual se puede escoger entre 2 opciones: el dispositivo móvil conectado a través del cable USB de datos, o el emulador que usa los dispositivos virtuales disponibles.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

15.	Para la primera opción de ejecución de la aplicación se usa un teléfono móvil conectado vía USB a la computadora que contiene la aplicación móvil, posterior indicará que instale un apk que contiene la ejecución de la aplicación. Se puede ver más de eso a partir del Paso 4: Habilitación de opciones para el desarrollador en el teléfono móvil con sistema operativo Android.

16. Para la segunda opción de ejecución de la aplicación se usa el emulador seleccionando el dispositivo virtual que le aparezca, en este caso Pixel_3a_API_30_x86. En caso de que no tenga instalado ningún dispositivo virtual continúe al literal 16.

**Nota: Verificar que la API del dispositivo sea mayor a 26, caso contrario continuar al literal 17.**

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

16.1 Durante la ejecución de la aplicación mediconline se debe ingresar un usuario y contraseña. No hay usuarios registrados para la aplicación por lo que debe salir el mensaje: “Usted no cuenta con un usuario”

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

16.2 Cuando da clic en el botón Registrarse, debe ingresar sus datos y dar click a grabar para que aparezca la notificación. La interfaz de usuario se encuentra diseñada en el archivo activity_formulario_registro.xml.


<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

17. Si no tiene instalado una versión de SDK para emular la ejecución de la aplicación en un dispositivo móvil, seleccione la opción AVD Manager (Android Virtual Device Manager).


<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

18.	Crear un dispositivo virtual.


<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>


19.	Seleccionar el hardware “Nexus 5X”, luego dar click en el botón siguiente. El hardware seleccionado no es relevante para la práctica, pero es recomendable escoger aquellos con símbolo del Play Store.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

20.	Seleccionar la imagen del API 30, luego dar click en el botón siguiente.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

21. En caso de no tener activado el botón next, dar clic a Download para descargar el API 30 y aceptar el acuerdo de la licencia de Android Software Development Kit.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

### Paso 3: Generación del APK (archivo ejecutable de Android) para instalación de aplicación en el teléfono celular. (5 puntos)

1.	Seleccionar el menú Build > Build APK(s) para generar al archivo con extensión apk, que es un paquete para el sistema operativo Android. 
(*) Este archivo permite ejecutar la aplicación desde el celular.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

2.	Cuando se da clic en el enlace “locate” o en la advertencia podrá ingresar a la ruta donde se encuentra el archivo apk.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

### Paso 4: Habilitación de opciones para el desarrollador en el teléfono móvil con sistema operativo Android. (5 puntos)

**Activar modo de desarrollo y depuración USB en Android**
1.	Vamos a los “Ajustes” o “Configuración” de nuestro dispositivo, dependiendo de la versión de Android.
2.	Nos desplazamos hasta la opción de “Acerca del dispositivo” o “Información del teléfono”.
3.	Buscamos la opción “Número de compilación” o “Número de versión” y presionamos 7 veces seguidas sobre esta opción.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

**Habilitar depuración por USB**

1.	Una vez habilitado el modo desarrollador, puede acceder a las opciones avanzadas.
2.	Habilite la opción “Depuración por USB” o “USB Debugging”.
3.	Cuando se conecte el celular mediante USB, aparecerá el mensaje “Permitir depuración por USB” o “Allow USB Debugging”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

### Paso 5: Ejecución de la aplicación en el teléfono móvil. (5 puntos)
En el Select Device del menú se puede observar como ya está configurado su dispositivo móvil, al hacer click en “run” puede observar cómo se ejecuta la aplicación en el mismo.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

## FORMATO DEL TRABAJO

La práctica de laboratorio será desarrollada en el siguiente formato:

- Nombre del archivo: AMST_LabA_Grupo B_Apellido1_Apellido2_Apellido3
- (*) Siendo A el número del trabajo y B el número del grupo
-	Nombre de la materia
-	Título del trabajo: Ejemplo: Trabajo Autónomo A - Tema
- Nombre de la profesora
- Número de grupo
-	Nombres/Apellidos de los integrantes del grupo que hayan desarrollado el trabajo
-	Fecha de inicio y fin del trabajo
-	Resultados de las actividades planteadas: Explicación de las actividades ejecutadas, incluyendo el código fuente (Java y XML) con las imágenes del proceso. También incluya el enlace del repositorio de Github que contiene el código del proyecto de la aplicación móvil y el archivo ejecutable (*.apk).
-	Conclusiones y Recomendaciones: Respecto a lo aprendido durante el desarrollo del trabajo.
-	Referencias bibliográficas: Colocar los documentos, enlaces web o libros consultados.


## Paso 6: Crear un repositorio (30 puntos).

1.	Dentro de la carpeta del proyecto creado en el paso anterior, abra la línea de comandos de GIT (GIT CLI). Podemos encontrarlo dando clic derecho en la carpeta y escogiendo la opción “GIT BASH HERE”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

- En caso de que no se disponga de GIT CLI, también se puede utilizar CMD de Windows/Ubuntu. Para probar que GIT ha sido instalado correctamente, utilice el comando “git --version”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

***GIT en línea de comandos de Windows***

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

***GIT BASH propia***

2.	Para crear un nuevo repositorio, utilice el siguiente comando “git init”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

***Esto creará un archivo oculto [.git] para el manejo del repositorio y nos ubicará directamente en la rama “master”***

3.	Agregamos todos los archivos del proyecto a nuestro repositorio local con el comando: “git add --all”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

4.	Ahora realizamos un commit, esto realizará nuestros cambios permanentes en el repositorio local. Pero debemos asignarle un mensaje [-m “mensaje”] para indicar los cambios que hemos realizado.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

**Importante:** Para poder realizar un commit es necesario configurar previamente su correo y nombre de usuario, por lo que debe poseer un usuario de GitHub. Los comandos por utilizar para configurar sus credenciales son: 

git config --global user.email "miusuario@example.com"
git config --global user.name "Tu nombre"

Una vez configurado su usuario en git podrá subir su commit.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

5.	Creamos un repositorio en línea. Ahora usaremos GitHub (Requerirá una cuenta gratuita). Del lado superior izquierdo, encontrara el botón “NEW”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

6.	La información requerida para crear un repositorio se muestra a continuación:

**Nombre del repositorio:** El nombre de nuestro repositorio que será publicado en línea.  Para este taller, usaremos AMST[numeroGrupo].

**Descripción (opcional)** Descripción sobre lo que realiza nuestro proyecto

**Tipo** Público o privado (para saber si es visible en línea)

**Archivo Readme** Archivo inicial del repositorio. Agregamos indicaciones para otros programadores

**Agregar. gitignore** Archivo para seleccionar los archivos que no queremos subir a nuestro repositorio

**Licencia** Tipo de licencia: OpenSouce, MIT, Apache, etc.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

  Una vez ingresados todos los campos, se da clic en “Create repository”.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

***Vista del repositorio vacío.***

7.	Damos clic en el botón verde “Code” donde estará visible el **URL** para su manejo y presionamos el botón de copiar.

<p align="center">
  <img src="../imagenes/amst_lab1_.png" alt="appAMST" width="30%">
</p>

8.	Para obtener el repositorio en línea, obtenemos la rama de externa con el comando:

$ git branch -M main (Es necesario un cambio de rama)

$ git remote add origin [link URL del repositorio]



