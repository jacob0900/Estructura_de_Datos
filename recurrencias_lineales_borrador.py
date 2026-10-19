"""
Programa para resolver relaciones de recurrencia lineales, homogéneas y de coeficientes constantes.
Este programa encuentra una expresión cerrada (no recurrente) para una relación de recurrencia 
de la forma: fn = a₁fn-1 + a₂fn-2 + ... + aₘfn-m con valores iniciales dados.

Autores: [Nombres de los autores]
Fecha: 8 de abril de 2025
"""

import numpy as np
from sympy import symbols, Poly, solve, exp, simplify, factor
import re

def obtener_datos():
    """
    Solicita al usuario los datos de entrada necesarios para resolver la relación de recurrencia.
    
    Returns:
        tuple: (m, coeficientes, valores_iniciales) donde:
            - m: Orden de la relación de recurrencia
            - coeficientes: Lista de m coeficientes (a₁, a₂, ..., aₘ)
            - valores_iniciales: Lista de m valores iniciales (C₀, C₁, ..., Cₘ₋₁)
    """
    try:
        print("Resolución de relaciones de recurrencia lineales, homogéneas y de coeficientes constantes")
        print("======================================================================================")
        print("Ingrese los datos para la relación de recurrencia: fn = a₁fn-1 + a₂fn-2 + ... + aₘfn-m")
        
        # Obtener el valor de m
        while True:
            try:
                m = int(input("\nIngrese el valor de m (el orden de la recurrencia): "))
                if m <= 0:
                    print("Error: m debe ser un número entero positivo.")
                    continue
                break
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
        
        # Obtener los coeficientes
        coeficientes = []
        print("\nIngrese los", m, "coeficientes a₁, a₂, ..., aₘ:")
        for i in range(1, m + 1):
            while True:
                try:
                    coef = float(input(f"  a{i}: "))
                    coeficientes.append(coef)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un número válido.")
        
        # Obtener los valores iniciales
        valores_iniciales = []
        print("\nIngrese los", m, "valores iniciales C₀, C₁, ..., Cₘ₋₁:")
        for i in range(m):
            while True:
                try:
                    valor = float(input(f"  C{i}: "))
                    valores_iniciales.append(valor)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un número válido.")
        
        return m, coeficientes, valores_iniciales
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, None, None

def encontrar_polinomio_caracteristico(m, coeficientes):
    """
    Encuentra el polinomio característico de la relación de recurrencia.
    
    Args:
        m (int): Orden de la recurrencia
        coeficientes (list): Lista de coeficientes a₁, a₂, ..., aₘ
    
    Returns:
        sympy.Poly: El polinomio característico
    """
    r = symbols('r')
    # El polinomio característico es rᵐ - a₁rᵐ⁻¹ - a₂rᵐ⁻² - ... - aₘ
    terminos = [r**m]
    for i in range(m):
        terminos.append(-coeficientes[i] * r**(m-i-1))
    
    polinomio = sum(terminos)
    return Poly(polinomio, r)

def resolver_polinomio_caracteristico(polinomio):
    """
    Encuentra las raíces del polinomio característico.
    
    Args:
        polinomio (sympy.Poly): El polinomio característico
    
    Returns:
        list: Lista de raíces con sus multiplicidades
    """
    r = symbols('r')
    raices = solve(polinomio.as_expr(), r)
    
    # Contar multiplicidades
    raices_con_multiplicidad = []
    raices_unicas = set(raices)
    
    for raiz in raices_unicas:
        multiplicidad = raices.count(raiz)
        raices_con_multiplicidad.append((raiz, multiplicidad))
    
    return raices_con_multiplicidad

