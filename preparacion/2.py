def entradaValdida (entrada:str):
    if len(entrada) < 20:
        return True

def inicio():
    expresion = input('Ingrese una expresion matematica: ')

    if not entradaValdida(expresion):
        print('LA EXPRESION ES DEMASIADO LARGA')

    try:
        print(eval(expresion))
    except:
        print('LA EXPRESION NO ES VALIDA')

    return 0

inicio()
