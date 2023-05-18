---
remote_theme: pages-themes/leap-day@v0.2.0
---
[Regresar](/Aplicaciones-Moviles-y-Servicios-Telematicos/)

# Unidad 1: Desarrollo de aplicaciones móviles
## 🎯 Objetivo de Aprendizaje
Al finalizar la clase el estudiante será capaz de:
- Desarrollar aplicaciones móviles sencillas considerando las características de la programación de dispositivos móviles.

# 1.1. 📲 Principios de Computación Móvil
<p align="center">
  <img src="../imagenes/movil.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="movil">
</p>

+ Los sistemas de computación móviles son sistemas informáticos que pueden moverse fácilmente físicamente. Por ejemplo: computadoras portátiles, asistentes digitales personales (PDA) y teléfonos móviles.

+ Entre los aspectos distintivos de los sistemas de computación móvil están la conectividad de red inalámbrica, tamaño pequeño, y fuente de energía.

+ En algunos ambientes el factor de la movilidad juega un rol muy importante, por ejemplo: en el sector de la salud, en los sectores de atención de desastres, en sectores académicos.

<p align="center">
  <img src="../imagenes/tiempo.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="tiempo">
</p>


+ La integración de las disciplinas de desarrollo de aplicaciones y de ingeniería de software permite la obtención de software de calidad.

+ Si bien existe una variedad de metodologías, técnicas, marcos y herramientas que se utilizan en el desarrollo de software para sistemas estacionarios, hay muy pocos para sistemas móviles.

imagen

<<<<<<< HEAD
## 🌐 Portabilidad: 
=======
# # PRINCIPIOS DE COMPUTACIÓN MÓVIL


+ ### Portabilidad: 
>>>>>>> 048df13bc50bb3dfd5c08684057ab45534fb3b6d
Dispositivos/nodos conectados dentro del sistema de computación móvil facilitan la movilidad.

## 🌐 Conectividad:
 Esto define la calidad de servicio (QoS) de la conectividad de la red. 

## 🌐 Interactividad:
 Los nodos que pertenecen a un sistema de computación móvil están conectados entre sí.

## 🌐 Individualidad: 
Un dispositivo portátil conectado a una red móvil a menudo denota un individuo.

Algunas de las formas más comunes de dispositivos de computación móvil son las siguientes:

- Computadoras portátiles
- Las tarjetas inteligentes
- Teléfonos celulares
- Computadoras usables (wearable)

Es absolutamente crucial que se entienda las dimensiones de la movilidad y las tenga en cuenta durante todo el proceso de diseño e implementación de la aplicación móvil.

<p align="center">
  <img src="../imagenes/movilidad.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="movilidad">
</p>

1. El usuario móvil se está moviendo, al menos ocasionalmente, entre ubicaciones conocidas o desconocidas.

2. El usuario móvil generalmente no está enfocado en la tarea de computación.

3. El usuario móvil con frecuencia requiere altos grados de inmediatez y capacidad de respuesta  del sistema.

4. El usuario móvil está cambiando las tareas con frecuencia y / o abruptamente.

5. El usuario móvil puede requerir acceso al sistema en cualquier lugar y en cualquier momento.

# 1.2. ARQUITECTURA DE SOFTWARE PARA SERVICIOS MÓVILES

<p align="center">
  <img src="../imagenes/apmoviles.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="apmoviles">
</p>

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


<p align="center">
  <img src="../imagenes/diseno.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="diseno">
</p>

¿Podemos o no podemos usar las mismas metodologías, marcos y herramientas para el desarrollo de aplicaciones móviles?
La respuesta es más bien un "Sí" a medida que el software se acerca al hardware y más un "No" a medida que se aleja del hardware.

Los marcos de referencia que nos ayudan a escribir software que está "más cerca" del hardware, como compiladores y ensambladores. Sin embargo, los marcos de referencia y herramientas de alto nivel, como las herramientas de desarrollo de interfaz de usuario (HTML, JFC, Visual Basic, etc.).

1. ### Marcos de referencia y herramientas completamente centralizados: 

