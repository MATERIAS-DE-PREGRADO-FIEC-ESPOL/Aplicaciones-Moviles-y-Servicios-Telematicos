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

Referencias
[Arquitectura de la plataforma](https://developer.android.com/guide/platform?hl=es-419)
[Descripción general de Proyectos](https://developer.android.com/studio/projects?hl=es-419)
[Activity](https://developer.android.com/reference/android/app/Activity#setContentView)
[Cómo interpretar el ciclo de vida de una actividad](https://developer.android.com/guide/components/activities/activity-lifecycle?hl=es-419#java)
