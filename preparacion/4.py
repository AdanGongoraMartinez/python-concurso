def string_to_unique_array(s):
    # Crear una lista a partir del string, eliminando duplicados
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char.upper())
    return unique_chars

def evaluate(leters, word):
    validated_chars = []
    for char in word:
        if char in leters:
            validated_chars.append(char)
    if len(validated_chars) == len(word):
        return 'WIN'
    return 'LOSE'

def read_values():
    leters = input('Ingrese las letras a evaluar: ')
    word = input('Ingrese la palabra a evaluar: ')

    return leters, word

def start():
    times = int(input('Ingrese la cantidad de casos a evaluar: '))
    for i in range(times):
        leters, word = read_values()
        array_leters = string_to_unique_array(leters)
        array_word = string_to_unique_array(word)
        print(evaluate(array_leters,array_word))
    return

start()