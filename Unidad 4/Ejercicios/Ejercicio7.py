def cantidad_divisores(n):
    contador = 0
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            contador += 1
    return contador

numeros = [6, 10, 12, 15, 28, 7]

resultado = list(filter(lambda x: cantidad_divisores(x) > 5, numeros))

print(resultado)