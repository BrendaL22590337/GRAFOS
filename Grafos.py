# grafo_simulador.py
# Programa para manejar un grafo simple no dirigido

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, v):
        if v not in self.grafo:
            self.grafo[v] = []
            print(f"Vértice '{v}' agregado.")
        else:
            print("El vértice ya existe.")

    def agregar_arista(self, v1, v2):
        if v1 not in self.grafo or v2 not in self.grafo:
            print("Ambos vértices deben existir.")
            return
        if v2 not in self.grafo[v1]:
            self.grafo[v1].append(v2)
            self.grafo[v2].append(v1)
            print(f"Arista agregada entre '{v1}' y '{v2}'.")
        else:
            print("La arista ya existe.")

    def mostrar_grafo(self):
        print("\n--- Grafo actual ---")
        for vertice, adyacentes in self.grafo.items():
            print(f"{vertice} → {adyacentes}")
        print("--------------------")

    def recorrido_BFS(self, inicio):
        if inicio not in self.grafo:
            print("El vértice no existe en el grafo.")
            return
        visitados = []
        cola = [inicio]

        while cola:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.append(actual)
                for vecino in self.grafo[actual]:
                    if vecino not in visitados:
                        cola.append(vecino)
        print(f"Recorrido BFS desde '{inicio}': {visitados}")

    def recorrido_DFS(self, inicio, visitados=None):
        if visitados is None:
            visitados = []
        if inicio not in self.grafo:
            print(" El vértice no existe en el grafo.")
            return
        visitados.append(inicio)
        for vecino in self.grafo[inicio]:
            if vecino not in visitados:
                self.recorrido_DFS(vecino, visitados)
        return visitados


def menu():
    grafo = Grafo()
    while True:
        print("\n===== MENÚ GRAFO =====")
        print("1. Agregar vértice")
        print("2. Agregar arista")
        print("3. Mostrar grafo")
        print("4. Recorrido BFS")
        print("5. Recorrido DFS")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            v = input("Ingresa nombre del vértice: ")
            grafo.agregar_vertice(v)
        elif opcion == '2':
            v1 = input("Vértice 1: ")
            v2 = input("Vértice 2: ")
            grafo.agregar_arista(v1, v2)
        elif opcion == '3':
            grafo.mostrar_grafo()
        elif opcion == '4':
            inicio = input("Vértice inicial para BFS: ")
            grafo.recorrido_BFS(inicio)
        elif opcion == '5':
            inicio = input("Vértice inicial para DFS: ")
            resultado = grafo.recorrido_DFS(inicio)
            if resultado:
                print(f" Recorrido DFS desde '{inicio}': {resultado}")
        elif opcion == '6':
            print("Saliendo del programa de Grafos...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
