class Producto:
    def __init__(self,nombre,codigo,valor):
        self.nombre = nombre
        self.codigo = codigo
        self.valor = valor
        self.siguiente = None
#Fin de la Clase Nodo


class ListaSE:
    def __init__(self):
        self.cabeza = None
        self.total = 0

    def agregar(self,nombre,codigo,valor):
        nuevo_nodo = Producto(nombre,codigo,valor)
        self.total += valor
        if self.cabeza is None: 
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return

    def buscar(self,valor):
         if self.cabeza is None:
             return "Inventario Vacio"
         else:
             temp = self.cabeza
             while temp is not None:
                 if temp.codigo == valor:
                     return f"Elemento encontrado: \n Nombre:{temp.nombre}\n Cantidad:{self.contarProducto(valor)}\n Precio unidad: ${temp.valor}"
                 temp = temp.siguiente

             return f"Elemento {valor} no encontrado"

    def imprimeLista(self):
        if self.cabeza is None:
            return
        else:
            temp = self.cabeza
            while temp is not None:
                print(f"{temp.nombre}: ${temp.valor}")
                temp = temp.siguiente

    def contarProductos(self):
        if self.cabeza is None:
            return "La lista se encuentra vacia"
        else:
            count = 0
            temp = self.cabeza
            while temp is not None:
                count +=1
                temp = temp.siguiente
            return count

    def contarProducto(self,codigo=None):
        if self.cabeza is None:
            return "La lista se encuentra vacia"
        else:
            count = 0
            temp = self.cabeza
            if codigo is not None:
                while temp is not None:
                    if codigo == temp.codigo:
                        count +=1
                    temp = temp.siguiente
            return count

    def listaVacia(self):
        if self.cabeza is None:
            return "Lista Vacia"
        else:
            return "Lista Llena"

    def calcularValorTotal(self):
        self.total = 0
        if self.cabeza is None:
            return self.total
        else:
            temp = self.cabeza
            while temp.siguiente is not None:
                self.total += temp.valor
                temp = temp.siguiente
            return self.total


lista = ListaSE()

print(lista.listaVacia())

lista.agregar("Medias", 4, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Camisa", 1, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Pantalon", 2, 1500)
lista.agregar("Zapato", 3, 1500)
print(lista.listaVacia())

print(f"Productos Totales: {lista.contarProductos()}")

print(f"Productos por codigo: {lista.contarProducto(2)}")

print()
lista.imprimeLista()
print()

print(lista.buscar(2))

print(f"El valor total de todos los productos: ${lista.calcularValorTotal()}")