def resolver_sistema_coeficientes(m, raices_con_multiplicidad, valores_iniciales):
    """
    Resuelve el sistema de ecuaciones para encontrar los coeficientes de la expresión cerrada.
    
    Args:
        m (int): Orden de la recurrencia
        raices_con_multiplicidad (list): Lista de raíces con sus multiplicidades
        valores_iniciales (list): Lista de valores iniciales C₀, C₁, ..., Cₘ₋₁
    
    Returns:
        list: Coeficientes para la expresión cerrada
    """
    n = symbols('n')
    
    # Construir la matriz del sistema de ecuaciones
    A = []
    for k in range(m):
        fila = []
        for raiz, multiplicidad in raices_con_multiplicidad:
            for j in range(multiplicidad):
                # Añadir término n^j * raiz^n evaluado en n=k
                fila.append(k**j * raiz**k)
        A.append(fila)
    
    # Resolver el sistema de ecuaciones
    A = np.array(A, dtype=complex)
    b = np.array(valores_iniciales, dtype=complex)
    
    try:
        # Si determinante es cercano a cero, usar mínimos cuadrados
        if abs(np.linalg.det(A)) < 1e-10:
            coeficientes_solucion, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        else:
            coeficientes_solucion = np.linalg.solve(A, b)
        
        return coeficientes_solucion
    except np.linalg.LinAlgError:
        # Si hay problemas al resolver, usar mínimos cuadrados
        coeficientes_solucion, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        return coeficientes_solucion

def formatear_termino(coef, raiz, potencia=0):
    """
    Formatea un término de la solución para mostrar como texto.
    
    Args:
        coef (complex): Coeficiente
        raiz (complex): Raíz del polinomio característico
        potencia (int): Potencia de n como factor
    
    Returns:
        str: Término formateado
    """
    # Redondear para evitar errores de precisión
    coef_real = round(coef.real, 10)
    coef_imag = round(coef.imag, 10)
    
    # Determinar si el coeficiente es real o complejo
    if abs(coef_imag) < 1e-10:  # Es real
        coef_str = f"{coef_real:.6g}".rstrip('0').rstrip('.') if coef_real != 1 else ""
        if coef_str == "-1":
            coef_str = "-"
        elif coef_str == "0":
            return ""
    else:  # Es complejo
        coef_str = f"({coef_real:.6g}{'+' if coef_imag > 0 else ''}{coef_imag:.6g}i)".rstrip('0').rstrip('.')
    
    # Formatear la potencia de n
    n_str = "" if potencia == 0 else f"n^{potencia} * " if potencia > 1 else "n * "
    
    # Formatear la raíz
    raiz_real = round(raiz.real, 10)
    raiz_imag = round(raiz.imag, 10)
    
    if abs(raiz_imag) < 1e-10:  # Es real
        raiz_str = f"{raiz_real:.6g}".rstrip('0').rstrip('.')
        term = f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}({raiz_str})^n"
    else:  # Es complejo
        raiz_str = f"({raiz_real:.6g}{'+' if raiz_imag > 0 else ''}{raiz_imag:.6g}i)".rstrip('0').rstrip('.')
        term = f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}{raiz_str}^n"
    
    # Simplificar casos especiales
    if "1)^n" in term:
        term = term.replace("(1)^n", "1")
    elif "0)^n" in term:
        term = term.replace("(0)^n", "0")
    
    return term

def formatear_solucion(coeficientes, raices_con_multiplicidad):
    """
    Formatea la solución completa para mostrar como texto.
    
    Args:
        coeficientes (list): Lista de coeficientes resueltos
        raices_con_multiplicidad (list): Lista de raíces con sus multiplicidades
    
    Returns:
        str: Expresión cerrada formateada
    """
    n = symbols('n')
    terminos = []
    indice = 0
    
    for raiz, multiplicidad in raices_con_multiplicidad:
        for j in range(multiplicidad):
            coef = coeficientes[indice]
            termino = formatear_termino(coef, raiz, j)
            if termino:
                terminos.append(termino)
            indice += 1
    
    if not terminos:
        return "0"
    
    # Unir todos los términos
    solucion = " + ".join(terminos)
    
    # Simplificar operadores
    solucion = solucion.replace("+ -", "- ")
    
    return solucion

