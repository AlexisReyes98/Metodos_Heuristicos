import numpy as np
import random
import statistics

def leer_caso(nombre_archivo):
    f = open(nombre_archivo, 'r')
    contenido = f.read()
    f.close()
    numeros = contenido.split()
    n = int(numeros[0])
    mejor_costo = int(numeros[1])
    dist = [[0 for x in range(n)] for y in range(n)]
    k = 1
    for i in range(n):
        for j in range(n):
            k = k+1
            dist[i][j] = int(numeros[k])
    return dist, mejor_costo

def camino_inicio(mat_Dist):
    ruta_Inicial = []
    n = len(mat_Dist)
    # Generación de una lista de ciudades
    for i in range(n):
        ruta_Inicial.append(i)
    return ruta_Inicial

def vecino_aleatorio(solution):
    # Vecindario
    aux_solution = solution.copy()
    cambio_solution = np.random.permutation(aux_solution)
    return cambio_solution

def recocido_simulado(mat_Dist, num_Iter):
    solucion = camino_inicio(mat_Dist)
    solucion_eval = evalua(solucion, mat_Dist)
    temperatura = solucion_eval*0.4     # Valor inicial del parámetro de control
    #print('Temperatura inicial: ',temperatura)
    while temperatura >= 0.1:   # Criterio de terminación
        for _ in range(num_Iter):  # Tiempo en una temperatura dada
            candidato = vecino_aleatorio(solucion.copy())  # Generación de una solución nueva
            candidato_eval = evalua(candidato, mat_Dist)
            delta = candidato_eval-solucion_eval    # Cálculo de la diferencia de la solución objetivo
            #print(delta)
            #print('Solución: ',solucion)
            #print('Candidato: ',candidato)
            if delta <= 0 or np.random.uniform(low=0.0, high=1.0, size=None) < np.power(np.e,(-delta/(20*temperatura))):    # Criterio de aceptación
                solucion, solucion_eval = candidato, candidato_eval
            #    if delta <= 0:
            #        print('Se acepta la nueva solución') 
            #    else:
            #        print('Se acepta la nueva solución sin mejora')
            #else:
            #    print('No se acepta la nueva solución sin mejora')            
        temperatura = temperatura * np.random.uniform(low=0.8, high=0.99, size=None)    # Perdida de temperatura
        # print('Temperatura final: ',temperatura)
    return temperatura, solucion, solucion_eval
    
def evalua(Ruta, mat_Dist):
    costo_ite = 0
    for i in range(len(Ruta)-1):
        costo_ite += mat_Dist[Ruta[i]][Ruta[i+1]]
    costo_ite += mat_Dist[Ruta[i-1]][Ruta[0]]
    return costo_ite

if __name__ == "__main__":
    nombre_arch = "ftv44.txt"
    matriz_dist, mejor_c = leer_caso(nombre_arch)

    lista_solucion = []
    lista_mejor = []
    
    print("Costos:\n")
    for _ in range(30):
        tmp, lista_solucion, costo_result = recocido_simulado(matriz_dist, 3)
        print(costo_result)
        lista_mejor.append(costo_result)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("\nPromedio mejor: ", prom)
    print("Desviación estandar mejor: ", st_dev)

    #print("Solucion: ", lista_solucion)
    #print("Mejor Costo: ", costo_result)
    #print("Temperatura: ", temp)
