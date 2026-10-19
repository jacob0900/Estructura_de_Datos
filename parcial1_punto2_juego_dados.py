import random
import os
import time

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaCircular(object):
    def __init__(self):
        # Inicializa la lista circular vacía
        self.head = None

    def esta_vacia(self):
        # Verifica si la lista circular está vacía
        return self.head is None

    def longitud(self):
        # Calcula la longitud de la lista circular
        if self.esta_vacia():
            return 0
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def imprimir(self):
        # Imprime los elementos de la lista circular
        if self.esta_vacia():
            return
        cur = self.head
        print(cur.data[0], end="")
        while cur.next != self.head:
            cur = cur.next
            print(" --> ", cur.data[0], end="")
        print()

    def agregar_ultimo(self, data):
        # Agrega un nuevo nodo al final de la lista circular
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
        # Elimina un jugador de la lista circular
        if self.esta_vacia():
            return False
            
        if self.head == jugador_node:
            # Si es el nodo cabeza
            if self.head.next == self.head:
                # Si es el único nodo
                self.head = None
                return True
            
            # Encontrar el último nodo que apunta a la cabeza
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            
            # Actualizar la cabeza y el apuntador del último nodo
            self.head = self.head.next
            cur.next = self.head
            return True
        
        # Buscar el nodo anterior al que queremos eliminar
        cur = self.head
        while cur.next != jugador_node and cur.next != self.head:
            cur = cur.next
            
        # Si encontramos el nodo a eliminar
        if cur.next == jugador_node:
            cur.next = jugador_node.next
            return True
            
        return False

    def mover_al_final(self, jugador_node):
        # Mueve un jugador al final de la lista
        if self.esta_vacia() or self.longitud() <= 1:
            return False
            
        # Si hay un solo nodo, no hay nada que mover
        if self.head.next == self.head:
            return True
            
        # Si el nodo a mover ya es el último, no hacer nada
        cur = self.head
        ultimo = None
        while cur.next != self.head:
            ultimo = cur
            cur = cur.next
        
        if cur == jugador_node:
            return True  # Ya está al final
        
        # Si el nodo a mover es la cabeza
        if self.head == jugador_node:
            # Actualizar la cabeza
            self.head = self.head.next
            # El último apunta al nuevo nodo al final
            cur.next = jugador_node
            # El nuevo nodo al final apunta a la cabeza
            jugador_node.next = self.head
            return True
        
        # Encontrar el nodo anterior al que queremos mover
        prev = self.head
        while prev.next != jugador_node and prev.next != self.head:
            prev = prev.next
            
        # Si encontramos el nodo a mover
        if prev.next == jugador_node:
            # Sacar el nodo de su posición actual
            prev.next = jugador_node.next
            # Insertar al final
            cur.next = jugador_node
            jugador_node.next = self.head
            return True
            
        return False

    def inicializar_jugadores(self):
        # Usar nombres predefinidos para los jugadores
        nombres = ["Cristiano Ronaldo", "Lionel Messi", "Kylian Mbappé", "Neymar Jr.", "Robert Lewandowski"]
        for nombre in nombres:
            # Cada jugador tiene [nombre, acumulado, eliminado]
            self.agregar_ultimo([nombre, 0, False])
        print("Jugadores inicializados con nombres arbitrarios.")

    def lanzar_dados(self):
        # Simula el lanzamiento de dos dados
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1, dado2

    def mostrar_estado_jugadores(self):
        # Muestra el estado actual de todos los jugadores
        if self.esta_vacia():
            print("No hay jugadores en la lista.")
            return
            
        print("\n--- ESTADO DE LOS JUGADORES ---")
        print("Nombre\t\t\tAcumulado\tEliminado")
        print("-" * 50)
        
        cur = self.head
        while True:
            nombre, acumulado, eliminado = cur.data
            estado = "Sí" if eliminado else "No"
            print(f"{nombre}\t\t{acumulado}\t\t{estado}")
            cur = cur.next
            if cur == self.head:
                break
        print("-" * 50)

    def jugar(self):
        # Implementa la lógica del juego
        if self.esta_vacia():
            print("No hay jugadores para jugar.")
            return
            
        print("\n¡Comienza el juego de dados!")
        self.mostrar_estado_jugadores()
        
        turno = 1
        cur = self.head
        jugadores_activos = self.longitud()
        
        while jugadores_activos > 1:
            # Limpiar la pantalla para sistemas compatibles (opcional)
            # os.system('cls' if os.name == 'nt' else 'clear')
            
            print(f"\n--- TURNO {turno} ---")
            
            # Mostrar jugador actual
            nombre, acumulado, eliminado = cur.data
            
            # Si el jugador está eliminado, pasar al siguiente
            if eliminado:
                cur = cur.next
                continue
                
            print(f"Turno de: {nombre}")
            input("Presione Enter para lanzar los dados...")
            
            # Lanzar dados
            dado1, dado2 = self.lanzar_dados()
            suma = dado1 + dado2
            
            print(f"Dado 1: {dado1}")
            print(f"Dado 2: {dado2}")
            print(f"Suma: {suma}")
            
            # Actualizar el acumulado
            cur.data[1] += suma
            
            # Verificar reglas
            if dado1 == dado2:
                print(f"¡{nombre} ha sacado dobles! ¡ES EL GANADOR!")
                return nombre  # Terminar el juego con un ganador
            elif suma >= 10:
                print(f"¡{nombre} ha sido eliminado! (Suma >= 10)")
                cur.data[2] = True  # Marcar como eliminado
                jugadores_activos -= 1
                if jugadores_activos <= 1:
                    break  # Terminar si solo queda un jugador
            elif suma == 7:
                print(f"{nombre} sacó 7. Se mueve al final de la lista.")
                temp = cur
                cur = cur.next  # Avanzar antes de mover
                self.mover_al_final(temp)
                # No avanzar cur nuevamente ya que ya lo hicimos
                turno += 1
                time.sleep(1)  # Pausa breve para leer el mensaje
                continue
            
            # Mostrar acumulado actual
            print(f"Acumulado de {nombre}: {cur.data[1]}")
            
            # Opción para finalizar el juego
            if jugadores_activos > 1:
                opcion = input("\n¿Desea continuar el juego? (s/n): ").lower()
                if opcion == 'n':
                    return None  # Terminar sin ganador por dobles
            
            # Pasar al siguiente jugador
            cur = cur.next
            turno += 1
            
            # Breve pausa entre turnos
            time.sleep(0.5)
        
        # Si solo queda un jugador activo, es el ganador
        cur = self.head
        while True:
            if not cur.data[2]:  # Si no está eliminado
                return cur.data[0]  # Retornar el nombre del ganador
            cur = cur.next
            if cur == self.head:
                break
                
        return None  # No debería llegar aquí

    def determinar_ganador_por_puntos(self):
        # Si se termina el juego sin ganador por dobles, gana quien tenga menos puntos
        if self.esta_vacia():
            return None, 0
            
        min_puntos = float('inf')
        ganador = None
        
        cur = self.head
        while True:
            nombre, acumulado, eliminado = cur.data
            if not eliminado and acumulado < min_puntos:
                min_puntos = acumulado
                ganador = nombre
            cur = cur.next
            if cur == self.head:
                break
                
        return ganador, min_puntos

def main():
    # Inicializar el juego
    lista_jugadores = ListaCircular()
    lista_jugadores.inicializar_jugadores()
    
    # Jugar hasta que haya un ganador o se termine el juego
    ganador_por_dobles = lista_jugadores.jugar()
    
    # Mostrar estado final
    lista_jugadores.mostrar_estado_jugadores()
    
    # Mostrar resultado final
    if ganador_por_dobles:
        print(f"\n¡{ganador_por_dobles} es el ganador por haber sacado dobles!")
    else:
        ganador, puntos = lista_jugadores.determinar_ganador_por_puntos()
        if ganador:
            print(f"\nJuego finalizado por decisión del usuario.")
            print(f"¡{ganador} es el ganador por tener la menor cantidad de puntos ({puntos})!")
        else:
            print("\nNo hay ganadores. Todos los jugadores fueron eliminados.")

if __name__ == "__main__":
    main()


    