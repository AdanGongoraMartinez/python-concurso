import statistics


def promedio(calificaciones):
    return (sum(calificaciones) / len(calificaciones))


def moda(calificaciones):
    return (statistics.mode(calificaciones))


def string_to_num_array(calificaciones):
    return [int(num) for num in calificaciones.split()]


def corregir_calificaciones(calificaciones):
    calificaciones_corregidas = []
    for cal in calificaciones:
        if cal < 70:
            calificaciones_corregidas.append(0)
        else:
            calificaciones_corregidas.append(cal)
    return calificaciones_corregidas


def aprovados_reprovados(calificaciones):
    aprovados = 0
    reprovados = 0
    for cal in calificaciones:
        if cal == 0:
            reprovados += 1
        else:
            aprovados += 1
    return aprovados, reprovados


def inicio():
    plateles = int(input('Ingrese la cantidad de plateles: '))
    calificaciones_plateles = []
    cal_plateles_num = []
    todas_calificaciones = []
    for plantel in range(plateles):
        calificaciones_plateles.append(input('Ingrese las calificaciones separadas por un espacio: '))
        cal_plateles_num.append(string_to_num_array(calificaciones_plateles[plantel]))
        cal_plateles_num[plantel] = corregir_calificaciones(cal_plateles_num[plantel])
        todas_calificaciones = todas_calificaciones + cal_plateles_num[plantel]
    print(promedio(todas_calificaciones))
    print(moda(todas_calificaciones))
    for c in range(len(cal_plateles_num)):
        aprovados, reprovados = aprovados_reprovados(cal_plateles_num[c]) # ??
        print(f"{round(promedio(cal_plateles_num[c]),2)} {moda(cal_plateles_num[c])} {aprovados} {reprovados}")
    return


inicio()