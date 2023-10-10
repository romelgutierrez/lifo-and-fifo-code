import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Definición de la clase Memoria
class Memoria:
    def __init__(self, capacidad):
        # Inicializa la memoria con una capacidad dada
        self.capacidad = capacidad
        # Lista para rastrear los procesos en memoria
        self.procesos_en_memoria = []

    def asignar_proceso(self, proceso):
        # Verifica si el proceso ya está en memoria
        if proceso not in self.procesos_en_memoria:
            # Si la memoria está llena, libera el primer proceso (FIFO)
            if len(self.procesos_en_memoria) >= self.capacidad:
                proceso_a_liberar = self.procesos_en_memoria.pop(0)
                print(f"Liberando memoria para {proceso_a_liberar}")
            # Asigna el nuevo proceso a la memoria
            print(f"Asignando memoria para {proceso}")
            self.procesos_en_memoria.append(proceso)

    def mostrar_estado(self):
        # Muestra el estado actual de la memoria en forma de tabla
        tabla = PrettyTable()
        tabla.field_names = ["Procesos en memoria", "Espacios disponibles"]
        tabla.add_row([', '.join(self.procesos_en_memoria), self.capacidad - len(self.procesos_en_memoria)])
        print(tabla)

# Función principal
def main():
    # Tamaño de la memoria
    tamano_memoria = 5
    # Crea una instancia de la memoria
    memoria = Memoria(tamano_memoria)

    # Lista de procesos
    procesos = ["luis", "sara", "romel", "raul", "eloy", "pol", "javier"]

    # Asignar procesos a la memoria
    for proceso in procesos:
        memoria.asignar_proceso(proceso)
        memoria.mostrar_estado()

    # Graficar el resultado
    plt.bar(memoria.procesos_en_memoria, [1] * len(memoria.procesos_en_memoria))
    plt.xlabel("Procesos en Memoria")
    plt.ylabel("Bloques de Memoria")
    plt.title("Asignación de Memoria con FIFO")
    plt.show()

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
