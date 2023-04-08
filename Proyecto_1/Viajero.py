import random
import numpy as np
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

def permutacion():
    nombre_arch = "br17.txt"
    matriz_dist, mejor_costo = leer_caso(nombre_arch)
    #print("dist: ",len(matriz_dist))
    #print("costo: ",mejor_costo)

    mi_lista = []
    n = len(matriz_dist)
    # Generación de una permutacion aleatoria de n números (1 a n).
    for i in range(n):
        mi_lista.append(i)

    #print(mi_lista)
    #lista_permutada = np.random.permutation(mi_lista)
    #print(lista_permutada)

    max_iteraciones = 10000
    cont = 0
    resultado = 1000
    suma = 0

    while cont < max_iteraciones:
        lista_permutada = np.random.permutation(mi_lista)
        for i in range(len(lista_permutada)-1):
            suma += matriz_dist[lista_permutada[i]][lista_permutada[i+1]]
        suma += matriz_dist[lista_permutada[n-1]][lista_permutada[0]]
        if suma < resultado:
            resultado = suma
        cont = cont+1

    #print(cont)
    return lista_permutada, resultado

def cambio_ciudades():
    nombre_arch = "br17.txt"
    matriz_dist, mejor_c = leer_caso(nombre_arch)
    #print("dist: ",len(matriz_dist))
    #print("costo: ",mejor_c)

    mi_lista = []
    n = len(matriz_dist)
    # Generación de una lista con cambio de 2 ciudades aleatorias.
    for i in range(n):
        mi_lista.append(i)

    #print(mi_lista)
    lista_permutada = np.random.permutation(mi_lista)
    #print(lista_permutada)

    repeticiones = 100
    iteraciones = 10000
    
    mejor_costo = 100000000
    costo_rep = 100000000
    costo_ite = 0
    lista_aux = []
    lista_solucion = []

    # BUsqueda local iterada
    for i in range(repeticiones):
        # Busqueda local
        for j in range(iteraciones):
            # Vecindario
            while True:
                num1 = random.randint(0, n-1)
                num2 = random.randint(0, n-1)
                if num1 != num2:
                    break
        
            indice = lista_permutada[num1]
            lista_permutada[num1] = lista_permutada[num2]
            lista_permutada[num2] = indice
            #print(lista_permutada)
            for k in range(len(lista_permutada)-1):
                costo_ite += matriz_dist[lista_permutada[k]][lista_permutada[k+1]]
            costo_ite += matriz_dist[lista_permutada[k-1]][lista_permutada[0]]
            if costo_ite < costo_rep:
                costo_rep = costo_ite
                lista_aux = lista_permutada

        if costo_rep < mejor_costo:
            mejor_costo = costo_rep
            lista_solucion = lista_aux

    return lista_solucion, mejor_costo

if __name__ == "__main__":
    solucion = []
    lista_mejor = []
    
    for i in range(30):
        solucion, resultado = cambio_ciudades()
        print(resultado)
        lista_mejor.append(resultado)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("Promedio mejor: ", prom)
    print("Desviación estanadar mejor: ", st_dev)

    #mejor_lista, resultado = permutacion()
    #print("Solucion: ", solucion)
    #print("Mejor Costo: ", resultado)