Debido a esta naturaleza integrada de los sistemas móviles totalmente centralizados, los recursos del dispositivo no son una preocupación en el desarrollo de software: las capacidades del cliente se conocen de antemano. Por lo tanto, tres de las dimensiones de la movilidad, a saber, la proliferación de plataformas, las capacidades limitadas de los dispositivos y el soporte para una variedad de interfaces de usuario, no se aplican a las aplicaciones totalmente centralizadas. Ejemplo: Sistemas de campo de batalla utilizados para determinar la ubicación de un objetivo y enviarlo a un sistema centralizado, que luego lo transmite a otro sistema responsable del lanzamiento de un misil.


2. ### Marcos de referencia cliente-servidor N-TIER y herramientas:

 Las aplicaciones cliente, en el caso del desarrollo móvil, son típicamente aquellas que se ejecutan en dispositivos móviles. Por lo general, no es posible escribir aplicaciones grandes para que los dispositivos sirvan como cliente, principalmente debido a los recursos limitados en los dispositivos y la gran variedad de ellos. Entonces, la mayoría de las veces, las aplicaciones móviles se distribuyen.

imágen

## TIPOS DE APLICACIONES

<p align="center">
  <img src="../imagenes/aphibrida.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="aphibrida">
</p>

1. Aplicaciones nativas
2. Aplicaciones web
3. Aplicaciones híbridas
4. Aplicaciones avanzadas

imagen

## PATRONES DE DISEÑO PARA INTERFACES DE USUARIO MÓVIL


<p align="center">
  <img src="../imagenes/diseno2.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="diseno2">
</p>

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


<p align="center">
  <img src="../imagenes/ctrlandroid1.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="ctrlandroid1">
</p>

<p align="center">
  <img src="../imagenes/ctrlandroid2.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="ctrlandroid2">
</p>

<p align="center">
  <img src="../imagenes/ctrlandroid3.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="ctrlandroid3">
</p>

1. Las clases de modelos están diseñadas para modelar las cosas que conciernen a su aplicación, como un usuario.
2. Los objetos modelo no tienen conocimiento de la interfaz de usuario; su único propósito es mantener y administrar datos.
3. En las aplicaciones de Android, las clases de modelos son generalmente clases personalizadas que crea. 
4. Todos los objetos modelo en su aplicación componen su capa modelo.
5. La capa de modelo de GeoQuiz consiste en la clase TrueFalse.


## ESTRUCTURA DEL SISTEMA OPERATIVO ANDROID

<p align="center">
  <img src="../imagenes/sistemaoper.jpg" style="width: 30%; height: 180px; float: left; padding: 15px;" alt="sistemaoper">
</p>

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

## ArrayAdapter

final String[] datos =
	new String[]{"Elem1","Elem2","Elem3","Elem4","Elem5"};
		 
ArrayAdapter<String> adaptador =
	new ArrayAdapter<String>(
		this, android.R.layout.simple_spinner_item, datos);

    <?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="valores_array">
        <item>Elem1</item>
        <item>Elem2</item>
        <item>Elem3</item>
        <item>Elem4</item>
        <item>Elem5</item>
    </string-array>
</resources>

ArrayAdapter<CharSequence> adapter =
    ArrayAdapter.createFromResource(this,
        R.array.valores_array,
        android.R.layout.simple_spinner_item);


## Spinner

Funcionan de forma similar al de cualquier control de este tipo, el usuario selecciona la lista, se muestra una especie de lista emergente al usuario con todas las opciones disponibles y al seleccionarse una de ellas ésta queda fijada en el control.

<Spinner android:id="@+id/CmbOpciones"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />

private Spinner cmbOpciones;
 
cmbOpciones = (Spinner)findViewById(R.id.CmbOpciones);
adaptador.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
cmbOpciones.setAdapter(adaptador);


Funcionan de forma similar al de cualquier control de este tipo, el usuario selecciona la lista, se muestra una especie de lista emergente al usuario con todas las opciones disponibles y al seleccionarse una de ellas ésta queda fijada en el control.

<Spinner android:id="@+id/CmbOpciones"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />

private Spinner cmbOpciones;
 
