

def contar_caracteres(cadena):
    conteo = {}
    
    for caracter in cadena:
        if caracter in conteo:
            conteo[caracter] += 1
        else:
            conteo[caracter] = 1
    
    return conteo

print(contar_caracteres("Esto es una prueba"))

