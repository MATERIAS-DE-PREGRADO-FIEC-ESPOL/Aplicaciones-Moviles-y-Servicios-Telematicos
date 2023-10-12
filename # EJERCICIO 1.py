# EJERCICIO 1

#**Objetivo:** A partir de una lista de libros vendidos, su precio y la cantidad de páginas, calcular el total de páginas vendidas.

#Lista de ejemplo: `Libros = ['Harry Potter|35.5|800', 'El Principito|20|120', 'Don Quijote|50|1600']`

#Siguiendo el modelo de la lista, comenzamos recorriendo la lista para obtener los datos

libros = ['Harry Potter|35.5|800', 'El Principito|20|120', 'Don Quijote|50|1600']

totalPaginas = 0 #Será la variable con el resultado

for libro in libros:
  partes = libro.split("|") #Divide la lista de libros por el |, obteniendo asi una lista con los valores, la cual en el primer elemento sería asi partes = [Harry Potter, 35.5, 800]
  paginasLibro = partes[2] #Obtenemos las paginas de la lista anterior
  totalPaginas += int(paginasLibro) #Sumamos las paginas de todos los libros vendidos

print("El total de páginas vendidas es: ", totalPaginas)
  
### EJERCICIO 2

#**Objetivo:** A partir de las colecciones de vehículos, precios, unidades vendidas y descuentos, encontrar el vehículo que generó la mayor venta total.

vehiculos = ["Sedan", "Kia","Carnival","Mazda"]
precios = [20000,15000,30000,50000]
vendidos = [100,200,50,25]
descuentos = [0.1,0.3,0.05,0.01]#Donde 1 es 100%

vehiculoMaximo = "" #variable con el resultado final del nombre del vehiculo
valorMaximo = 0 #variable con el valor maximo de venta 

for i in range(len(vehiculos)):
  venta = precios[i]*vendidos[i]*(1-descuentos[i])
  if venta > valorMaximo:
    valorMaximo = venta
    vehiculoMaximo = vehiculos[i]

print("El vehiculo que en total genero mas ventas es: ", vehiculoMaximo)

### EJERCICIO 3: Gestión de Inventario de un Supermercado con Fechas de Caducidad

#**Objetivo:**

#Se desea gestionar el inventario de un supermercado que tiene productos con fechas de caducidad. Las transacciones disponibles son 'compra' y 'venta'. La entrada de productos en la compra debe registrar la fecha de caducidad. En cada venta, se deben vender los productos que están más cerca de la fecha de caducidad. 

#La lista de transacciones podría verse así: `["compra|leche|10|2024-10-20", "venta|leche|5", "compra|leche|20|2025-12-15"]`. Se pide escribir un programa que maneje este tipo de transacciones y, al final, muestre el inventario con las cantidades y fechas de caducidad.

inventario = {}

# Lista de transacciones
transacciones = ["compra|leche|10|2024-10-20", "venta|leche|5", "compra|leche|20|2025-12-15"]

# Procesar las transacciones
for transaccion in transacciones:
    partes = transaccion.split('|') #divide cada elemento de la lista por el | obtenienod asi cada dato y colocandolo en las siguientes variables:
    accion = partes[0]
    producto = partes[1]
    
    if accion == 'compra':
        cantidad = int(partes[2])
        fecha_caducidad = partes[3]
        
        # Agregar o actualizar el producto en el inventario
        if producto in inventario:
            inventario[producto].append((cantidad, fecha_caducidad))
        else:
            inventario[producto] = [(cantidad, fecha_caducidad)]
    if accion == 'venta':
        cantidad_vendida = int(partes[2])
        
        # Vender productos basados en la fecha de caducidad
        if producto in inventario:
            inventario[producto].sort(key=lambda x: x[1])  # Ordenar por fecha de caducidad utilizando lambda
            cantidad_disponible = sum(item[0] for item in inventario[producto])
            
            if cantidad_disponible >= cantidad_vendida:
                while cantidad_vendida > 0:
                    cantidad, fecha_caducidad = inventario[producto][0]
                    if cantidad <= cantidad_vendida:
                        cantidad_vendida -= cantidad
                        inventario[producto].pop(0)
                    else:
                        inventario[producto][0] = (cantidad - cantidad_vendida, fecha_caducidad)
                        cantidad_vendida = 0
            else:
                print(f"No hay suficientes unidades de {producto} para la venta.")
        else:
            print(f"{producto} no está en el inventario.")

# Mostrar el inventario actualizado
print("Inventario:")
for producto, detalles in inventario.items():
    cantidad_total = sum(item[0] for item in detalles)
    print(f"{producto}: {cantidad_total} unidades")