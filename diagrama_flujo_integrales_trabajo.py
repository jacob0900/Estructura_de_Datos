import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

def crear_diagrama_flujo():
    # Configurar la figura
    fig, ax = plt.subplots(1, 1, figsize=(16, 20))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 25)
    ax.axis('off')
    
    # Colores para diferentes tipos de cajas
    color_inicio = '#e3f2fd'
    color_decision = '#fff3e0'
    color_proceso = '#f1f8e9'
    color_conservativo = '#e8f5e8'
    color_no_conservativo = '#ffebee'
    color_resultado = '#c8e6c9'
    
    # Función para crear cajas rectangulares
    def crear_caja(x, y, width, height, text, color, fontsize=9):
        box = FancyBboxPatch((x-width/2, y-height/2), width, height,
                           boxstyle="round,pad=0.1", 
                           facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
                fontweight='bold', wrap=True)
    
    # Función para crear cajas de decisión (rombos)
    def crear_rombo(x, y, width, height, text, color, fontsize=8):
        # Crear un rombo usando un polígono
        diamond = patches.RegularPolygon((x, y), 4, radius=width/2, 
                                       orientation=np.pi/4,
                                       facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(diamond)
        ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
                fontweight='bold', wrap=True)
    
    # Función para crear flechas
    def crear_flecha(x1, y1, x2, y2, text='', offset=0.2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        if text:
            mid_x, mid_y = (x1+x2)/2 + offset, (y1+y2)/2 + offset
            ax.text(mid_x, mid_y, text, ha='center', va='center', 
                   fontsize=10, fontweight='bold', 
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # INICIO
    crear_caja(5, 23, 3, 1.2, 
              'INICIO\n∮C F⃗·dr⃗\nF⃗ = P î + Q ĵ', 
              color_inicio, 10)
    
    # Flecha hacia abajo
    crear_flecha(5, 22.4, 5, 21.1)
    
    # Primera decisión: ¿Campo conservativo?
    crear_rombo(5, 20, 2.5, 1.5, 
               '¿Campo\nconservativo?\n∂P/∂y = ∂Q/∂x?', 
               color_decision)
    
    # RAMA IZQUIERDA - CONSERVATIVO
    crear_flecha(3.8, 19.2, 2.5, 18.5, 'SÍ', -0.3)
    
    crear_caja(2, 17.5, 2.5, 1.2, 
              'CAMPO\nCONSERVATIVO\n∇ × F⃗ = 0', 
              color_conservativo)
    
    crear_flecha(2, 16.9, 2, 15.6)
    
    crear_caja(2, 15, 2.5, 1.2, 
              'Encontrar función\npotencial f\n∇f = F⃗', 
              color_proceso)
    
    crear_flecha(2, 14.4, 2, 13.1)
    
    crear_caja(2, 12.5, 2.8, 1.2, 
              'Teorema Fundamental:\n∮C F⃗·dr⃗ = f(B) - f(A)', 
              color_proceso)
    
    crear_flecha(2, 11.9, 2, 10.6)
    
    crear_caja(2, 10, 2, 1, 'RESULTADO', color_resultado, 11)
    
    # RAMA DERECHA - NO CONSERVATIVO
    crear_flecha(6.2, 19.2, 7.5, 18.5, 'NO', 0.3)
    
    crear_caja(8, 17.5, 2.5, 1.2, 
              'CAMPO NO\nCONSERVATIVO\n∇ × F⃗ ≠ 0', 
              color_no_conservativo)
    
    crear_flecha(8, 16.9, 8, 15.6)
    
    # Segunda decisión: ¿Camino cerrado?
    crear_rombo(8, 15, 2, 1.2, 
               '¿Camino\ncerrado?', 
               color_decision)
    
    # CAMINO CERRADO - SÍ
    crear_flecha(7, 14.5, 6, 13.8, 'SÍ', -0.3)
    
    # Tercera decisión: ¿Región simplemente conexa?
    crear_rombo(5.5, 13, 2, 1.2, 
               '¿Región\nsimplemente\nconexa?', 
               color_decision, 7)
    
    crear_flecha(5.5, 12.4, 5.5, 11.1, 'SÍ')
    
    crear_caja(5.5, 10.5, 3, 1.2, 
              'TEOREMA DE GREEN:\n∮C (P dx + Q dy) =\n∬D (∂Q/∂x - ∂P/∂y) dA', 
              color_proceso, 8)
    
    crear_flecha(5.5, 9.9, 5.5, 8.6)
    
    crear_caja(5.5, 8, 2.5, 1, 
              'Calcular\nintegral doble', 
              color_proceso)
    
    crear_flecha(5.5, 7.5, 5.5, 6.6)
    
    crear_caja(5.5, 6, 2, 1, 'RESULTADO', color_resultado, 11)
    
    # CAMINO ABIERTO - NO
    crear_flecha(8.8, 14.2, 9.5, 13.5, 'NO', 0.3)
    
    crear_caja(9.5, 12.5, 2.2, 1.2, 
              'PARAMETRIZACIÓN:\nr⃗(t) = x(t)î + y(t)ĵ\nt ∈ [a,b]', 
              color_proceso, 8)
    
    crear_flecha(9.5, 11.9, 9.5, 10.6)
    
    crear_caja(9.5, 10, 2.2, 1, 
              'Calcular dr⃗/dt', 
              color_proceso)
    
    crear_flecha(9.5, 9.5, 9.5, 8.6)
    
    crear_caja(9.5, 8, 2.5, 1.2, 
              '∫[P(x(t),y(t))·dx/dt +\nQ(x(t),y(t))·dy/dt] dt', 
              color_proceso, 8)
    
    crear_flecha(9.5, 7.4, 9.5, 6.6)
    
    crear_caja(9.5, 6, 2, 1, 'RESULTADO', color_resultado, 11)
    
    # Título
    ax.text(5, 24.5, 'DIAGRAMA DE FLUJO PARA INTEGRALES DE TRABAJO', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Leyenda con estrategia adicional
    leyenda_x, leyenda_y = 1, 4
    crear_caja(5, 3, 8, 2.5, 
              'ESTRATEGIA ADICIONAL: CERRAR EL CAMINO\n\n' +
              '1. Cerrar camino C con segmento simple C₂\n' +
              '2. Aplicar Green: ∮C∪C₂ F⃗·dr⃗ = ∬D (∂Q/∂x - ∂P/∂y) dA\n' +
              '3. Calcular ∮C₂ F⃗·dr⃗ por parametrización\n' +
              '4. Resultado = Integral doble - ∮C₂ F⃗·dr⃗', 
              '#e8f4f8', 9)
    
    plt.tight_layout()
    return fig

# Ejecutar y mostrar el diagrama
if __name__ == "__main__":
    fig = crear_diagrama_flujo()
    plt.show()
    
    # Opcional: Guardar como imagen
    # fig.savefig('diagrama_integrales_trabajo.png', dpi=300, bbox_inches='tight')
    print("Diagrama de flujo generado exitosamente!")
    print("\nElementos incluidos:")
    print("✓ Verificación del rotacional")
    print("✓ Teorema de Green")
    print("✓ Parametrización del camino")
    print("✓ Estrategia de cerrar el camino")
    print("✓ Casos conservativos y no conservativos")