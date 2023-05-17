---
remote_theme: pages-themes/cayman@v0.2.0
---
[Regresar](/Administracion-de-Sistemas-y-Servicios-en-Red/)

# Unidad 1: Internet y servicios en red

## 🎯 Objetivo de Aprendizaje
Al finalizar la clase el estudiante será capaz de:
- Desarrollar aplicaciones móviles sencillas considerando las características de la programación de dispositivos móviles.

# 1.1. PRINCIPIOS DE COMPUTACIÓN MÓVIL

+ Los sistemas de computación móviles son sistemas informáticos que pueden moverse fácilmente físicamente. Por ejemplo: computadoras portátiles, asistentes digitales personales (PDA) y teléfonos móviles.

+ Entre los aspectos distintivos de los sistemas de computación móvil están la conectividad de red inalámbrica, tamaño pequeño, y fuente de energía.

+ En algunos ambientes el factor de la movilidad juega un rol muy importante, por ejemplo: en el sector de la salud, en los sectores de atención de desastres, en sectores académicos.

+ La integración de las disciplinas de desarrollo de aplicaciones y de ingeniería de software permite la obtención de software de calidad.

+ Si bien existe una variedad de metodologías, técnicas, marcos y herramientas que se utilizan en el desarrollo de software para sistemas estacionarios, hay muy pocos para sistemas móviles.

imagen

# # PRINCIPIOS DE COMPUTACIÓN MÓVIL

+ ### Portabilidad: 
Dispositivos/nodos conectados dentro del sistema de computación móvil facilitan la movilidad.

+ ### Conectividad:
 Esto define la calidad de servicio (QoS) de la conectividad de la red. 

+ ### Interactividad:
 Los nodos que pertenecen a un sistema de computación móvil están conectados entre sí.

+ ### Individualidad: 
Un dispositivo portátil conectado a una red móvil a menudo denota un individuo.

Algunas de las formas más comunes de dispositivos de computación móvil son las siguientes:

+ Computadoras portátiles
+ Las tarjetas inteligentes
+ Teléfonos celulares
+ Computadoras usables (wearable)

Es absolutamente crucial que se entienda las dimensiones de la movilidad y las tenga en cuenta durante todo el proceso de diseño e implementación de la aplicación móvil.


imagen

1. El usuario móvil se está moviendo, al menos ocasionalmente, entre ubicaciones conocidas o desconocidas.

2. El usuario móvil generalmente no está enfocado en la tarea de computación.

3. El usuario móvil con frecuencia requiere altos grados de inmediatez y capacidad de respuesta  del sistema.

4. El usuario móvil está cambiando las tareas con frecuencia y / o abruptamente.

5. El usuario móvil puede requerir acceso al sistema en cualquier lugar y en cualquier momento.

# 1.2. ARQUITECTURA DE SOFTWARE PARA SERVICIOS MÓVILES

El primer paso para crear una aplicación de software, después del proceso de recopilación de requisitos, es establecer un plan de alto nivel sobre cómo será la aplicación cuando finalice. Se conoce a este plan de alto nivel de la aplicación móvil una "arquitectura de software móvil”.

imagen

## INTERFACES DE USUARIO Y CICLO DE VIDA DE ACTIVIDADES

¿Podemos o no podemos usar las mismas metodologías, marcos y herramientas para el desarrollo de aplicaciones móviles?
La respuesta es más bien un "Sí" a medida que el software se acerca al hardware y más un "No" a medida que se aleja del hardware.

Los marcos de referencia que nos ayudan a escribir software que está "más cerca" del hardware, como compiladores y ensambladores. Sin embargo, los marcos de referencia y herramientas de alto nivel, como las herramientas de desarrollo de interfaz de usuario (HTML, JFC, Visual Basic, etc.).

