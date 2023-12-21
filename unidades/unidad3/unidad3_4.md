---
remote_theme: pages-themes/cayman@v0.2.0
---
[Regresar](/Aplicaciones-Moviles-y-Servicios-Telematicos/)

# 3.4📲 Aplicaciones y servicios basados en localización 

Existen algunos trucos para obtener la localización:

+ Utilizando la última ubicación conocida del LocationManager para cualquier proveedor de ubicación.
+ Recuperar esa ubicación en la interfaz de usuario, y para eso simplemente puede transmitir un Intent como si fuera el LocationManager.


<p align="left">
  <img src="../imagenes/unid4_localizacion1.png" alt="tiempo" width="50%">
</p>

<p align="right">
  <img src="../imagenes/unid4_localizacion2.png" alt="tiempo" width="50%">
</p>

Múltiples son las aplicaciones y los servicios basados en localización, que buscan proveer servicios geográficos en tiempo real. A continuación serán enunciados algunos de los más relevantes.

+ **Rescate y salvamento:** En EE.UU. el servicio 911.
+ **Rastreo y navegación:** Navegación avanzada.
+ **Hogar:** Información preventiva sobre los lugares peligrosos.
+ **Privacidad:** DAA “Direct Anonymous Attestation”.
+ **Mensajería:** SIP “Session Initiation Protocol”.
+ **Sector commercial:** RFID “Radio Frequency Identification”.


<p align="center">
  <img src="../imagenes/unid4_localizacion3.jpg" alt="tiempo" width="80%">
</p>

## [INV] Análisis de aplicaciones móviles de rastreo de contactos con sensores embebidos

## 🎯 Objetivo de Aprendizaje

Diseñar aplicaciones que utilicen los sensores embebidos en dispositivos móviles para la entrega de información a los usuarios en tiempo real.

### Actividades
1.Investigar sobre 3 aplicaciones móviles avanzadas que apliquen M2M, incluir detalles de la aplicación móvil. Por ejemplo: flota de buses que utilizan sensores en la batería del bus.
2. Hacer pruebas de usabilidad, por lo menos con 3 aplicaciones móviles de rastreo de contactos, considerando que usen los siguientes sensores embebidos: Bluetooth, GPS. 
Desarrollar una aplicación móvil que active uno de los sensores embebidos (Bluetooth, GPS, cámara).
3. Presentar diapositivas con los resultados de las actividades, incluyendo el enlace del repositorio de GitHub.

## Referencias bibliográficas
https://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ExposureNotification-BluetoothSpecificationv1.2.pdf?1
https://www.technologyreview.com/2020/05/07/1000961/launching-mittr-covid-tracing-tracker/
https://developer.android.com/guide/topics/connectivity/bluetooth
https://developer.android.com/training/camera
https://developer.android.com/guide/topics/sensors

### Protocolos de intercambio de datos
La LPWAN (red de área extensa de baja potencia) es un tipo de red de área extensa de telecomunicaciones inalámbricas diseñada para permitir comunicaciones de largo alcance a baja velocidad de bits entre objetos conectados, como sensores que funcionan con batería.
Existen varias normas y proveedores que compiten en el ámbito de las LPWAN:

+ DASH7
+ Chirp spread spectrum based
+ LoRa
+ Sigfox

**LoRaWAN**

+ La arquitectura de red LoRaWAN® se despliega en una topología de estrella de estrellas en la que las pasarelas retransmiten mensajes entre los dispositivos finales y un servidor de red central. 
+ Las pasarelas están conectadas al servidor de red a través de conexiones IP estándar y actúan como un puente transparente, simplemente convirtiendo los paquetes RF en paquetes IP y viceversa. 
+ Todos los modos permiten la comunicación bidireccional.


<p align="center">
  <img src="../imagenes/unid3.embebido4.png" alt="tiempo" width="100%">
</p>

**Sigfox**
El protocolo Sigfox se centra en: 
+ **Autonomía**. Consumo de energía extremadamente bajo, que permite años de duración de la batería.
+ **Simplicidad**. Sin configuración, solicitud de conexión ni señalización. 
+ **Rentabilidad**. Desde el hardware utilizado en los dispositivos hasta nuestra red, optimizamos cada paso para que sea lo más rentable posible.
+ **Mensajes pequeños**. En la red no se permiten activos ni medios de gran tamaño, sólo notificaciones pequeñas: hasta 12 bytes.

