def contarVocales(palabra):
    contador = 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

palabras=["Hola","Como","Estas"]

vocales=list(map(contarVocales, palabras))

print(vocales)