### 1. Marcos de referencia y herramientas completamente centralizados:
 Debido a esta naturaleza integrada de los sistemas móviles totalmente centralizados, los recursos del dispositivo no son una preocupación en el desarrollo de software: las capacidades del cliente se conocen de antemano. Por lo tanto, tres de las dimensiones de la movilidad, a saber, la proliferación de plataformas, las capacidades limitadas de los dispositivos y el soporte para una variedad de interfaces de usuario, no se aplican a las aplicaciones totalmente centralizadas. Ejemplo: Sistemas de campo de batalla utilizados para determinar la ubicación de un objetivo y enviarlo a un sistema centralizado, que luego lo transmite a otro sistema responsable del lanzamiento de un misil.

 ### 2. Marcos de referencia cliente-servidor N-TIER y herramientas:
  Las aplicaciones cliente, en el caso del desarrollo móvil, son típicamente aquellas que se ejecutan en dispositivos móviles. Por lo general, no es posible escribir aplicaciones grandes para que los dispositivos sirvan como cliente, principalmente debido a los recursos limitados en los dispositivos y la gran variedad de ellos. Entonces, la mayoría de las veces, las aplicaciones móviles se distribuyen.

 # 1.3. INTERFACES DE USUARIO Y CICLO DE VIDA DE ACTIVIDADES
¿Podemos o no podemos usar las mismas metodologías, marcos y herramientas para el desarrollo de aplicaciones móviles?
La respuesta es más bien un "Sí" a medida que el software se acerca al hardware y más un "No" a medida que se aleja del hardware.

Los marcos de referencia que nos ayudan a escribir software que está "más cerca" del hardware, como compiladores y ensambladores. Sin embargo, los marcos de referencia y herramientas de alto nivel, como las herramientas de desarrollo de interfaz de usuario (HTML, JFC, Visual Basic, etc.).

1. ### Marcos de referencia y herramientas completamente centralizados: 

Debido a esta naturaleza integrada de los sistemas móviles totalmente centralizados, los recursos del dispositivo no son una preocupación en el desarrollo de software: las capacidades del cliente se conocen de antemano. Por lo tanto, tres de las dimensiones de la movilidad, a saber, la proliferación de plataformas, las capacidades limitadas de los dispositivos y el soporte para una variedad de interfaces de usuario, no se aplican a las aplicaciones totalmente centralizadas. Ejemplo: Sistemas de campo de batalla utilizados para determinar la ubicación de un objetivo y enviarlo a un sistema centralizado, que luego lo transmite a otro sistema responsable del lanzamiento de un misil.


2. ### Marcos de referencia cliente-servidor N-TIER y herramientas:

 Las aplicaciones cliente, en el caso del desarrollo móvil, son típicamente aquellas que se ejecutan en dispositivos móviles. Por lo general, no es posible escribir aplicaciones grandes para que los dispositivos sirvan como cliente, principalmente debido a los recursos limitados en los dispositivos y la gran variedad de ellos. Entonces, la mayoría de las veces, las aplicaciones móviles se distribuyen.

imágen

## TIPOS DE APLICACIONES

1. Aplicaciones nativas
2. Aplicaciones web
3. Aplicaciones híbridas
4. Aplicaciones avanzadas

imagen

## PATRONES DE DISEÑO PARA INTERFACES DE USUARIO MÓVIL

La «Ley del pulgar» se refiere a la superficie de pantalla a la que este dedo tiene acceso sin mayores problemas y nos da pistas para organizar jerárquicamente los elementos en la interfaz.

imagen

## PROTOTIPADO MÓVIL

Las herramientas para el diseño del prototipado móvil son las siguientes:

Proto.io
https://proto.io

Marvelapp
https://marvelapp.com

https://spaces.proto.io/project/BFCB3D3D-0E94-EEFC-B26C-10502C54FB41/TeenTa-universal/

Adobe XD
https://www.adobe.com/la/products/xd.html

## MODELO-VISTA-CONTROLADOR EN ANDROID

imagen

