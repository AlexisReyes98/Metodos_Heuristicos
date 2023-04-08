import random
import numpy as np
import math
import statistics

def schwef():
    repeticiones = 100
    iteraciones = 10000

    d = 10
    sigma = 0.1
    mejor = 10000
    rep = 10000

    # BUsqueda local iterada
    for i in range(repeticiones):
        # Busqueda local
        for j in range(iteraciones):
            # Vecindario
            x = []
            for i in range(d):
                x.append(random.uniform(-500, 500))

            suma = 0
            for k in range(d):
                xi = x[k]
                suma = suma + xi*math.sin(math.sqrt(abs(xi)))

            y = 418.9829 * d - suma
            s = np.random.normal(y, sigma)
            if s < rep:
                rep = s

        if rep < mejor:
            mejor = rep

    return mejor

if __name__ == "__main__":
    lista_mejor = []
    for i in range(30):
        resultado = schwef()
        print(resultado)
        lista_mejor.append(resultado)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("Promedio mejor: ", prom)
    print("Desviación estanadar mejor: ", st_dev)