<p align="center">
  <img src="../imagenes/unid3.embebido1.png" alt="tiempo" width="100%">
</p>

**Captura de datos en tiempo real**

+ El aumento de la generación de datos no sólo se ha limitado a las empresas o grandes organizaciones. 

+ Los individuos también están generando más datos personales, conocidos como rastros digitales.

+ A menudo, los individuos pueden publicar y acceder a información histórica y en tiempo real sobre su entorno, intereses y otra variedad de temas.


<p align="right">
  <img src="../imagenes/unid3.embebido9.png" alt="tiempo" width="60%">
</p>

+ En estas aplicaciones, los sistemas embebidos deben proporcionar predictibilidad tanto en el tiempo de respuesta como en la calidad de los resultados. Esta característica los eleva a la categoría de sistemas en tiempo real. En estos sistemas, la validez de los resultados viene dada no sólo por su corrección, sino también por su puntualidad. Es decir, existen algunas restricciones que limitan el tiempo de su funcionamiento.

+ En un sistema de monitorización remota en tiempo real, los dispositivos conectados recopilan datos médicos y otros datos sanitarios y utilizan una red Wi-Fi, zigbee o celular para transferir esos datos a un médico o almacenarlos en la nube, donde pueden acceder a ellos médicos, cuidadores, pacientes y asesores.

**Captura de datos en tiempo real**

## Visualización de datos sensados

<p align="center">
  <img src="../imagenes/unid4_visualizacion_datos2.jpg" alt="tiempo" width="100%">
</p>

Referencia: https://github.com/AnyChart/AnyChart-Android


https://github.com/AnyChart/AnyChart-Android
http://www.estadisticaparatodos.es/taller/graficas/cajas.html

**iOS - Steps**       
**Android -Steps**    
**Android - Stress**


<p align="center">
  <img src="../imagenes/unid4_visualizacion_datos3.jpg" alt="tiempo" width="100%">
</p>

http://appdesignbook.com/es/contenidos/patrones-interaccion-moviles/


Tipos de sistemas en tiempo real basados en restricciones temporales:
+ Duros 
+ Firme
+ Suave

Modelo de referencia de sistema en tiempo real: Nuestro modelo de referencia se caracteriza por tres elementos:

+ Un modelo de carga de trabajo
+ Un modelo de recursos
+ Algoritmos

Otro factor que se debe tener en cuenta para decidir si el sistema es fiable para el uso en tiempo real, además de la latencia incurrida en el manejo de eventos externos, es la "variación" en esta latencia, es decir, para que un sistema se considere fiable para la aplicación en tiempo real, tiene que haber un límite superior sobre cuánta variación en la latencia puede ser tolerada por la aplicación en tiempo real. Hemos analizado nuestras mediciones experimentales con estos criterios en mente.

**Detección y consumo de batería

+ Conseguir un bajo consumo de energía en cualquier sistema integrado es importante. Los sistemas embebidos en aplicaciones espaciales son un ejemplo en el que existe un presupuesto de energía definido, y normalmente bajo, que debe cumplirse. 

+ Incluso en aplicaciones en las que a primera vista podría parecer que el consumo de energía es una cuestión menos prioritaria, como en las aplicaciones de automoción, el creciente uso de sistemas embebidos para sustituir a los sistemas mecánicos tiene un gran impacto en el consumo de energía en reposo.

## Utilización de los recursos de almacenamiento y procesamiento para la detección

+ Esta sección ofrece un breve resumen de las aplicaciones de teledetección que utilizan entornos de computación en nube, así como un estudio de caso más detallado.
+ El proyecto Matsu es un proyecto de código abierto para el procesamiento de imágenes de satélite utilizando una nube comunitaria. Este proyecto, una colaboración entre la NASA y el Open Cloud Consortium (OCC), se ha desarrollado para procesar datos del satélite EO-1 de la NASA y desarrollar tecnología de código abierto para el procesamiento público de imágenes de satélite basado en la nube. La mayoría de los cálculos se completaron utilizando un marco Hadoop que se ejecuta en 9 nodos de computación con 54 núcleos de computación AQ4 y 352 GB de RAM.





```