cmbOpciones = (Spinner)findViewById(R.id.CmbOpciones);
adaptador.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
cmbOpciones.setAdapter(adaptador);

 imagenes

 ## EVENTO CONTROL SPINNER

 cmbOpciones.setOnItemSelectedListener(
        new AdapterView.OnItemSelectedListener() {
        public void onItemSelected(AdapterView<?> parent,
            android.view.View v, int position, long id) {
                lblMensaje.setText("Seleccionado: " + datos[position]);
        }
 
        public void onNothingSelected(AdapterView<?> parent) {
            lblMensaje.setText("");
        }
});

## ListView

<ListView android:id="@+id/LstOpciones"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" />

final String[] datos = new String[]{"Elem1","Elem2","Elem3","Elem4","Elem5"};
 
ArrayAdapter<String> adaptador =
    new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, datos);
lstOpciones = (ListView)findViewById(R.id.LstOpciones); 
lstOpciones.setAdapter(adaptador);

## GridView

El control GridView de Android presenta al usuario un conjunto de opciones seleccionables distribuidas de forma tabular, o dicho de otra forma, divididas en filas y columnas. Dada la naturaleza del control ya podéis imaginar sus propiedades más importantes, que paso a enumerar a continuación:

<GridView android:id="@+id/GridOpciones"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:numColumns="auto_fit"
    android:columnWidth="80px"
    android:horizontalSpacing="5dp"
    android:verticalSpacing="10dp"
    android:stretchMode="columnWidth" />

imagen

private String[] datos = new String[25];
for(int i=1; i<=25; i++)
        datos[i-1] = "Dato " + i;
 ArrayAdapter<String> adaptador = 
new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, datos);
grdOpciones = (GridView)findViewById(R.id.GridOpciones);
grdOpciones.setAdapter(adaptador);

## Evento

grdOpciones.setOnItemClickListener(
   new AdapterView.OnItemClickListener() {
      public void onItemClick(AdapterView<?> parent,
         android.view.View v, int position, long id) {
            lblMensaje.setText("Opción seleccionada: " + datos[position]);
         }
   });


## INTERFAZ DE USUARIO: CONTROLES PERSONALIZADOS

Android admite por supuesto crear controles personalizados, y permite hacerlo de diferentes formas:

+ Extendiendo la funcionalidad de un control ya existente.
+ Combinando varios controles para formar otro más complejo.
+ Diseñando desde cero un nuevo control.

Vamos a extender el control EditText (cuadro de texto) para que muestre en todo momento el número de caracteres que contiene a medida que se escribe en él. Intentaríamos emular algo así como el editor de mensajes SMS del propio sistema operativo, que nos avisa del número de caracteres que contiene el mensaje.

imagen

Creación de controles compuestos, es decir, controles personalizados construidos a partir de varios controles estándar, combinando la funcionalidad de todos ellos en un sólo control reutilizable en otras aplicaciones.

imagen

Vamos a construir un control que nos permita seleccionar un color entre varios disponibles.

Los colores disponibles van a ser sólo cuatro, que se mostrarán en la franja superior del control. En la parte inferior se mostrará el color seleccionado en cada momento, o permanecerá negro si aún no se ha seleccionado ningún color.

imagen

## PESTAÑAS

1. Creamos un contenedor principal de nuestro conjunto de pestañas y deberá tener obligatoriamente como id el valor “@android:id/tabhost”. 

2. Dentro de éste vamos a incluir un LinearLayout que nos servirá para distribuir verticalmente las secciones principales del layout: la sección de pestañas en la parte superior y la sección de contenido en la parte inferior

3. La sección de pestañas se representará mediante un elemento TabWidget, que deberá tener como id el valor “@android:id/tabs”.

4. Como contenedor para el contenido de las pestañas añadiremos un FrameLayout con el id obligatorio “@android:id/tabcontent”.

5. Por último, dentro del FrameLayout  incluiremos el contenido de cada pestaña, normalmente cada uno dentro de su propio layout principal y con un id único que nos permita posteriormente hacer referencia a ellos fácilmente.

imagen

## MENÚS EN ANDROID

En Android podemos encontrar 3 tipos diferentes de menús:

   Menús Principales. Los más habituales, aparecen en la zona inferior de la pantalla al pulsar el botón ‘menu’ del teléfono.
   Submenús. Son menús secundarios que se pueden mostrar al pulsar sobre una opción de un menú principal.
   Menús Contextuales. Útiles en muchas ocasiones, aparecen al realizar una pulsación larga sobre algún elemento de la pantalla.

   imagen