1. Las clases de modelos están diseñadas para modelar las cosas que conciernen a su aplicación, como un usuario.
2. Los objetos modelo no tienen conocimiento de la interfaz de usuario; su único propósito es mantener y administrar datos.
3. En las aplicaciones de Android, las clases de modelos son generalmente clases personalizadas que crea. 
4. Todos los objetos modelo en su aplicación componen su capa modelo.
5. La capa de modelo de GeoQuiz consiste en la clase TrueFalse.


## ESTRUCTURA DEL SISTEMA OPERATIVO ANDROID

1. Aplicaciones escritas en Java.
2. Arquitectura diseñada para simplificar la reutilización de componentes.
3. Incluye un conjunto de bibliotecas de C/C++ usadas por varios componentes del sistema
4. Incluye un set de bibliotecas base que proporcionan la mayor parte de las funciones disponibles en las bibliotecas base del lenguaje Java.
5. Android depende de Linux para los servicios base del sistema como seguridad, gestión de memoria, gestión de procesos, pila de red y modelo de controladores.

imagen

## VERSIONES DE ANDROID

imagen
Los datos recogidos durante un período final de 7 días, el 6 de Junio 2016. 


## ENTORNO DE DESARROLLO

+ Java JDK 1.6+
(http://www.oracle.com/technetwork/java/javase/downloads/index.html)
+ IDE Eclipse 
(http://www.eclipse.org/downloads/)
+ Android SDK
(http://developer.android.com/sdk/index.html)
+ AVD Manager
+ Android Development Tools
( https://dll-ssl.google.com/android/eclipse/ )


1. Android SDK Tools
2. Android SDK Platform-tools
3. Android SDK Build-tools (la versión más reciente disponible)
4. Una o más versiones de la plataforma Android
5. Android Support Repository (extras)
6. Google Repository (extras)
7. Google Play Services (extras)

## ESTRUCTURA DE UN PROYECTO

app>java>com.example.myfirstapp>MainActivity
Esta es la actividad principal (el punto de entrada para tu app). Cuando compilas y ejecutas la app, el sistema inicia una instancia de esta Activity y carga su diseño.

app>res>layout>activity_main.xml
Este archivo XML define el diseño correspondiente a la IU de la actividad. Contiene elementos editText y Button.

Gradle Scripts > build.gradle
Dos archivos con este nombre: uno para el proyecto ("Project: MyFirstApp") y otro para el módulo de la "app" ("Module: app"). Cada módulo tiene su propio archivo build.gradle, pero este proyecto por el momento tiene un solo módulo. Trabajarás principalmente con el archivo build.gradle del módulo para configurar la forma en que las herramientas de Gradle compilan y crean tu app.

app>manifests>AndroidManifest.xml
El archivo de manifiesto describe las características fundamentales de la app y define cada uno de sus componentes.

Diseño de la interfaz de usuario

imagen

## COMPONENTES DE UNA APLICACIÓN

+ ### Activity: 
Las actividades (activities) representan el componente principal de la interfaz gráfica de una aplicación Android.
+ ### View: 
Son los componentes básicos con los que se construyen la interfaz gráfica de la aplicación.
+ ### Service: 
Son los componentes sin interfaz gráfica que se ejecutan en segundo plano.
+ ### Content Provider: 
Es el mecanismo que se ha definido en Android para compartir datos entre aplicaciones.
+ ### Broadcast Receiver:
Es un componente destinado a detectar y reaccionar ante determinados mensajes o eventos globales generados por el sistema.
+ ### Widget: 
Son elementos visuales, interactivos, que pueden mostrarse en la pantalla principal.
+ ### Intent:
Es el elemento básico de comunicación entre los distintos componentes Android que hemos descrito anteriormente.

## DISEÑO DE UNA APLICACIÓN MÓVIL

El splash/pantalla de bienvenida/pantalla de inicio, es la primera pantalla que verá el usuario al iniciar la app. Su uso está siendo cada vez más limitado, por lo que generalmente se muestra rápidamente la primera vez que se abre la aplicación. Esta pantalla sirve como presentación del contenido mientras se realiza la carga inicial, por tanto, es normal que se incluya un elemento indicativo de carga junto a los demás elementos gráficos.

imagen

+ Crear una aplicación donde se ingresa el nombre del usuario y la clave, al dar click en “Login” el usuario accederá a la aplicación.

imagen

## PROCESO DE CONSTRUCCIÓN DE ANDROID

imagen

## INTERFAZ DE USUARIO: LAYOUTS

### FrameLayout

imagen

Un FrameLayout coloca todos sus controles hijos alineados con su esquina superior izquierda, de forma que cada control quedará oculto por el control siguiente. 

### LinearLayout
imagen
Este layout apila uno tras otro todos sus  Elementos hijos de forma horizontal o Vertical según se establezca su propiedad Android:orientation


### TableLayout

imagen
Un TableLayout permite distribuir sus elementos hijos de forma tabular, definiendo las filas y columnas necesarias, y la posición de cada componente dentro de la tabla.

### RelativeLayout

imagen
Este layout permite especificar la posición de cada elemento de forma relativa a su elemento padre o a cualquier otro elemento incluido en el propio layout.

## INTERFAZ DE USUARIO: LAYOUTS

imagen

## LAYOUTS PROPIEDADES

+ ### Posición relativa a otro control:

Android:layout_above
Android:layout_below
Android:layout_toLeftOf
Android:layout_toRightOf
Android:layout_alignLeft
Android:layout_alignRight
Android:layout_alignTop
Android:layout_alignBottom
Android:layout_alignBaseline

+ ### Posición relativa al layout padre:

Android:layout_alignParentLeft
Android:layout_alignParentRight
android:layout_alignParentTop.
android:layout_alignParentBotto
android:layout_centerHorizontal.
android:layout_centerVertical
android:layout_centerInParent.

## LAYOUTS PROPIEDADES

+ ### Opciones de margen

android:layout_margin
android:layout_marginBottom
android:layout_marginTop
android:layout_marginLeft
android:layout_marginRight

### Opciones de espaciado o padding

android:padding
android:paddingBottom
android:paddingTop
android:paddingLeft
android:paddingRight

## INTERFAZ DE USUARIO: CONTROLES BÁSICOS

+ El SDK de Android nos proporciona tres tipos de botones:
+ El clásico (Button)
+ El de tipo on/off (ToggleButton)
+ El que puede contener una imagen (Imagebutton)


<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:app="http://schemas.android.com/apk/res-auto"
   xmlns:tools="http://schemas.android.com/tools"
   android:id="@+id/linearLayout"
   android:layout_width="match_parent"
   android:layout_height="match_parent"
   android:orientation="vertical"
   tools:context=".MainActivity">

   <Button
       android:id="@+id/btnPulsame"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:layout_marginStart="156dp"
       android:layout_marginTop="24dp"
       android:text="@string/pulsame" />

   <ToggleButton
       android:id="@+id/tgbuttonEstado"
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:layout_marginStart="156dp"
       android:layout_marginTop="100dp"
       android:checked="true"
       android:textOff="@string/off"
       android:textOn="@string/on" />

   <ImageButton
       android:id="@+id/imageButton3"
       android:layout_width="wrap_content"
       android:layout_height="269dp"
       android:layout_marginStart="156dp"
       android:layout_marginTop="100dp"
       android:layout_weight="1"
       android:contentDescription="@string/app_name"
       tools:srcCompat="@tools:sample/avatars" />

</LinearLayout>

## Eventos de un botón

btnBoton1 = (Button)findViewById(R.id.BtnBoton1);
btnBoton1.setOnClickListener(new View.OnClickListener() {
		    public void onClick(View arg0) {
		        lblMensaje.setText("Botón 1 pulsado!");
		    }
		});


btnBoton2 = (ToggleButton)findViewById(R.id.BtnBoton2);
btnBoton2.setOnClickListener(new View.OnClickListener() {
	public void onClick(View arg0) {
		if(btnBoton2.isChecked())
		            lblMensaje.setText("Botón 2: ON");
		        else
		            lblMensaje.setText("Botón 2: OFF");
		    }
		});


## Control ImageView


<ImageView android:id="@+id/ImgFoto"
		    layut
		    android:layout_height="wrap_content"
		    android:src="@drawable/icon"
		    android:contentDescription="@string/imagen_ejemplo" />

        ImageView img= (ImageView)findViewById(R.id.ImgFoto);
		img.setImageResource(R.drawable.icon);
    

## Control TextView

<TextView android:id="@+id/LblEtiqueta"
		    android:layout_width="matchfill_parent"
		    android:layout_height="wrap_content"
		    android:text="@string/escribe_algo"
		    android:background="#AA44FF"
		    android:typeface="monospace" />


final TextView lblEtiqueta = (TextView)findViewById(R.id.LblEtiqueta);
		String texto = lblEtiqueta.getText().toString();
		texto += "123";
		lblEtiqueta.setText(texto);
		lblEtiqueta.setBackgroundColor(Color.BLUE);


## Control EditText

<EditText android:id="@+id/txtTexto"
		    android:layout_width="match_parent"
		    android:layout_height="wrap_content"
		    android:inputType="text" />

final EditText txtTexto = (EditText)findViewById(R.id.txtTexto);
String texto = txtTexto.getText().toString();
txtTexto.setText("Hola mundo!");


## Control CheckBox

<CheckBox android:id="@+id/ChkMarcame"
	android:layout_width="wrap_content"
	android:layout_height="wrap_content"
	android:text="@string/marcame"
	android:checked="false" />


if (checkBox.isChecked()) {
	checkBox.setChecked(false);
}

## Control CheckBox Evento

private CheckBox cbMarcame;
cbMarcame = (CheckBox)findViewById(R.id.chkMarcame);		 
cbMarcame.setOnCheckedChangeListener(
	new CheckBox.OnCheckedChangeListener() {
	public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
		            if (isChecked) {
		                cbMarcame.setText("Checkbox marcado!");
		            }
		            else {
		                cbMarcame.setText("Checkbox desmarcado!");
		            }
    }});


## Control RadioButton

<RadioGroup android:id="@+id/gruporb"
		    android:orientation="vertical"
		    android:layout_width="match_parent"
		    android:layout_height="match_parent" >
		 
		    <RadioButton android:id="@+id/radio1"
		        android:layout_width="wrap_content"
		        android:layout_height="wrap_content"
		        android:text="@string/opcion_1" />
		 
		    <RadioButton android:id="@+id/radio2"
		        android:layout_width="wrap_content"
		        android:layout_height="wrap_content"
		        android:text="@string/opcion_2" />
		</RadioGroup>

  
  RadioGroup rg = (RadioGroup)findViewById(R.id.gruporb);
		rg.clearCheck();
		rg.check(R.id.radio1);
		int idSeleccionado = rg.getCheckedRadioButtonId();

  
  private TextView lblMensaje;
private RadioGroup rgOpciones;		 
lblMensaje = (TextView)findViewById(R.id.LblSeleccion);
rgOpciones = (RadioGroup)findViewById(R.id.gruporb);
rgOpciones.setOnCheckedChangeListener(
	new RadioGroup.OnCheckedChangeListener() {
	public void onCheckedChanged(RadioGroup group, int checkedId) {
		lblMensaje.setText("ID opción seleccionada: " + checkedId);
	}
});

## INTERFAZ DE USUARIO: CONTROLES DE SELECCIÓN

1. ### ArrayAdapter: 
Es el más sencillo de todos los adaptadores, y provee de datos a un control de selección a partir de un array de objetos de cualquier tipo.

2. ### SimpleAdapter:
 Se utiliza para mapear datos sobre los diferentes controles definidos en un fichero XML de layout.

3. ### SimpleCursorAdapter: 
Se utiliza para mapear las columnas de un cursor abierto sobre una base de datos sobre los diferentes elementos visuales contenidos en el control de selección.


