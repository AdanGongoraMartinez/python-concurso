# No entendi el significado de este ejercicio

# H = puntos de vida
# P = puntos
# K = turnos

def resolver(N, pociones, H, K, P):
    # Ordenamos las pociones en orden para usarlas de la mejor forma
    pociones.sort(reverse=True)
    
    # Comenzamos suponiendo que no usaremos ninguna poción
    escudo_min = max(0, P - (H // K))  # Calcular el escudo mínimo
    vida_restante = H - K * (P - escudo_min)
    pociones_usadas = 0
    
    # Si no podemos sobrevivir con la vida inicial y el escudo mínimo, usamos pociones
    i = 0
    while vida_restante < 0 and i < N:
        H += pociones[i]
        pociones_usadas += 1
        escudo_min = max(0, P - (H // K))  # Recalcular el escudo mínimo
        vida_restante = H - K * (P - escudo_min)
        i += 1
    
    # Resultados
    print(f"POCIONES: {pociones_usadas}")
    print(f"ESCUDO: {escudo_min}")

# Ejemplo de uso con los datos de entrada y salida proporcionados
N1 = 5
pociones1 = [1, 2, 3, 4, 5]
H1, K1, P1 = 450, 15, 60
resolver(N1, pociones1, H1, K1, P1)

N2 = 6
pociones2 = [5, 2, 5, 15, 1, 15]
H2, K2, P2 = 400, 15, 50
resolver(N2, pociones2, H2, K2, P2)
