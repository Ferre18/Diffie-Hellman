from sympy import isprime
import random

def generar_clave_privada(q, a):
    # Generar una clave privada aleatoria en el rango [2, q-2]
    clave_privada = random.randint(2, q - 2)
    return clave_privada

def generar_clave_publica(q, a, clave_privada):
    # Calcular la clave publica usando la formula: clave_publica = (a^clave_privada) % q
    clave_publica = pow(a, clave_privada, q)
    return clave_publica

def generar_clave_compartida(q, clave_publica_otro, clave_privada_propia):
    # Calcular la clave compartida usando la formula: clave_compartida = (clave_publica_otro^clave_privada_propia) % q
    clave_compartida = pow(clave_publica_otro, clave_privada_propia, q)
    return clave_compartida

# Parametros compartidos publicamente (q y a)
q = 23
a = 5

# Generar claves privadas y publicas para ambas partes
clave_privada_alice = generar_clave_privada(q, a)
clave_publica_alice = generar_clave_publica(q, a, clave_privada_alice)

clave_privada_bob = generar_clave_privada(q, a)
clave_publica_bob = generar_clave_publica(q, ax, clave_privada_bob)

# Intercambio de claves publicas
clave_compartida_alice = generar_clave_compartida(q, clave_publica_bob, clave_privada_alice)
clave_compartida_bob = generar_clave_compartida(q, clave_publica_alice, clave_privada_bob)

# Ambas partes deberian tener la misma clave compartida
print("Clave compartida por Alice:", clave_compartida_alice)
print("Clave compartida por Bob:", clave_compartida_bob)

# Verificar que ambas partes tienen la misma clave compartida
assert clave_compartida_alice == clave_compartida_bob

