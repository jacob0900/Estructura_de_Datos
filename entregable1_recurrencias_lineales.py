import numpy as np
from sympy import symbols, Poly, solve, exp, simplify, factor, Symbol, I, pi, cos, sin, re, im
from sympy import Rational, sympify, expand
from fractions import Fraction
import cmath
import re as regex

def obtener_datos():
    """
    Solicita al usuario los datos de entrada necesarios para resolver la relación de recurrencia.
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
        
        # Obtener los coeficientes como fracciones simbólicas
        coeficientes = []
        print("\nIngrese los", m, "coeficientes a₁, a₂, ..., aₘ (puede usar fracciones como '1/3'):")
        for i in range(1, m + 1):
            while True:
                try:
                    coef_str = input(f"  a{i}: ")
                    # Convertir a fracción simbólica
                    coef = sympify(coef_str)
                    coeficientes.append(coef)
                    break
                except (ValueError, SyntaxError):
                    print("Error: Por favor ingrese un número válido o una fracción (ej: 1/3).")
        
        # Obtener los valores iniciales como fracciones simbólicas
        valores_iniciales = []
        print("\nIngrese los", m, "valores iniciales C₀, C₁, ..., Cₘ₋₁ (puede usar fracciones como '1/3'):")
        for i in range(m):
            while True:
                try:
                    valor_str = input(f"  C{i}: ")
                    # Convertir a fracción simbólica
                    valor = sympify(valor_str)
                    valores_iniciales.append(valor)
                    break
                except (ValueError, SyntaxError):
                    print("Error: Por favor ingrese un número válido o una fracción (ej: 1/3).")
        
        return m, coeficientes, valores_iniciales
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, None, None

def encontrar_polinomio_caracteristico(m, coeficientes):
   
    r = symbols('r')
    # El polinomio característico es rᵐ - a₁rᵐ⁻¹ - a₂rᵐ⁻² - ... - aₘ
    terminos = [r**m]
    for i in range(m):
        terminos.append(-coeficientes[i] * r**(m-i-1))
    
    polinomio = sum(terminos)
    return Poly(polinomio, r)

def resolver_polinomio_caracteristico(polinomio):
   
    r = symbols('r')
    raices = solve(polinomio.as_expr(), r)
    
    # Contar multiplicidades
    raices_con_multiplicidad = []
    raices_unicas = []
    
    # Usamos un enfoque más robusto para identificar raíces únicas
    for raiz in raices:
        es_nueva = True
        for r_unica in raices_unicas:
            if abs(complex(raiz.evalf()) - complex(r_unica.evalf())) < 1e-10:
                es_nueva = False
                break
        if es_nueva:
            raices_unicas.append(raiz)
    
    for raiz in raices_unicas:
        multiplicidad = 0
        for r in raices:
            if abs(complex(raiz.evalf()) - complex(r.evalf())) < 1e-10:
                multiplicidad += 1
        raices_con_multiplicidad.append((raiz, multiplicidad))
    
    return raices_con_multiplicidad

def son_conjugados(raiz1, raiz2):
    
    r1 = complex(raiz1.evalf())
    r2 = complex(raiz2.evalf())
    return abs(r1.real - r2.real) < 1e-10 and abs(r1.imag + r2.imag) < 1e-10 and abs(r1.imag) > 1e-10

def encontrar_pares_conjugados(raices_con_multiplicidad):
   
    pares_conjugados = []
    for i in range(len(raices_con_multiplicidad)):
        for j in range(i+1, len(raices_con_multiplicidad)):
            raiz1, mult1 = raices_con_multiplicidad[i]
            raiz2, mult2 = raices_con_multiplicidad[j]
            if mult1 == mult2 and son_conjugados(raiz1, raiz2):
                pares_conjugados.append((i, j))
    return pares_conjugados

def resolver_sistema_coeficientes(m, raices_con_multiplicidad, valores_iniciales):
   
    n = symbols('n')
    
    # Construir la matriz del sistema de ecuaciones
    A = []
    for k in range(m):
        fila = []
        for raiz, multiplicidad in raices_con_multiplicidad:
            for j in range(multiplicidad):
                # Añadir término n^j * raiz^n evaluado en n=k
                valor = complex((k**j * raiz**k).evalf())
                fila.append(valor)
        A.append(fila)
    
    # Convertir a valores iniciales a complejos para el cálculo numérico
    b = np.array([complex(v.evalf()) for v in valores_iniciales], dtype=complex)
    A = np.array(A, dtype=complex)
    
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

def simplificar_forma_polar(raiz):
    
    c = complex(raiz.evalf())
    return abs(c), cmath.phase(c)

def formatear_termino_real(coef, raiz, potencia=0):
    
    # Intentar simplificar el coeficiente a una fracción
    coef_real = round(coef.real, 14)
    if abs(coef.imag) > 1e-10:  # Si realmente tiene parte imaginaria (no debería)
        return ""  # No debería ocurrir para términos reales
    
    # Intentar convertir a fracción si es posible
    try:
        frac = Fraction(coef_real).limit_denominator(1000)
        if frac.denominator == 1:
            coef_str = str(frac.numerator)
        else:
            coef_str = f"{frac.numerator}/{frac.denominator}"
    except (ValueError, OverflowError):
        coef_str = f"{coef_real:.10g}".rstrip('0').rstrip('.')
    
    # Simplificar coeficiente
    if coef_str == "1" and potencia == 0 and raiz != 0:
        coef_str = ""
    elif coef_str == "-1" and potencia == 0 and raiz != 0:
        coef_str = "-"
    elif coef_str == "0":
        return ""
    
    # Formatear la potencia de n
    n_str = "" if potencia == 0 else f"n^{potencia} * " if potencia > 1 else "n * "
    
    # Formatear la raíz
    if raiz == 0:
        if potencia == 0:
            return coef_str  # Si raíz=0 y potencia=0, solo retornamos el coeficiente
        else:
            return f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}0"  # 0^n = 0 para n > 0
    
    # Intentar convertir la raíz a fracción si es posible
    raiz_float = float(raiz.evalf())
    try:
        raiz_frac = Fraction(raiz_float).limit_denominator(1000)
        if raiz_frac.denominator == 1:
            raiz_str = str(raiz_frac.numerator)
        else:
            raiz_str = f"{raiz_frac.numerator}/{raiz_frac.denominator}"
    except (ValueError, OverflowError):
        raiz_str = f"{raiz_float:.10g}".rstrip('0').rstrip('.')
    
    # Construir el término
    if raiz_str == "1":
        return f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}1"
    else:
        return f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}({raiz_str})^n"

def formatear_par_conjugado(coef1, coef2, raiz, potencia=0):
   
    # Verificar que los coeficientes son realmente conjugados
    if abs(coef1.real - coef2.real) > 1e-10 or abs(coef1.imag + coef2.imag) > 1e-10:
        # Si no son conjugados, formatear individualmente
        return None
    
    # Obtener forma polar de la raíz
    modulo, angulo = simplificar_forma_polar(raiz)
    
    # = 2A*a*r^n donde A es 2*coef1.real
    coef_real = 2 * coef1.real
    
    # Intentar convertir a fracción si es posible
    try:
        coef_frac = Fraction(coef_real).limit_denominator(1000)
        if coef_frac.denominator == 1:
            coef_str = str(coef_frac.numerator)
        else:
            coef_str = f"{coef_frac.numerator}/{coef_frac.denominator}"
    except (ValueError, OverflowError):
        coef_str = f"{coef_real:.10g}".rstrip('0').rstrip('.')
    
    # Simplificar coeficiente
    if coef_str == "1" and potencia == 0:
        coef_str = ""
    elif coef_str == "-1" and potencia == 0:
        coef_str = "-"
    elif coef_str == "0":
        return ""
    
    # Formatear la potencia de n
    n_str = "" if potencia == 0 else f"n^{potencia} * " if potencia > 1 else "n * "
    
    # Intentar expresar el ángulo como múltiplo de π
    angulo_pi = angulo / np.pi
    try:
        frac_pi = Fraction(angulo_pi).limit_denominator(12)  # Limitar a fracciones simples
        if abs(angulo_pi - float(frac_pi)) < 1e-10:  # Si es realmente una fracción simple de π
            if frac_pi.numerator == 0:
                ang_str = "0"
            elif frac_pi.denominator == 1:
                ang_str = f"{frac_pi.numerator}π"
            else:
                ang_str = f"{frac_pi.numerator}π/{frac_pi.denominator}"
        else:
            ang_str = f"{angulo:.10g}".rstrip('0').rstrip('.')
    except (ValueError, OverflowError):
        ang_str = f"{angulo:.10g}".rstrip('0').rstrip('.')
    
    # Intentar expresar el módulo como fracción
    try:
        mod_frac = Fraction(modulo).limit_denominator(1000)
        if mod_frac.denominator == 1:
            mod_str = str(mod_frac.numerator)
        else:
            mod_str = f"{mod_frac.numerator}/{mod_frac.denominator}"
    except (ValueError, OverflowError):
        mod_str = f"{modulo:.10g}".rstrip('0').rstrip('.')
    
    # Construir el término trigonométrico
    if "π" in ang_str:
        trig_term = f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}({mod_str})^n * cos(n * {ang_str})"
    else:
        trig_term = f"{coef_str}{'' if not coef_str or coef_str == '-' else ' * '}{n_str}({mod_str})^n * cos(n * {ang_str})"
    
    return trig_term

def formatear_solucion(coeficientes, raices_con_multiplicidad):
   
    # Identificar pares conjugados
    pares_conjugados = encontrar_pares_conjugados(raices_con_multiplicidad)
    pares_procesados = set()
    
    terminos = []
    indice = 0
    
    # Procesar cada raíz
    for i, (raiz, multiplicidad) in enumerate(raices_con_multiplicidad):
        # Comprobar si esta raíz es parte de un par conjugado
        es_parte_de_par = False
        for par in pares_conjugados:
            if i in par and i not in pares_procesados:
                # Encontramos un par no procesado
                i1, i2 = par
                raiz1, mult1 = raices_con_multiplicidad[i1]
                raiz2, mult2 = raices_con_multiplicidad[i2]
                
                # Procesar cada potencia de n para este par
                for j in range(mult1):
                    idx1 = indice + sum(r[1] for r in raices_con_multiplicidad[:i1]) + j
                    idx2 = indice + sum(r[1] for r in raices_con_multiplicidad[:i2]) + j
                    
                    if idx1 < len(coeficientes) and idx2 < len(coeficientes):
                        coef1 = coeficientes[idx1]
                        coef2 = coeficientes[idx2]
                        
                        # Formatear como par trigonométrico
                        termino_trig = formatear_par_conjugado(coef1, coef2, raiz1, j)
                        if termino_trig:
                            terminos.append(termino_trig)
                
                # Marcar ambos índices como procesados
                pares_procesados.add(i1)
                pares_procesados.add(i2)
                es_parte_de_par = True
                break
        
        # Si no es parte de un par conjugado, formatear normalmente
        if not es_parte_de_par:
            for j in range(multiplicidad):
                idx = indice + sum(r[1] for r in raices_con_multiplicidad[:i]) + j
                if idx < len(coeficientes):
                    coef = coeficientes[idx]
                    # Si la raíz es real (o casi real)
                    if abs(im(raiz.evalf())) < 1e-10:
                        termino = formatear_termino_real(coef, re(raiz.evalf()), j)
                        if termino:
                            terminos.append(termino)
    
    if not terminos:
        return "0"
    
    # Unir todos los términos
    solucion = " + ".join(terminos)
    
    # Simplificar operadores
    solucion = solucion.replace("+ -", "- ")
    
    return solucion

def calcular_fn_recursivamente(n, m, coeficientes, valores_iniciales):
    
    # Crear un caché para valores ya calculados
    cache = {i: valores_iniciales[i] for i in range(min(m, len(valores_iniciales)))}
    
    def fn_rec(k):
        if k in cache:
            return cache[k]
        
        # Calcular f(k) usando la relación de recurrencia
        result = 0
        for i in range(m):
            result += coeficientes[i] * fn_rec(k - i - 1)
        
        # Guardar en caché y retornar
        cache[k] = result
        return result
    
    return fn_rec(n)

def calcular_valor_fn(n, coeficientes_solucion, raices_con_multiplicidad):
    """
    Calcula el valor de f(n) usando la expresión cerrada.
    """
    resultado = complex(0, 0)
    indice = 0
    
    for raiz, multiplicidad in raices_con_multiplicidad:
        for j in range(multiplicidad):
            coef = coeficientes_solucion[indice]
            # Calcular raiz^n de manera segura como complejo
            raiz_evaluada = complex(raiz.evalf()) ** n
            resultado += coef * (n**j) * raiz_evaluada
            indice += 1
    
    # Si el resultado es casi real, retornar como real
    if abs(resultado.imag) < 1e-10:
        return resultado.real
    return resultado

def mostrar_valor_numerico(valor):
    """
    Muestra un valor numérico de manera adecuada, sea real o complejo.
    """
    if isinstance(valor, complex):
        if abs(valor.imag) < 1e-10:  # Si la parte imaginaria es despreciable
            return f"{valor.real:.10g}"
        else:
            return f"{valor.real:.6g} + {valor.imag:.6g}i"
    else:
        return f"{valor:.10g}"

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
            if abs(im(raiz.evalf())) < 1e-10:
                raiz_value = float(re(raiz.evalf()))
                try:
                    frac = Fraction(raiz_value).limit_denominator(1000)
                    if frac.denominator == 1:
                        raiz_str = str(frac.numerator)
                    else:
                        raiz_str = f"{frac.numerator}/{frac.denominator}"
                    print(f"  {raiz_str} (multiplicidad {multiplicidad})")
                except (ValueError, OverflowError):
                    print(f"  {raiz_value:.10g} (multiplicidad {multiplicidad})")
            else:
                raiz_compleja = complex(raiz.evalf())
                modulo, angulo = abs(raiz_compleja), cmath.phase(raiz_compleja)
                
                # Intentar expresar el ángulo como múltiplo de π
                angulo_pi = angulo / np.pi
                try:
                    frac_pi = Fraction(angulo_pi).limit_denominator(12)
                    if abs(angulo_pi - float(frac_pi)) < 1e-10:
                        if frac_pi.denominator == 1:
                            ang_str = f"{frac_pi.numerator}π"
                        else:
                            ang_str = f"{frac_pi.numerator}π/{frac_pi.denominator}"
                        print(f"  {modulo:.6g} * e^(i*{ang_str}) (multiplicidad {multiplicidad})")
                    else:
                        print(f"  {raiz_compleja:.10g} (multiplicidad {multiplicidad})")
                except (ValueError, OverflowError):
                    print(f"  {raiz_compleja:.10g} (multiplicidad {multiplicidad})")
        
        # Resolver el sistema para encontrar coeficientes
        coeficientes_solucion = resolver_sistema_coeficientes(m, raices_con_multiplicidad, valores_iniciales)
        
        # Formatear la solución
        expresion_cerrada = formatear_solucion(coeficientes_solucion, raices_con_multiplicidad)
        print("\nExpresión cerrada para f(n):")
        print(f"  f(n) = {expresion_cerrada}")
        
        # Verificación completa
        print("\nVerificación de valores:")
        for i in range(m):
            valor_inicial = complex(valores_iniciales[i].evalf())
            if abs(valor_inicial.imag) < 1e-10:
                print(f"  f({i}) = {valor_inicial.real:.10g} (valor inicial)")
            else:
                print(f"  f({i}) = {valor_inicial} (valor inicial)")
        
        # Verificar algunos valores adicionales usando ambos métodos
        max_verificacion = m + 5
        print(f"\nComparación de valores calculados (recursivamente vs expresión cerrada):")
        for i in range(m, max_verificacion):
            # Calcular usando la recurrencia
            fn_recurrente = calcular_fn_recursivamente(i, m, coeficientes, valores_iniciales)
            if hasattr(fn_recurrente, 'evalf'):
                fn_recurrente_valor = complex(fn_recurrente.evalf())
                if abs(fn_recurrente_valor.imag) < 1e-10:
                    fn_recurrente_val = fn_recurrente_valor.real
                else:
                    fn_recurrente_val = fn_recurrente_valor
            else:
                fn_recurrente_val = fn_recurrente
            
            # Calcular usando la expresión cerrada
            fn_cerrada = calcular_valor_fn(i, coeficientes_solucion, raices_con_multiplicidad)
            
            # Verificar diferencia relativa
            if isinstance(fn_recurrente_val, complex) or isinstance(fn_cerrada, complex):
                # Si alguno de los valores es complejo, convertir ambos a complejos y calcular la diferencia
                fn_rec_complejo = complex(fn_recurrente_val) if not isinstance(fn_recurrente_val, complex) else fn_recurrente_val
                fn_cer_complejo = complex(fn_cerrada) if not isinstance(fn_cerrada, complex) else fn_cerrada
                diferencia = abs(fn_cer_complejo - fn_rec_complejo)
                if abs(fn_rec_complejo) > 1e-10:
                    diferencia_rel = diferencia / abs(fn_rec_complejo)
                    mensaje = "OK" if diferencia_rel < 1e-10 else f"Diferencia relativa: {diferencia_rel:.2e}"
                else:
                    mensaje = "OK" if diferencia < 1e-10 else f"Diferencia absoluta: {diferencia:.2e}"
            else:
                # Ambos son reales
                diferencia = abs(fn_cerrada - fn_recurrente_val)
                if abs(fn_recurrente_val) > 1e-10:
                    diferencia_rel = diferencia / abs(fn_recurrente_val)
                    mensaje = "OK" if diferencia_rel < 1e-10 else f"Diferencia relativa: {diferencia_rel:.2e}"
                else:
                    mensaje = "OK" if diferencia < 1e-10 else f"Diferencia absoluta: {diferencia:.2e}"
            
            print(f"  f({i}) = {mostrar_valor_numerico(fn_recurrente_val)} (recursivo) vs {mostrar_valor_numerico(fn_cerrada)} (cerrada) - {mensaje}")
        
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
                
                # Calcular usando ambos métodos
                if n_especifico < 100:  # Limitar cálculo recursivo a valores razonables
                    fn_recurrente = calcular_fn_recursivamente(n_especifico, m, coeficientes, valores_iniciales)
                    if hasattr(fn_recurrente, 'evalf'):
                        fn_recurrente_complejo = complex(fn_recurrente.evalf())
                        if abs(fn_recurrente_complejo.imag) < 1e-10:
                            print(f"f({n_especifico}) = {fn_recurrente_complejo.real:.10g} (calculado recursivamente)")
                        else:
                            print(f"f({n_especifico}) = {fn_recurrente_complejo} (calculado recursivamente)")
                    else:
                        print(f"f({n_especifico}) = {fn_recurrente} (calculado recursivamente)")
                
                fn_cerrada = calcular_valor_fn(n_especifico, coeficientes_solucion, raices_con_multiplicidad)
                if isinstance(fn_cerrada, complex):
                    if abs(fn_cerrada.imag) < 1e-10:
                        print(f"f({n_especifico}) = {fn_cerrada.real:.10g} (calculado con expresión cerrada)")
                    else:
                        print(f"f({n_especifico}) = {fn_cerrada} (calculado con expresión cerrada)")
                else:
                    print(f"f({n_especifico}) = {fn_cerrada:.10g} (calculado con expresión cerrada)")
                
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
            except Exception as e:
                print(f"Error al calcular: {e}")
                import traceback
                traceback.print_exc()
    
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()