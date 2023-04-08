import numpy as np
import random
import statistics

def Vecindario():
    x1 = random.uniform(-3, 3)
    x2 = random.uniform(-2, 2)
    return x1, x2

def recocido_simulado(num_Iter):
    solucion_x1, solucion_x2 = Vecindario()
    solucion_eval = camel(solucion_x1, solucion_x2)
    temperatura = solucion_eval*0.4     # Valor inicial del parámetro de control
    #print('Temperatura inicial: ',temperatura)
    while temperatura >= 0.1:   # Criterio de terminación
        for _ in range(num_Iter):  # Tiempo en una temperatura dada
            candidato_x1, candidato_x2 = Vecindario()  # Generación de una solución nueva
            candidato_eval = camel(candidato_x1, candidato_x2)
            delta = candidato_eval-solucion_eval    # Cálculo de la diferencia de la solución objetivo
            #print(delta)
            #print('Solución: ',solucion)
            #print('Candidato: ',candidato)
            if delta <= 0 or np.random.uniform(low=0.0, high=1.0, size=None) < np.power(np.e,(-delta/(20*temperatura))):    # Criterio de aceptación
                solucion_x1, solucion_x2, solucion_eval = candidato_x1, candidato_x2, candidato_eval
            #    if delta <= 0:
            #        print('Se acepta la nueva solución') 
            #    else:
            #        print('Se acepta la nueva solución sin mejora')
            #else:
            #    print('No se acepta la nueva solución sin mejora')            
        temperatura = temperatura * np.random.uniform(low=0.8, high=0.99, size=None)    # Perdida de temperatura
        # print('Temperatura final: ',temperatura)
    return temperatura, solucion_eval

def camel(x1, x2):
    sigma = 0.1

    term1 = (4-2.1*x1**2+(x1**4)/3) * x1**2
    term2 = x1*x2
    term3 = (-4+4*x2**2) * x2**2
    
    y = term1 + term2 + term3
    s = np.random.normal(y, sigma)
    return s

if __name__ == "__main__":
    lista_mejor = []

    print("Minimos:\n")
    for _ in range(30):
        temp, resultado = recocido_simulado(3)
        print(resultado)
        lista_mejor.append(resultado)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("\nPromedio mejor: ", prom)
    print("Desviación estanadar mejor: ", st_dev)
