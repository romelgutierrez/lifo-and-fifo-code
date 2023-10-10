# Paso 1: Crear una pila vacía
pila = []

# Paso 2: Agregar elementos a la pila
pila.append("A")
pila.append("B")
pila.append("C")

# Paso 3: Mostrar la pila actual
print("Pila actual:", pila)

# Paso 4: Sacar el último elemento (Last In, First Out)
elemento_extraido = pila.pop()
print("Elemento extraído:", elemento_extraido)

# Paso 5: Mostrar la pila después de extraer un elemento
print("Pila después de extraer:", pila)


import matplotlib.pyplot as plt

# Datos para el gráfico
elementos = ["A", "B", "C"]

# Crear un gráfico de barras horizontal
plt.barh(elementos, range(len(elementos)))

# Configuración del gráfico
plt.xlabel("Posición en la pila")
plt.ylabel("Elementos")
plt.title("Representación gráfica de una pila LIFO")

# Mostrar el gráfico
plt.show()
