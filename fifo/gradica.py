import matplotlib.pyplot as plt

# Datos para el gráfico
elementos = ["A", "B", "C"]

# Crear un gráfico de barras horizontal
plt.barh(elementos, range(len(elementos)))

# Configuración del gráfico
plt.xlabel("Posición en la cola")
plt.ylabel("Elementos")
plt.title("Representación gráfica de una cola FIFO")

# Mostrar el gráfico
plt.show()
