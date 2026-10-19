class Nodo:
    def _init_(self, data=None, next=None):
        self.data = data
        self.next = next

class Lista_enlazada:
    def _init_(self):
        self.head = None

    def agregar_al_inicio(self, data):
        self.head = Nodo(data=data, next=self.head)

    def agregar_al_final(self, data):
        if not self.head:
            self.head = Nodo(data=data)
            return
        temporal = self.head
        while temporal.next:
            temporal = temporal.next
        temporal.next = Nodo(data=data)

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=" --> ")
            node = node.next
        print("None")

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def Mover_dato(self, nombre_jugador, posiciones, direccion):
        # Caso 1: Lista vacía
        if not self.head:
            print(f"Error: La lista está vacía. No se puede mover a {nombre_jugador}.")
            return False
        
        # Caso 2: Buscar el jugador en la lista
        if not self.contains(nombre_jugador):
            print(f"Error: El jugador {nombre_jugador} no existe en la lista.")
            return False
        
        # Caso 3: Validar dirección
        if direccion.lower() not in ["adelante", "atras"]:
            print("Error: La dirección debe ser 'adelante' o 'atras'.")
            return False
        
        # Caso 4: Validar que posiciones sea un número positivo
        if posiciones <= 0:
            print("Error: El número de posiciones debe ser mayor que 0.")
            return False
        
        # Encontrar la posición actual del jugador
        current = self.head
        posicion_actual = 0
        while current and current.data != nombre_jugador:
            current = current.next
            posicion_actual += 1
        
        # Determinar la nueva posición
        if direccion.lower() == "atras":
            nueva_posicion = max(0, posicion_actual - posiciones)  # No puede ser negativa
        else:  # direccion == "atras"
            # Primero contamos el total de elementos en la lista
            total_elementos = 0
            temp = self.head
            while temp:
                total_elementos += 1
                temp = temp.next
            nueva_posicion = min(posicion_actual + posiciones, total_elementos - 1)
        
        # Si la posición no cambia, no hacemos nada
        if nueva_posicion == posicion_actual:
            print(f"El jugador {nombre_jugador} permanece en la misma posición.")
            return True
        
        # Eliminar el nodo del jugador de su posición actual
        if posicion_actual == 0:  # Es la cabeza
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(posicion_actual - 1):
                prev = prev.next
            prev.next = prev.next.next
        
        # Insertar el nodo del jugador en la nueva posición
        if nueva_posicion == 0:  # Insertar al inicio
            self.agregar_al_inicio(nombre_jugador)
        else:
            # Llegar al nodo anterior a la nueva posición
            temp = self.head
            for _ in range(nueva_posicion - 1):
                temp = temp.next
            nuevo_nodo = Nodo(data=nombre_jugador, next=temp.next)
            temp.next = nuevo_nodo
        
        print(f"Jugador {nombre_jugador} movido {posiciones} posiciones hacia {direccion}.")
        return True


# Ejemplos de uso

# Crear una lista de jugadores
def crear_lista_ejemplo():
    lista = Lista_enlazada()
    lista.agregar_al_final("Maria")
    lista.agregar_al_final("Juan")
    lista.agregar_al_final("Pedro")
    lista.agregar_al_final("Ana")
    lista.agregar_al_final("Carlos")
    return lista

print("=== Ejemplo 1: Lista normal ===")
lista = crear_lista_ejemplo()
print("Lista inicial:")
lista.print_list()
print("\nMoviendo a Juan 1 posición hacia adelante:")
lista.Mover_dato("Juan", 1, "adelante")
lista.print_list()
print("\nMoviendo a Pedro 2 posiciones hacia atras:")
lista.Mover_dato("Pedro", 2, "atras")
lista.print_list()

print("\n=== Ejemplo 2: Lista vacía ===")
lista_vacia = Lista_enlazada()
print("Lista vacía:")
lista_vacia.print_list()
lista_vacia.Mover_dato("Juan", 1, "adelante")

print("\n=== Ejemplo 3: Jugador inexistente ===")
lista = crear_lista_ejemplo()
lista.Mover_dato("Luis", 1, "adelante")

print("\n=== Ejemplo 4: Mover jugador al inicio de la lista ===")
lista = crear_lista_ejemplo()
print("Lista inicial:")
lista.print_list()
print("\nMoviendo a Carlos 4 posiciones hacia adelante:")
lista.Mover_dato("Carlos", 4, "adelante")
lista.print_list()

print("\n=== Ejemplo 5: Mover jugador al final de la lista ===")
lista = crear_lista_ejemplo()
print("Lista inicial:")
lista.print_list()
print("\nMoviendo a Maria 4 posiciones hacia atras:")
lista.Mover_dato("Maria", 4, "atras")
lista.print_list()

print("\n=== Ejemplo 6: Dirección incorrecta ===")
lista = crear_lista_ejemplo()
lista.Mover_dato("Juan", 1, "izquierda")

print("\n=== Ejemplo 7: Número de posiciones negativo o cero ===")
lista = crear_lista_ejemplo()
lista.Mover_dato("Juan", 0, "adelante")

print("\n=== Ejemplo 8: Mover más allá de los límites ===")
lista = crear_lista_ejemplo()
print("Lista inicial:")
lista.print_list()
print("\nMoviendo a Maria 10 posiciones hacia adelante (debería quedarse al inicio):")
lista.Mover_dato("Maria", 10, "adelante")
lista.print_list()
print("\nMoviendo a Carlos 10 posiciones hacia atras (debería quedarse al final):")
lista.Mover_dato("Carlos", 10, "atras")
lista.print_list()