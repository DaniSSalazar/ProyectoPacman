import random

n = 100  # cantidad de movimientos

# Generar listas
direcciones= [random.randint(1, 4) for _ in range(n)]

# Imprimir todo en orden limpio
print("---------- DIRECCIONES PAC-MAN ----------")
for d in direcciones:
    print(f"HEX {d:03X}")

