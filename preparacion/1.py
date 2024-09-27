def ganador (espino: int, karel: int):
    if espino > karel:
        return 'ESPINO'

    if karel > espino:
        return 'KAREL'
    else:
        return 'EMPATE'

def limiteValido (variable:int):
    if 0 <= variable <=100:
        return True

    return False

def iniciar():
    try:
        espino = int(input('Ingrese el puntaje de Espino: '))
    except:
        print('ESPINO DEBE SER ENTERO')
        return 0

    if not limiteValido(espino):
        print('ESPINO NO ESTÁ DENTRO DEL LÍMITE')
        return 0

    try:
        karel = int(input('Ingrese el puntaje de Karel: '))
    except:
        print('ESPINO DEBE SER ENTERO')
        return 0

    if not limiteValido(karel):
        print('KAREL NO ESTÁ DENTRO DEL LÍMITE')
        return 0

    print(ganador(espino, karel))

iniciar()
