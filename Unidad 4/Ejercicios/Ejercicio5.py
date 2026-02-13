



def hanoi(n, desde, hasta, aux):
    if n == 0:
        return 0
    
    movimientos = 0
    
    movimientos += hanoi(n-1, desde, aux, hasta)
    
    print(f"Mover disco {n} desde {desde} hacia {hasta}")
    movimientos += 1
    
    movimientos += hanoi(n-1, aux, hasta, desde)
    
    return movimientos


n = int(input("Ingrese el número de discos (0-20): "))

if 0 <= n <= 20:
    total = hanoi(n, "A", "C", "B")
    print("\nNúmero mínimo de movimientos:", total)
else:
    print("El número debe estar entre 0 y 20")


