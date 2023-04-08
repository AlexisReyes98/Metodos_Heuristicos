import numpy as np
import random
import statistics

def leer_caso(nombre_archivo):
    f = open(nombre_archivo, 'r')
    contenido = f.read()
    f.close()
    numeros = contenido.split()
    capacidad = int(numeros[0])
    n = int(numeros[1])
    peso = [0 for x in range(n)]
    valor = [0 for x in range(n)]
    solucion = [0 for x in range(n)]
    k = 2
    for i in range(n):
        peso[i] = int(numeros[k])
        valor[i] = int(numeros[k+1])
        solucion[i] = int(numeros[k+2])
        k = k+3
    mejor_peso = int(numeros[k])
    mejor_valor = int(numeros[k+1])
    return capacidad, n, peso, valor, solucion, mejor_peso, mejor_valor

def lista_inicio(n):
    mi_lista = []
    # Generación de una lista de binarios aleatorios de n bits
    for _ in range(n):
        mi_lista.append(random.randint(0,1))
    return mi_lista

def vecino_aleatorio(solution, n):
    # Vecindario
    aux_solution = solution.copy()
    num1 = random.randint(0, n-1)
    if aux_solution[num1] == 1:
        aux_solution[num1] = 0
    else:
        aux_solution[num1] = 1
        
    cambio_solution = aux_solution
    return cambio_solution

def recocido_simulado(capacidad, n, peso, valor, num_Iter):
    while True:
        solucion = lista_inicio(n)
        peso_eval, valor_eval = evalua(capacidad, n, solucion, peso, valor)
        if peso_eval != 0 and valor_eval != 0:
            break;
    temperatura = peso_eval*0.4     # Valor inicial del parámetro de control
    #print('Temperatura inicial: ',temperatura)
    while temperatura >= 0.1:   # Criterio de terminación
        for _ in range(num_Iter):  # Tiempo en una temperatura dada
            while True:
                candidato = vecino_aleatorio(solucion.copy(), n)  # Generación de una solución nueva
                candidato_peso, candidato_valor = evalua(capacidad, n, candidato, peso, valor)
                if candidato_peso != 0 and candidato_valor != 0:
                    break;
            delta = candidato_peso-candidato_valor    # Cálculo de la diferencia de la solución objetivo
            #print(delta)
            #print('Solución: ',solucion)
            #print('Candidato: ',candidato)
            if delta <= 0 or np.random.uniform(low=0.0, high=1.0, size=None) < np.power(np.e,(-delta/(20*temperatura))):    # Criterio de aceptación
                solucion, peso_eval, valor_eval = candidato, candidato_peso, candidato_valor
            #    if delta <= 0:
            #        print('Se acepta la nueva solución') 
            #    else:
            #        print('Se acepta la nueva solución sin mejora')
            #else:
            #    print('No se acepta la nueva solución sin mejora')            
        temperatura = temperatura * np.random.uniform(low=0.8, high=0.99, size=None)    # Perdida de temperatura
        # print('Temperatura final: ',temperatura)
    return temperatura, solucion, peso_eval, valor_eval
    
def evalua(capacidad, n, mi_lista, peso, valor):
    # Valor total y peso de la capacidad de la mochila
    v = 0     # valor total
    p = 0     # peso total
    for i in range(n):
        if mi_lista[i] == 1:
            p += peso[i]
            v += valor[i]
    if p > capacidad:  # demasiado grande para entrar en la mochila
        p = 0
        v = 0
    return p, v

if __name__ == "__main__":
    nombre_arch = "P01.txt"
    capacidad, n, peso, valor, solucion, mejor_peso, mejor_valor = leer_caso(nombre_arch)

    lista_solucion = []
    lista_mejor_peso = []
    lista_mejor_valor = []
    
    print("Pesos\tValores\n")
    for _ in range(30):
        temp, lista_solucion, result_peso, result_valor = recocido_simulado(capacidad, n, peso, valor, 3)
        print(result_peso, result_valor)
        lista_mejor_peso.append(result_peso)
        lista_mejor_valor.append(result_valor)
    
    prom_peso = statistics.mean(lista_mejor_peso)
    prom_valor = statistics.mean(lista_mejor_valor)
    st_dev_peso = statistics.pstdev(lista_mejor_peso)
    st_dev_valor = statistics.pstdev(lista_mejor_valor)

    print("\nPromedio peso: ", prom_peso)
    print("Promedio valor: ", prom_valor)
    print("Desviación estanadar peso: ", st_dev_peso)
    print("Desviación estanadar valor: ", st_dev_valor)

    #print("Solucion: ", lista_solucion)        
    #print("Mejor Peso: ", result_peso)
    #print("Mejor Valor: ", result_valor)
    #print("Temperatura: ", temp)