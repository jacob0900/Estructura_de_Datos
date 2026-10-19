# Estructura de Datos

Códigos en **Python** del curso de **Estructura de Datos**: listas enlazadas simples y circulares implementadas desde cero, algoritmos de ordenamiento, recorrido de grafos, relaciones de recurrencia, y los laboratorios, entregables y parciales del curso.

## Contenido

### Listas enlazadas simples

| Archivo | Contenido |
|---|---|
| `lista_enlazada_completa.py` | Implementación completa de una lista enlazada: inserción (inicio, final, posición, ordenada), eliminación, búsqueda, recorrido, ordenamiento, inversión y un iterador propio |
| `lista_enlazada_metodos.py` | Métodos básicos: agregar al inicio y al final, eliminar, imprimir, máximo, mínimo, promedio y búsqueda |

### Listas circulares

| Archivo | Contenido |
|---|---|
| `lista_circular_completa.py` | Implementación completa de una lista circular: inserción, eliminación, búsqueda, `map`/`filter`/`reduce`, rotaciones, unión, intersección y diferencia, palíndromos, y un juego de ruleta que usa dos listas circulares (jugadores y premios) |
| `lista_circular_metodos.py` | Métodos básicos de una lista circular: agregar, eliminar, imprimir, máximo, mínimo, promedio y búsqueda |
| `lista_circular_juego_dados.py` | Juego por turnos con dos dados en el que los jugadores, guardados en una lista circular, se van eliminando |

### Ordenamiento y grafos

| Archivo | Contenido |
|---|---|
| `ordenamiento_insercion.py` | Ordenamiento por inserción |
| `ordenamiento_seleccion.py` | Ordenamiento por selección |
| `grafo_recorrido_dfs.py` | Recorrido en profundidad (DFS) recursivo de un grafo representado con listas de adyacencia |

### Relaciones de recurrencia

| Archivo | Contenido |
|---|---|
| `entregable1_recurrencias_lineales.py` | **Entregable 1.** Resuelve relaciones de recurrencia lineales, homogéneas y de coeficientes constantes de cualquier orden: polinomio característico, raíces reales y complejas conjugadas (forma polar), sistema de condiciones iniciales y solución cerrada, verificada contra el cálculo recursivo. Usa SymPy |
| `recurrencias_lineales_borrador.py` | Versión anterior del entregable 1 |
| `laboratorio_recurrencia_segundo_orden.py` | Expresión no recurrente de fₙ = a·fₙ₋₁ + b·fₙ₋₂ a partir de f₀ y f₁, para raíces distintas o repetidas |

### Entregables y laboratorios

| Archivo | Contenido |
|---|---|
| `entregable2_portafolio_acciones.py` | **Entregable 2.** Selección de un portafolio de acciones a partir de sus rendimientos y correlaciones: máximo beneficio con un límite de correlación, un mínimo de acciones y un riesgo máximo. Lee `rendimientos.txt` y `correlaciones.txt` |
| `laboratorio_sistema_cine.py` | Sistema de cine: cartelera, salas como matrices de asientos, validación de horarios, reserva de puestos y pago de boletas con registro de ingresos. Lee `peliculaslab2.csv` |
| `emparejamiento_clientes_empleados.py` | Empareja clientes con empleados según la ocupación requerida y el presupuesto. Lee `empleados.txt` y `clientes.txt` (formato `nombre;ocupación;valor`) |

### Parciales

| Archivo | Contenido |
|---|---|
| `parcial1_punto1_lista_enlazada.py` | Parcial 1, punto 1: menú interactivo sobre una lista enlazada |
| `parcial1_punto2_juego_dados.py` | Parcial 1, punto 2: juego de dados con jugadores en una lista circular |
| `parcial1_solucion1_listas_potencias.py` | Solución: tres listas enlazadas con números aleatorios, sus cuadrados y sus cubos |
| `parcial1_solucion3_notas.py` | Solución: notas validadas en una lista enlazada, con máximo, mínimo y promedio |
| `parcial2_punto1_mover_jugador.py` | Parcial 2, punto 1: mover un jugador *n* posiciones hacia adelante o hacia atrás en una lista enlazada, con validaciones |
| `parcial_festival_talentos.py` | Festival de talentos: participantes en una lista circular, rondas con puntajes aleatorios, ordenamiento por puntaje y eliminación de los últimos |
| `parcial_festival_talentos_borrador.py` | Borrador del parcial del festival de talentos |
| `parcial_festival_talentos_promedio.py` | Versión del festival de talentos que además calcula el puntaje promedio |

### Otros

| Archivo | Contenido |
|---|---|
| `notas_promedio_max_min.py` | Lee 5 notas validadas y muestra el promedio, la máxima y la mínima |
| `diagrama_flujo_integrales_trabajo.py` | Diagrama de flujo, dibujado con Matplotlib, para resolver integrales de trabajo (rotacional y teorema de Green) |

### Datos

- `peliculaslab2.csv`: películas, horarios, salas y ocupación de puestos para el sistema de cine.
- `rendimientos.txt`: rendimiento y riesgo de cada acción para el entregable 2.

## Cómo ejecutarlo

Requisitos: **Python 3**. Solo algunos scripts usan librerías externas:

```bash
pip install numpy sympy matplotlib
```

Cada archivo es un programa independiente. Los que leen datos deben ejecutarse desde esta carpeta:

```bash
python lista_circular_completa.py
```

## Autores

- **Jacobo Londoño**, [LinkedIn](https://www.linkedin.com/in/jacobo-londo%C3%B1o-baquero-a2b86733a/)
- Los entregables 1 y 2 se desarrollaron en equipo con **Samuel Chamorro** y **Yulissa Tapia**.
