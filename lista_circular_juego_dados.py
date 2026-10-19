import random
import os
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaCircular:
    def __init__(self):
        """Inicializa la lista circular vacía."""
        self.head = None

    def esta_vacia(self):
        """Verifica si la lista circular está vacía."""
        return self.head is None

    def longitud(self):
        """Calcula la longitud de la lista circular."""
        if self.esta_vacia():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def imprimir(self):
        """Imprime los elementos de la lista circular."""
        if self.esta_vacia():
            print("La lista está vacía.")
            return
        cur = self.head
        print(self.obtener_nombre(cur.data), end="")
        while cur.next != self.head:
            cur = cur.next
            print(" --> ", self.obtener_nombre(cur.data), end="")
        print()

    def obtener_nombre(self, data):
        """Obtiene el nombre del jugador a partir de los datos."""
        return data.split(",")[0]

    def agregar_ultimo(self, data):
        """Agrega un nuevo nodo al final de la lista circular."""
        node = Node(data)
        if self.esta_vacia():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def eliminar_jugador(self, jugador_node):
        """Elimina un jugador de la lista circular."""
        if self.esta_vacia():
            return False

        if self.head == jugador_node:
            if self.head.next == self.head:
                self.head = None
                return True

            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            self.head = self.head.next
            cur.next = self.head
            return True

        cur = self.head
        while cur.next != jugador_node and cur.next != self.head:
            cur = cur.next

        if cur.next == jugador_node:
            cur.next = jugador_node.next
            return True

        return False

    def mover_al_final(self, jugador_node):
        """Mueve un jugador al final de la lista."""
        if self.esta_vacia() or self.longitud() <= 1:
            return False

        if self.head.next == self.head:
            return True

        cur = self.head
        ultimo = None
        while cur.next != self.head:
            ultimo = cur
            cur = cur.next

        if cur == jugador_node:
            return True

        if self.head == jugador_node:
            self.head = self.head.next
            cur.next = jugador_node
            jugador_node.next = self.head
            return True

        prev = self.head
        while prev.next != jugador_node and prev.next != self.head:
            prev = prev.next

        if prev.next == jugador_node:
            prev.next = jugador_node.next
            cur.next = jugador_node
            jugador_node.next = self.head
            return True

        return False

    def inicializar_jugadores(self):
        """Inicializa jugadores con nombres predefinidos."""
        nombres = "Cristiano Ronaldo, Lionel Messi, Kylian Mbappé, Neymar Jr., Robert Lewandowski"
        for nombre in nombres.split(", "):
            self.agregar_ultimo(nombre + ", 0, False")
        print("Jugadores inicializados con nombres arbitrarios.")

    def lanzar_dados(self):
        """Simula el lanzamiento de dos dados."""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1, dado2

    def mostrar_estado_jugadores(self):
        """Muestra el estado actual de todos los jugadores."""
        if self.esta_vacia():
            print("No hay jugadores en la lista.")
            return

        print("\n--- ESTADO DE LOS JUGADORES ---")
        print("Nombre\t\t\tAcumulado\tEliminado")
        print("-" * 50)

        cur = self.head
        while True:
            nombre, acumulado, eliminado = cur.data.split(", ")
            estado = "Sí" if eliminado == "True" else "No"
            print(f"{nombre}\t\t{acumulado}\t\t{estado}")
            cur = cur.next
            if cur == self.head:
                break
        print("-" * 50)

    def jugar(self):
        """Implementa la lógica del juego."""
        if self.esta_vacia():
            print("No hay jugadores para jugar.")
            return

        print("\n¡Comienza el juego de dados!")
        self.mostrar_estado_jugadores()

        turno = 1
        cur = self.head
        jugadores_activos = self.longitud()

        while jugadores_activos > 1:
            print(f"\n--- TURNO {turno} ---")

            nombre, acumulado, eliminado = cur.data.split(", ")

            if eliminado == "True":
                cur = cur.next
                continue

            print(f"Turno de: {nombre}")
            input("Presione Enter para lanzar los dados...")

            dado1, dado2 = self.lanzar_dados()
            suma = dado1 + dado2

            print(f"Dado 1: {dado1}")
            print(f"Dado 2: {dado2}")
            print(f"Suma: {suma}")

            acumulado = str(int(acumulado) + suma)
            cur.data = nombre + ", " + acumulado + ", " + eliminado

            if dado1 == dado2:
                print(f"¡{nombre} ha sacado dobles! ¡ES EL GANADOR!")
                return nombre
            elif suma >= 10:
                print(f"¡{nombre} ha sido eliminado! (Suma >= 10)")
                cur.data = nombre + ", " + acumulado + ", True"
                jugadores_activos -= 1
                if jugadores_activos <= 1:
                    break
            elif suma == 7:
                print(f"{nombre} sacó 7. Se mueve al final de la lista.")
                temp = cur
                cur = cur.next
                self.mover_al_final(temp)
                turno += 1
                time.sleep(1)
                continue

            print(f"Acumulado de {nombre}: {acumulado}")

            if jugadores_activos > 1:
                opcion = input("\n¿Desea continuar el juego? (s/n): ").lower()
                if opcion == 'n':
                    return None

            cur = cur.next
            turno += 1

            time.sleep(0.5)

        cur = self.head
        while True:
            nombre, acumulado, eliminado = cur.data.split(", ")
            if eliminado == "False":
                return nombre
            cur = cur.next
            if cur == self.head:
                break

        return None

    def determinar_ganador_por_puntos(self):
        """Si se termina el juego sin ganador por dobles, gana quien tenga menos puntos."""
        if self.esta_vacia():
            return None, 0

        min_puntos = float('inf')
        ganador = None

        cur = self.head
        while True:
            nombre, acumulado, eliminado = cur.data.split(", ")
            if eliminado == "False" and int(acumulado) < min_puntos:
                min_puntos = int(acumulado)
                ganador = nombre
            cur = cur.next
            if cur == self.head:
                break

        return ganador, min_puntos
