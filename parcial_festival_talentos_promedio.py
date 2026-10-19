import random
import time

class Participante:
    def __init__(self, nombre, edad):
        """Inicializa un nuevo participante con nombre y edad."""
        self.nombre = nombre
        self.edad = edad
        self.puntaje = 0  # Puntaje inicial del participante

class Node:
    def __init__(self, participante):
        """Inicializa un nuevo nodo con un participante."""
        self.participante = participante
        self.next = None  # Referencia al siguiente nodo

class ListaCircular:
    def __init__(self):
        """Inicializa una lista circular vacía."""
        self.head = None  # Referencia al primer nodo

    def esta_vacia(self):
        """Verifica si la lista está vacía."""
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
        """Imprime los nombres de los participantes en la lista."""
        if self.esta_vacia():
            print("La lista está vacía")
            return
        cur = self.head
        print(cur.participante.nombre, end="")
        while cur.next != self.head:
            cur = cur.next
            print(" --> ", cur.participante.nombre, end="")
        print()

    def agregar_ultimo(self, participante):
        """Agrega un nuevo participante al final de la lista."""
        node = Node(participante)
        if self.esta_vacia():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def mover_al_inicio(self, current_node):
        """Mueve un nodo específico al inicio de la lista."""
        if self.esta_vacia() or self.longitud() <= 1 or current_node == self.head:
            return
        prev = self.head
        while prev.next != current_node:
            prev = prev.next
        prev.next = current_node.next
        last = self.head
        while last.next != self.head:
            last = last.next
        current_node.next = self.head
        last.next = current_node
        self.head = current_node

    def lanzar_puntaje(self):
        """Genera un puntaje aleatorio entre 1 y 10."""
        return random.randint(1, 10)

    def mostrar_estado_participantes(self):
        """Muestra el estado actual de todos los participantes."""
        if self.esta_vacia():
            print("No hay participantes en la lista.")
            return
        print("\nESTADO DE LOS PARTICIPANTES")
        print("Nombre\t\t\tEdad\tPuntaje")
        cur = self.head
        while True:
            participante = cur.participante
            print(participante.nombre + "\t\t" + str(participante.edad) + "\t" + str(participante.puntaje))
            cur = cur.next
            if cur == self.head:
                break

    def ordenar_por_puntaje(self):
        """Ordena la lista de participantes por puntaje en orden descendente."""
        if self.esta_vacia() or self.longitud() <= 1:
            return
        n = self.longitud()
        for i in range(n):
            cur = self.head
            for j in range(n - i - 1):
                if cur.participante.puntaje < cur.next.participante.puntaje:
                    temp = cur.participante
                    cur.participante = cur.next.participante
                    cur.next.participante = temp
                cur = cur.next

    def eliminar_ultimos_dos(self):
        """Elimina los dos últimos nodos de la lista."""
        if self.esta_vacia() or self.longitud() <= 2:
            self.head = None
            return
        n = self.longitud()
        cur = self.head
        for i in range(n - 3):
            cur = cur.next
        cur.next = self.head
        
    def calcular_promedio(self):
        """Calcula el promedio de los puntajes en la lista circular."""
        if self.esta_vacia():
            return None

        suma = 0
        contador = 0
        actual = self.head

        while True:
            suma += actual.participante.puntaje
            contador += 1
            actual = actual.next

            # Salir del bucle cuando volvemos al nodo inicial
            if actual == self.head:
                break

        if contador == 0:
            return 0

        return suma / contador


def main():
    """Función principal que ejecuta el festival de talentos."""
    festival = ListaCircular()

    # Crear participantes
    participante1 = Participante("Ana López", 22)
    participante2 = Participante("Carlos Gómez", 20)
    participante3 = Participante("María Pérez", 21)
    participante4 = Participante("Juan Rodríguez", 19)
    participante5 = Participante("Lucía Martínez", 23)

    # Agregar participantes a la lista
    festival.agregar_ultimo(participante1)
    festival.agregar_ultimo(participante2)
    festival.agregar_ultimo(participante3)
    festival.agregar_ultimo(participante4)
    festival.agregar_ultimo(participante5)

    print("Participantes inscritos en el festival:")
    festival.imprimir()
    festival.mostrar_estado_participantes()

    # Ejecutar rondas del festival
    for ronda in range(1, 4):
        print("\nRONDA " + str(ronda) + " DEL FESTIVAL DE TALENTOS")

        participantes_en_ronda = festival.longitud()
        cur = festival.head

        for i in range(participantes_en_ronda):
            participante = cur.participante
            siguiente = cur.next

            print("\nTurno de " + participante.nombre + " (Edad: " + str(participante.edad) + ")")
            respuesta = input("¿Está presente " + participante.nombre + "? (s/n): ").lower()

            if respuesta == 's':
                puntaje = festival.lanzar_puntaje()
                print(participante.nombre + " recibe puntaje: " + str(puntaje))
                participante.puntaje += puntaje
                print("Puntaje acumulado: " + str(participante.puntaje))
                cur = siguiente
            else:
                print(participante.nombre + " ausente. Se mueve al inicio.")
                festival.mover_al_inicio(cur)
                cur = siguiente

        print("\nEstado después de la Ronda " + str(ronda) + ":")
        festival.mostrar_estado_participantes()

    print("\nOrdenando por puntaje (mayor a menor)...")
    festival.ordenar_por_puntaje()
   

    print("\nRESULTADOS FINALES:")
    print("Nombre\t\t\tEdad\tPuntaje")

    cur = festival.head
    ganador = cur.participante if not festival.esta_vacia() else None
    n = festival.longitud()

    for i in range(n):
        participante = cur.participante
        print(participante.nombre + "\t\t" + str(participante.edad) + "\t" + str(participante.puntaje))
        cur = cur.next
        if cur == festival.head:
            break

    if ganador:
        print("\nGANADOR: " + ganador.nombre + " con " + str(ganador.puntaje) + " puntos")

    print("\nEliminando los dos últimos lugares...")
    festival.eliminar_ultimos_dos()

    
    promedio = festival.calcular_promedio()
    print("El promedio de puntos fue:")
    print(promedio)

    print("\nParticipantes restantes:")
    festival.imprimir()

if __name__ == "__main__":
    main()
