class NodoPrenda:
    def __init__(self, id_prenda, tipo_prenda):
        self.id_prenda = id_prenda
        self.tipo_prenda = tipo_prenda
        self.conexiones = {}

    def agregar_conexion(self, nodo, peso=0):
        self.conexiones[nodo] = peso

    def obtener_conexiones(self):
        return self.conexiones.keys()

    def obtener_id(self):
        return self.id_prenda

    def obtener_tipo(self):
        return self.tipo_prenda

    def obtener_peso(self, nodo):
        return self.conexiones[nodo]

class GrafoInventario:
    def __init__(self):
        self.nodos_prendas = {}
        self.numero_nodos = 0
        self.contador_prendas = {
            'camisas': 0,
            'pantalones': 0,
            'chaquetas': 0,
            'faldas': 0
        }

    def agregar_nodo(self, id_prenda, tipo_prenda):
        self.numero_nodos += 1
        nuevo_nodo = NodoPrenda(id_prenda, tipo_prenda)
        self.nodos_prendas[id_prenda] = nuevo_nodo
        self.contador_prendas[tipo_prenda] += 1
        print(f"Prenda {id_prenda} de tipo {tipo_prenda} agregada al grafo.")

    def eliminar_nodo(self, id_prenda):
        if id_prenda in self.nodos_prendas:
            tipo_prenda = self.nodos_prendas[id_prenda].obtener_tipo()
            del self.nodos_prendas[id_prenda]
            self.contador_prendas[tipo_prenda] -= 1
            print(f"Prenda {id_prenda} eliminada del grafo.")
        else:
            print(f"La prenda {id_prenda} no se encontró en el grafo.")

    def agregar_arista(self, de_prenda, a_prenda, peso=0):
        if de_prenda in self.nodos_prendas and a_prenda in self.nodos_prendas:
            self.nodos_prendas[de_prenda].agregar_conexion(self.nodos_prendas[a_prenda], peso)
            print(f"Arista agregada de {de_prenda} a {a_prenda} con peso {peso}.")
        else:
            print(f"Una o ambas prendas no se encontraron en el grafo.")

    def buscar_prenda(self, tipo_prenda):
        print(f"Hay {self.contador_prendas[tipo_prenda]} prendas de tipo {tipo_prenda} en el inventario.")

    def mostrar_grafo(self):
        for nodo in self:
            print(f"Prenda {nodo.obtener_id()} ({nodo.obtener_tipo()}) está conectada con:")
            for conexion in nodo.obtener_conexiones():
                print(f"  - {conexion.obtener_id()} ({conexion.obtener_tipo()})")

    def __iter__(self):
        return iter(self.nodos_prendas.values())

def menu():
    grafo = GrafoInventario()
    while True:
        print("\nMenú Principal:")
        print("1. Ingresar Prenda")
        print("2. Eliminar Prenda")
        print("3. Buscar Prenda")
        print("4. Mostrar Grafo")
        print("5. Agregar Conexión entre Prendas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nTipos de Prendas:")
            print("1. Camisa")
            print("2. Pantalón")
            print("3. Chaqueta")
            print("4. Falda")
            tipo_opcion = input("Seleccione el tipo de prenda: ")
            tipo_prenda = ''
            if tipo_opcion == '1':
                tipo_prenda = 'camisas'
            elif tipo_opcion == '2':
                tipo_prenda = 'pantalones'
            elif tipo_opcion == '3':
                tipo_prenda = 'chaquetas'
            elif tipo_opcion == '4':
                tipo_prenda = 'faldas'
            else:
                print("Opción no válida.")
                continue
            id_prenda = input("Ingrese el ID de la prenda: ")
            grafo.agregar_nodo(id_prenda, tipo_prenda)

        elif opcion == '2':
            id_prenda = input("Ingrese el ID de la prenda a eliminar: ")
            grafo.eliminar_nodo(id_prenda)

        elif opcion == '3':
            print("\nTipos de Prendas:")
            print("1. Camisa")
            print("2. Pantalón")
            print("3. Chaqueta")
            print("4. Falda")
            tipo_opcion = input("Seleccione el tipo de prenda: ")
            tipo_prenda = ''
            if tipo_opcion == '1':
                tipo_prenda = 'camisas'
            elif tipo_opcion == '2':
                tipo_prenda = 'pantalones'
            elif tipo_opcion == '3':
                tipo_prenda = 'chaquetas'
            elif tipo_opcion == '4':
                tipo_prenda = 'faldas'
            else:
                print("Opción no válida.")
                continue
            grafo.buscar_prenda(tipo_prenda)

        elif opcion == '4':
            grafo.mostrar_grafo()

        elif opcion == '5':
            de_prenda = input("Ingrese el ID de la prenda de origen: ")
            a_prenda = input("Ingrese el ID de la prenda de destino: ")
            peso = input("Ingrese el peso de la conexión (opcional, por defecto 0): ")
            if peso == '':
                peso = 0
            else:
                peso = int(peso)
            grafo.agregar_arista(de_prenda, a_prenda, peso)

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