## WIDGETS

Los pasos principales para la creación de un widget Android son los siguientes:

1. Definición de su interfaz gráfica (layout).
2. Configuración XML del widget (AppWidgetProviderInfo).
3. Implementación de la funcionalidad del widget (AppWidgetProvider) , especialmente su evento de actualización.
4. Declaración del widget en el Android Manifest de la aplicación.

Fórmula para ajustar las dimensiones de nuestro widget 
+  ancho_mínimo = (num_celdas * 70) – 30
+ alto_mínimo = (num_celdas * 70) – 30

### Métodos destacados:

   + onEnabled(): lanzado cuando se crea la primera instancia de un widget.
   + onUpdate(): lanzado periodicamente cada vez que se debe actualizar un widget, por ejemplo cada vez que se cumple el periodo de tiempo definido por el parámetro updatePeriodMillisantes descrito, o cuando se añade el widget al escritorio.
   + onDeleted(): lanzado cuando se elimina del escritorio una instancia de un widget.
   + onDisabled(): lanzado cuando se elimina del escritorio la última instancia de un widget.

   El widget se declarará como un elemento <receiver> y deberemos aportar la siguiente información:

   + Atributo name: Referencia a la clase java de nuestro widget, creada en el paso anterior.
   + Elemento <intent-filter>, donde indicaremos los “eventos” a los que responderá nuestro widget, 
   normalmente añadiremos el evento APPWIDGET_UPDATE, para detectar la acción de actualización.
   + Elemento <meta-data>, donde haremos referencia con su atributo resource al XML de configuración que creamos en el segundo paso del proceso.


## PREFERENCIAS EN ANDROID: SHARED PREFERENCES

    + MODE_PRIVATE. Sólo nuestra aplicación tiene acceso a estas preferencias.
    + MODE_WORLD_READABLE. Todas las aplicaciones pueden leer estas preferencias, pero sólo la nuestra puede modificarlas.
   + MODE_WORLD_WRITABLE. Todas las aplicaciones pueden leer y modificar estas preferencias.

    Estos ficheros XML se almacenan en una ruta que sigue el siguiente patrón:

/data/data/paquete.java/shared_prefs/nombre_coleccion.xml

Así, por ejemplo, en nuestro caso encontraríamos nuestro fichero de preferencias en la ruta:
/data/data/com.curso.android.preferences1/shared_prefs/MisPreferencias.xml

imagen

## PREFERENCIAS EN ANDROID: PREFERENCE ACTIVITY

imagen

CheckBoxPreference. Marca seleccionable.
   EditTextPreference. Cadena simple de texto.
   ListPreference. Lista de valores seleccionables (exclusiva).
   MultiSelectListPreference. Lista de valores seleccionables (múltiple).

###  CheckBoxPreference

Representa un tipo de opción que sólo puede tomar dos valores distintos: activada o desactivada. Es el equivalente a un control de tipo checkbox. En este caso tan sólo tendremos que especificar los atributos: nombre interno de la opción (android:key), texto a mostrar (android:title) y descripción de la opción (android:summary).

<CheckBoxPreference
    android:key="opcion1"
    android:title="Preferencia 1"
    android:summary="Descripción de la preferencia 1" />


### EditTextPreference

Representa un tipo de opción que puede contener como valor una cadena de texto. Al pulsar sobre una opción de este tipo se mostrará un cuadro de diálogo sencillo que solicitará al usuario el texto a almacenar. Para este tipo, además de los tres atributos comunes a todas las opciones (key, title y summary) también tendremos que indicar el texto a mostrar en el cuadro de diálogo, mediante el atributo android:dialogTitle

<EditTextPreference
   android:key="opcion2"
   android:title="Preferencia 2"
   android:summary="Descripción de la preferencia 2"
   android:dialogTitle="Introduce valor" />


### ListPreference

