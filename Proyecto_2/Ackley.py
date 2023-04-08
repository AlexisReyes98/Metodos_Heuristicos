import numpy as np
import random
import math
import statistics

def Vecindario(d):
    x = []
    for _ in range(d):
        x.append(random.uniform(-32.768, 32.768))
    return x

def recocido_simulado(d, num_Iter):
    solucion = Vecindario(d)
    solucion_eval = ackley(d, solucion)
    temperatura = solucion_eval*0.4     # Valor inicial del parámetro de control
    #print('Temperatura inicial: ',temperatura)
    while temperatura >= 0.1:   # Criterio de terminación
        for _ in range(num_Iter):  # Tiempo en una temperatura dada
            candidato = Vecindario(d)  # Generación de una solución nueva
            candidato_eval = ackley(d, candidato)
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
    return temperatura, solucion_eval

def ackley(d, x):
    sigma = 0.1
    a = 20
    b = 0.2
    c = 2*math.pi

    sum1 = 0
    sum2 = 0
    for i in range(d):
        xi = x[i]
        sum1 = sum1 + xi**2
        sum2 = sum2 + math.cos(c*xi)

    term1 = -a * math.exp(-b*math.sqrt(sum1/d))
    term2 = -math.exp(sum2/d)

    y = term1 + term2 + a + math.exp(1)
    s = np.random.normal(y, sigma)
    return s

if __name__ == "__main__":
    lista_mejor = []
    d = 10

    print("Minimos:\n")
    for _ in range(30):
        temp, resultado = recocido_simulado(d, 3)
        print(resultado)
        lista_mejor.append(resultado)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("\nPromedio mejor: ", prom)
    print("Desviación estanadar mejor: ", st_dev)
