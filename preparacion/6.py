# Barbie
import math


def punto_en_linea(x1, y1, x2, y2, x, y):
    # Verificamos si las proporciones son iguales (evitando divisiones por cero)
    if (x2 - x1) == 0:  # Línea vertical
        return x == x1 and min(y1, y2) <= y <= max(y1, y2)
    elif (y2 - y1) == 0:  # Línea horizontal
        return y == y1 and min(x1, x2) <= x <= max(x1, x2)
    else:
        # Comprobamos si las proporciones de las diferencias son iguales
        en_linea = (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1)
        # Verificamos si está dentro del segmento
        en_segmento = min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)
        return en_linea and en_segmento

def string_to_num_array(calificaciones):
    return [int(num) for num in calificaciones.split()]

def inicio():
    coordenadas_string = input('Ingrese las coordenadas de Barbie y la Suprema Corte: ')
    n = int(input('Ingrese la cantidad de amigas de barbie: '))
    cantidad_amigas = 0
    coordenadas = string_to_num_array(coordenadas_string)
    for i in range(n):
        amigas = []
        coor_amiga = input(f'Ingrese las coordenadas de la amiga {i} de Barbie: ')
        amigas = string_to_num_array(coor_amiga)
        if punto_en_linea(coordenadas[0],coordenadas[1],coordenadas[2],coordenadas[3],amigas[0],amigas[1]):
            cantidad_amigas += 1
    print(cantidad_amigas)


inicio()