Representa un tipo de opción que puede tomar como valor un elemento, y sólo uno, seleccionado por el usuario entre una lista de valores predefinida. Al pulsar sobre una opción de este tipo se mostrará la lista de valores posibles y el usuario podrá seleccionar uno de ellos. Y en este caso seguimos añadiendo atributos. Además de los cuatro ya comentados (key, title, summary y dialogTitle) tendremos que añadir dos más, uno de ellos indicando la lista de valores a visualizar en la lista y el otro indicando los valores internos que utilizaremos para cada uno de los valores de la lista anterior 

<?xml version="1.0" encoding="utf-8" ?>
<resources>
   <string-array name="pais">
      <item>España</item>
      <item>Francia</item>
      <item>Alemania</item>
   </string-array>
   <string-array name="codigopais">
      <item>ESP</item>
      <item>FRA</item>
      <item>ALE</item>
   </string-array>
</resources>


<ListPreference
   android:key="opcion3"
   android:title="Preferencia 3"
   android:summary="Descripción preferencia3"
   android:dialogTitle="Indicar Pais"
   android:entries="@array/pais"
   android:entryValues="@array/codigopais" />


## MultiSele
## TRATAMIENTO DE XML

Los dos modelos más extendidos son SAX (Simple API for XML) y DOM (Document Object Model).


ctListPreference

Las opciones de este tipo son muy similares a las ListPreference, con la diferencia de que el usuario puede seleccionar varias de las opciones de la lista de posibles valores. Los atributos a asignar son por tanto los mismos que para el tipo anterior.

<MultiSelectListPreference
   android:key="opcion4"
   android:title="Preferencia 4"
   android:summary="Descripción de la preferencia 4"
   android:dialogTitle="Indicar Pais"
   android:entries="@array/pais"
   android:entryValues="@array/codigopais" />

## TRATAMIENTO DE XML

Los dos modelos más extendidos son SAX (Simple API for XML) y DOM (Document Object Model).

### SAX en Android


En el modelo SAX, el tratamiento de un XML se basa en un analizador (parser) que a medida que lee secuencialmente el documento XML va generando diferentes eventos con la información de cada elemento leido.
Así por ejemplo, a medida que lee el XML, si encuentra el comienzo de una etiqueta <title> generará un evento de comienzo de etiqueta, startElement(), con su información asociada, si después de esa etiqueta encuentra un fragmento de texto generará un evento characters() con toda la información necesaria, y así sucesivamente hasta el final del documento.

Los principales eventos que se pueden producir son los siguientes (consultar aquí la lista completa):

startDocument(): comienza el documento XML.
endDocument(): termina el documento XML.
startElement(): comienza una etiqueta XML.
endElement(): termina una etiqueta XML.
characters(): fragmento de texto.

Todos estos métodos están definidos en la clase org.xml.sax.helpers.DefaultHandler, de la cual deberemos derivar una clase propia donde se sobrescriban los eventos necesarios.

## NOTIFICACIONES: TOAST

Un toast es un mensaje que se muestra en pantalla durante unos segundos al usuario para luego volver a desaparecer automáticamente sin requerir ningún tipo de actuación por su parte, y sin recibir el foco en ningún momento (o dicho de otra forma, sin interferir en las acciones que esté realizando el usuario en ese momento). Aunque son personalizables, aparecen por defecto en la parte inferior de la pantalla, sobre un rectángulo gris ligeramente translúcido.

imagen

## NOTIFICACIONES: BARRA DE ESTADO

Las notificaciones de la barra de estado de Android. Estas notificaciones son las que se muestran en nuestro dispositivo por ejemplo cuando recibimos un mensaje SMS, cuando tenemos actualizaciones disponibles, cuando tenemos el reproductor de música abierto en segundo plano, … Estas notificaciones constan de un icono y un texto mostrado en la barra de estado superior, y adicionalmente un mensaje algo más descriptivo y una marca de fecha/hora que podemos consultar desplegando la bandeja del sistema.

imagen

## NOTIFICACIONES: DIÁLOGOS

Los diálogos de Android los podremos utilizar con distintos fines, en general:

Mostrar un mensaje.
Pedir una confirmación rápida.
Solicitar al usuario una elección (simple o múltiple) entre varias alternativas.


## DIÁLOGO DE ALERTA

Este tipo de diálogo se limita a mostrar un mensaje sencillo al usuario, y un único botón de OK para confirmar su lectura.

imagen

