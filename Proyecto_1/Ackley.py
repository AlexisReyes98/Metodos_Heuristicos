import random
import numpy as np
import math
import statistics

def ackley():
    repeticiones = 100
    iteraciones = 10000
    
    a = 20
    b = 0.2
    c = 2*math.pi
    d = 10
    sigma = 0.1
    mejor = 1000
    rep = 1000

    # BUsqueda local iterada
    for i in range(repeticiones):
        # Busqueda local
        for j in range(iteraciones):
            # Vecindario
            x = []
            for i in range(d):
                x.append(random.uniform(-32.768, 32.768))

            sum1 = 0
            sum2 = 0
            for k in range(d):
                xi = x[k]
                sum1 = sum1 + xi**2
                sum2 = sum2 + math.cos(c*xi)

            term1 = -a * math.exp(-b*math.sqrt(sum1/d))
            term2 = -math.exp(sum2/d)

            y = term1 + term2 + a + math.exp(1)
            s = np.random.normal(y, sigma)
            if s < rep:
                rep = s

        if rep < mejor:
            mejor = rep

    return mejor

if __name__ == "__main__":
    lista_mejor = []
    for i in range(30):
        resultado = ackley()
        print(resultado)
        lista_mejor.append(resultado)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("Promedio mejor: ", prom)
    print("Desviación estanadar mejor: ", st_dev)