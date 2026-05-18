import random

# Parámetros
POBLACION_SIZE = 6
GENES = 5  # número de bits
GENERACIONES = 10
TASA_MUTACION = 0.1

# Crear individuo (cadena binaria)
def crear_individuo():
    return ''.join(random.choice('01') for _ in range(GENES))

# Convertir binario a entero
def binario_a_entero(ind):
    return int(ind, 2)

# Función fitness
def fitness(ind):
    x = binario_a_entero(ind)
    return x ** 2

# Selección (torneo simple)
def seleccionar(poblacion):
    return max(random.sample(poblacion, 2), key=fitness)

# Cruce
def cruce(padre1, padre2):
    punto = random.randint(1, GENES - 1)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

# Mutación
def mutar(ind):
    nuevo = ''
    for bit in ind:
        if random.random() < TASA_MUTACION:
            nuevo += '1' if bit == '0' else '0'
        else:
            nuevo += bit
    return nuevo

# Inicializar población
poblacion = [crear_individuo() for _ in range(POBLACION_SIZE)]

# Evolución
for gen in range(GENERACIONES):
    nueva_poblacion = []
    
    for _ in range(POBLACION_SIZE):
        padre1 = seleccionar(poblacion)
        padre2 = seleccionar(poblacion)
        hijo = cruce(padre1, padre2)
        hijo = mutar(hijo)
        nueva_poblacion.append(hijo)
    
    poblacion = nueva_poblacion
    
    mejor = max(poblacion, key=fitness)
    print(f"Generación {gen}: Mejor = {mejor}, x = {binario_a_entero(mejor)}, fitness = {fitness(mejor)}")
