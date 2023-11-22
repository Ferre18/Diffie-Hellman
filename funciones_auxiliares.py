import random

def es_primo(q):
    if q <= 1:
        return False
    elif q == 2:
        return True
    elif q % 2 == 0:
        return False
    else:
        # Iterar desde 3 hasta la raíz cuadrada de q con paso 2
        for i in range(3, int(q**0.5) + 1, 2):
            if q % i == 0:
                return False
        return True
    
def es_raiz_primitiva(alpha, q):
    if alpha < 2 or alpha >= q:
        print("alpha debe estar en el rango [2, q-1]")
        exit(-1)

    # Calcular el conjunto de elementos generados por alpha
    elementos_generados = set(pow(alpha, i, q) for i in range(1, q))

    # Verificar si todos los elementos en el rango [1, q-1] están presentes
    return len(elementos_generados) == q - 1

def numero_aleatorio(n):
    if n <= 1:
        print("n debe ser mayor que 1")
        exit(-1)

    return random.randint(1, n - 1)