## DIÁLOGO DE CONFIRMACIÓN

Un diálogo de confirmación es muy similar al anterior, con la diferencia de que lo utilizaremos para solicitar al usuario que nos confirme una determinada acción, por lo que las posibles respuestas serán del tipo Sí/No.

imagen

## DIÁLOGO DE SELECCIÓN

Cuando las opciones a seleccionar por el usuario no son sólo dos, como en los diálogos de confirmación, sino que el conjunto es mayor podemos utilizar los diálogos de selección para mostrar una lista de opciones entre las que el usuario pueda elegir.

imagen

## PROCESOS Y SUBPROCESOS

+ Cuando se inicia un componente de la aplicación y la aplicación no tiene ningún otro componente en ejecución, el sistema Android inicia un nuevo proceso de Linux para la aplicación con un solo hilo de ejecución. 
+ Por defecto, todos los componentes de la misma aplicación se ejecutan en el mismo proceso y subproceso (llamado el subproceso "principal"). 
+ Si se inicia un componente de la aplicación y ya existe un proceso para esa aplicación (porque existe otro componente de la aplicación), entonces el componente se inicia dentro de ese proceso y utiliza el mismo hilo de ejecución. 
+ Sin embargo, puede organizar diferentes componentes en su aplicación para que se ejecuten en procesos separados, y puede crear hilos adicionales para cualquier proceso.
+ En el dispositivo móvil en la opción Ajustes > Opciones de desarrollador  > Estadísticas de procesos se muestran los procesos.

imagen

## PROCESOS Y SUBPROCESOS

Por defecto, todos los componentes de la misma aplicación se ejecutan en el mismo proceso y la mayoría de las aplicaciones no deberían cambiar esto. Sin embargo, si encuentra que necesita controlar a qué proceso pertenece un determinado componente, puede hacerlo en el archivo de manifiest.
La entrada de manifiest para cada tipo de elemento componente: <activity>, <service>, <receiver> y <provider>, admite un atributo android: process que puede especificar un proceso en el que se debe ejecutar ese componente.

# 1.4. HILOS (THREADS)

+ Cuando se inicia una aplicación, el sistema crea un hilo de ejecución para la aplicación, llamado "main". 
+ Este hilo es muy importante porque se encarga de enviar eventos a los widgets de interfaz de usuario apropiados, incluidos los eventos de dibujo. 
+ También es casi siempre el hilo en el que su aplicación interactúa con los componentes del kit de herramientas de la interfaz de usuario de Android (componentes de los paquetes android.widget y android.view). 
+ Como tal, el hilo principal también a veces se llama hilo de la interfaz de usuario. Sin embargo, en circunstancias especiales, el hilo principal de una aplicación podría no ser su hilo de interfaz de usuario.
+ El sistema no crea un hilo separado para cada instancia de un componente. Todos los componentes que se ejecutan en el mismo proceso se instancian en el subproceso de la interfaz de usuario, y las llamadas del sistema a cada componente se envían desde ese subproceso.

IMAGEN

## SERVICIOS

Estos son los tres tipos de servicios:

Primer plano
Segundo plano
Enlace

## SERVICIOS EN SEGUNDO PLANO

+ Un servicio es un componente de una aplicación que puede realizar operaciones de larga ejecución en segundo plano y que no proporciona una interfaz de usuario.

+ Otro componente de la aplicación puede iniciar un servicio y continuará ejecutándose en segundo plano aunque el usuario cambie a otra aplicación.

+ Por ejemplo, un servicio puede manejar transacciones de red, reproducir música, realizar I/O de archivos o interactuar con un proveedor de contenido, todo en segundo plano.

## DESARROLLO DE SOFTWARE EN CASCADA VS. ÁGIL

imagen 

# RECOMENDACIONES DE ESTUDIO DE LA PROFESORA

+ Asiste regularmente a las clases del componente teórico y práctico del Itinerario de Aplicaciones Móviles y Sistemas Telemáticos.
+ Participa en clase, en las actividades conjuntamente con la profesora.
+ Investiga pro-activamente, para que aportes con ideas innovadoras.

“Leer y practicar es la mejor forma de aprender los fundamentos teóricos”.
### Ángel Collaguazo 

