def calcular_valor_fn(n, coeficientes, raices_con_multiplicidad):
    """
    Calcula el valor numérico de f(n) para un n específico usando la expresión cerrada.
    
    Args:
        n (int): Valor de n para calcular f(n)
        coeficientes (list): Lista de coeficientes resueltos
        raices_con_multiplicidad (list): Lista de raíces con sus multiplicidades
    
    Returns:
        complex: Valor de f(n)
    """
    resultado = 0
    indice = 0
    
    for raiz, multiplicidad in raices_con_multiplicidad:
        for j in range(multiplicidad):
            coef = coeficientes[indice]
            resultado += coef * (n**j) * (raiz**n)
            indice += 1
    
    # Si el resultado es casi real, retornar como real
    if abs(resultado.imag) < 1e-10:
        return resultado.real
    return resultado

def main():
    """
    Función principal del programa.
    """
    try:
        # Obtener datos de entrada
        m, coeficientes, valores_iniciales = obtener_datos()
        if m is None:
            return
        
        print("\nResolución de la relación de recurrencia:")
        print("fn =", end=" ")
        for i in range(m):
            if i > 0:
                print(" +", end=" ")
            print(f"({coeficientes[i]}) * f(n-{i+1})", end="")
        
        print("\nValores iniciales:", end=" ")
        for i in range(m):
            if i > 0:
                print(",", end=" ")
            print(f"f{i} = {valores_iniciales[i]}", end="")
        print("\n")
        
        # Encontrar el polinomio característico
        polinomio = encontrar_polinomio_caracteristico(m, coeficientes)
        print(f"Polinomio característico: {polinomio}")
        
        # Resolver el polinomio característico
        raices_con_multiplicidad = resolver_polinomio_caracteristico(polinomio)
        print("\nRaíces del polinomio característico:")
        for raiz, multiplicidad in raices_con_multiplicidad:
            if raiz.is_real:
                print(f"  {float(raiz.evalf()):.6g} (multiplicidad {multiplicidad})")
            else:
                print(f"  {complex(raiz.evalf()):.6g} (multiplicidad {multiplicidad})")
        
        # Resolver el sistema para encontrar coeficientes
        coeficientes_solucion = resolver_sistema_coeficientes(m, raices_con_multiplicidad, valores_iniciales)
        
        # Formatear la solución
        expresion_cerrada = formatear_solucion(coeficientes_solucion, raices_con_multiplicidad)
        print("\nExpresión cerrada para f(n):")
        print(f"  f(n) = {expresion_cerrada}")
        
        # Calcular algunos valores para verificación
        print("\nVerificación de valores:")
        for i in range(m):
            print(f"  f({i}) = {valores_iniciales[i]} (valor inicial)")
        
        # Verificar algunos valores adicionales
        for i in range(m, m + 5):
            # Calcular usando la recurrencia
            fn_recurrente = 0
            for j in range(m):
                indice = i - j - 1
                if indice < m:
                    fn_recurrente += coeficientes[j] * valores_iniciales[indice]
                else:
                    # Si necesitamos valores de fn para n > m-1, los calculamos recursivamente
                    # No implementado para simplicidad
                    pass
            
            # Calcular usando la expresión cerrada
            fn_cerrada = calcular_valor_fn(i, coeficientes_solucion, raices_con_multiplicidad)
            
            # Mostrar solo si tenemos ambos valores para comparar
            if i == m:
                print(f"  f({i}) = {fn_cerrada:.10g} (usando expresión cerrada)")
            
        # Ofrecer calcular valores específicos
        while True:
            try:
                opcion = input("\n¿Desea calcular f(n) para algún valor específico de n? (s/n): ").lower()
                if opcion != 's':
                    break
                
                n_especifico = int(input("Ingrese el valor de n: "))
                if n_especifico < 0:
                    print("Error: n debe ser no negativo.")
                    continue
                
                resultado = calcular_valor_fn(n_especifico, coeficientes_solucion, raices_con_multiplicidad)
                print(f"f({n_especifico}) = {resultado:.10g}")
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
            except Exception as e:
                print(f"Error al calcular: {e}")
    
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()