---
remote_theme: pages-themes/cayman@v0.2.0
---
[Regresar](/Aplicaciones-Moviles-y-Servicios-Telematicos/)

# Unidad 2 Recursos en red para aplicaciones avanzadas

## 🎯 Objetivo de Aprendizaje
Al finalizar la clase el estudiante será capaz de:
- Demostrar el acceso a los recursos en red para la programación de aplicaciones móviles avanzadas.

# 2.2 Programación de sockets
- [Programación de sockets](#sockets)
- [Arquitectura general de los sistemas IoT utilizados en proyectos académicos](#arquitectura)
- [Taxonomía de problemas en el desarrollo de sistemas IoT](#taxonomia)
- [Referencias](#referencias)

<a name="sockets"> </a>

# 📲 Sockets

+ Define las reglas que un programa ha de seguir para utilizar los servicios del nivel de transporte en una red TCP/IP. Esta interfaz se basa en el concepto de socket. 
+ Un socket es el punto final de una comunicación bidireccional entre dos programas que intercambian información a través de Internet.
+ Un socket se identifica por la dirección IP del dispositivo, más un número de puerto de 16 bits. 
+ Una conexión está determinada por un par de sockets, uno en cada extremo de la conexión. Existen dos tipos de socket: socket stream y socket datagram.
+ Permisos para el uso de internet por medio del teléfono celular en app > manifests > AndroidManifest.xml: 
<uses-permission android:name="android.permission.INTERNET"/>

https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml


<a name="arquitectura"> </a>

# 📲 Arquitectura general de los sistemas IoT utilizados en proyectos académicos

<p align="center">
  <img src="../imagenes/unidad2_2_arquitectura_sistemas_iot.jpg" alt="arquitectura" width="100%">
</p>

1. Physical layer: This layer corresponds to things that become intelligent by being programmed, integrating hardware development boards, sensors, and actuators to interact with the real world. Arduino and ThinkXtra Sigfox, iButton devices
with GPS sensors, and Suntech with GPS sensors were used in the AMST projects, whereas ESP8266 and ESP32 WiFi
modules were used in the PST projects. Weight sensors (HX711 sensor), gas (MQ-2 sensor), sound (KY-038 sensor), air quality
(MQ-135 sensor), and temperature and humidity (DHT11 sensor) were used in both courses.
2. Edge layer: This layer allows routing of the sensed data originating from the IoT devices from the physical layer to the cloud services
layer without manipulating them. This layer is based on communication protocols such as HTTP, which allows data to be sent
through wired or wireless technologies such as 0G, 3 G, 5 G, LTE, and IEEE 802.11.
3. Cloud services layer: This layer works bi-directionally with the application layer and is responsible for the storage and processing of
data required by software applications. Google Cloud services such as Firebase were used in some of the projects, and
Heroku, among others.
4. Application layer: This layer allows the monitoring of information by end users through combined and analyzed data, which can
contribute to decision-making. For AMST course projects, it is necessary to develop a mobile application, whereas, for PST,
these applications can be web or mobile depending on the type of project. The tools used for the development of mobile applications
were the Android Studio integrated development environment (IDE), and for web applications, the execution environment for
JavaScript Node.js, and the React library.


<a name="taxonomia"> </a>

# 📲 Taxonomía de problemas en el desarrollo de sistemas IoT
<p align="center">
  <img src="../imagenes/unidad2_2_taxonomy_iot.jpg" alt="taxonomy" width="100%">
</p>

<a name="referencias"> </a>

# 📲 Referencias
[An activity-based approach for the early identification and resolution of problems in the development of IoT systems in academic projects
](https://www.sciencedirect.com/science/article/pii/S2542660523002524)