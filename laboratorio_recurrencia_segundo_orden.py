import math
import numpy as np

def expresion_no_recurrente(a, b, C0, C1):
    """
  
    """
    
    discriminante = a**2 + 4*b
    
    if abs(discriminante) < 1e-10:  
        r = a / 2
        d = C0
        e = (C1 - d*r) / r if r != 0 else 0  # Evitar división por cero
        
        return {
            "tipo": "raiz_doble",
            "r": r,
            "d": d,
            "e": e,
            "expresion": f"fn = {d:.6f}*({r:.6f}^n) + {e:.6f}*n*({r:.6f}^n)"
        }
    
    else:
        # Dos raíces distintas
        r1 = (a + math.sqrt(discriminante)) / 2
        r2 = (a - math.sqrt(discriminante)) / 2
        
        if abs(r1 - r2) < 1e-10:
            # Tratarlo como raíz doble
            r = (r1 + r2) / 2
            d = C0
            e = (C1 - d*r) / r if r != 0 else 0
            return {
                "tipo": "raiz_doble",
                "r": r,
                "d": d,
                "e": e,
                "expresion": f"fn = {d:.6f}*({r:.6f}^n) + {e:.6f}*n*({r:.6f}^n)"
            }
        
        # Matriz del sistema
        A = np.array([[1, 1], [r1, r2]])
        b = np.array([C0, C1])
        
        try:
            # Resolver el sistema de ecuaciones
            solucion = np.linalg.solve(A, b)
            d, e = solucion
            
            return {
                "tipo": "raices_distintas",
                "r1": r1,
                "r2": r2,
                "d": d,
                "e": e,
                "expresion": f"fn = {d:.6f}*({r1:.6f}^n) + {e:.6f}*({r2:.6f}^n)"
            }
        except np.linalg.LinAlgError:
            # Si hay un problema con la resolución del sistema
            return {
                "tipo": "error",
                "mensaje": "No se pudo resolver el sistema de ecuaciones."
            }


if __name__ == "__main__":
    print("Algoritmo para encontrar expresión no recurrente de una recurrencia lineal homogénea")
    print("Formato: fn = a*fn-1 + b*fn-2, con f0 = C0 y f1 = C1")
    
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    C0 = float(input("Ingrese f0 (C0): "))
    C1 = float(input("Ingrese f1 (C1): "))
    resultado = expresion_no_recurrente(a, b, C0, C1)
    
    print("\nResultado:")
    if resultado["tipo"] == "error":
        print(resultado["mensaje"])
    else:
        print(resultado["expresion"])
        print("\nVerificación de los primeros términos:")
        
        
        f = [C0, C1]
        for n in range(2, 6):
            f.append(a * f[n-1] + b * f[n-2])
        
        print(f"Términos por recurrencia: {f}")
        
        
        f_formula = []
        if resultado["tipo"] == "raices_distintas":
            r1, r2 = resultado["r1"], resultado["r2"]
            d, e = resultado["d"], resultado["e"]
            for n in range(6):
                f_formula.append(d * (r1 ** n) + e * (r2 ** n))
        else:  # raíz doble
            r = resultado["r"]
            d, e = resultado["d"], resultado["e"]
            for n in range(6):
                f_formula.append(d * (r ** n) + e * n * (r ** n))
        
        print(f"Términos por fórmula: {[round(x, 6) for x in f_formula]}")