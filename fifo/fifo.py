from collections import deque

# Paso 1: Crear una cola vacía
cola = deque()

# Paso 2: Agregar elementos a la cola
cola.append("A")
cola.append("B")
cola.append("C")

# Paso 3: Mostrar la cola actual
print("Cola actual:", cola)

# Paso 4: Sacar el primer elemento (First In, First Out)
elemento_extraido = cola.popleft()
print("Elemento extraído:", elemento_extraido)

# Paso 5: Mostrar la cola después de extraer un elemento
print("Cola después de extraer:", cola)
