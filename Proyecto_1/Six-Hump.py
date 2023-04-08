import random
import numpy as np
import statistics

def camel():
    repeticiones = 100
    iteraciones = 10000
    
    sigma = 0.1
    mejor = 1000
    rep = 1000

    # BUsqueda local iterada
    for i in range(repeticiones):
        # Busqueda local
        for j in range(iteraciones):
            # Vecindario
            x1 = random.uniform(-3, 3)
            x2 = random.uniform(-2, 2)

            term1 = (4-2.1*x1**2+(x1**4)/3) * x1**2
            term2 = x1*x2
            term3 = (-4+4*x2**2) * x2**2

            y = term1 + term2 + term3
            s = np.random.normal(y, sigma)
            if s < rep:
                rep = s

        if rep < mejor:
            mejor = rep

    return mejor

if __name__ == "__main__":
    lista_mejor = []
    for i in range(30):
        resultado = camel()
        print(resultado)
        lista_mejor.append(resultado)
    
    prom = statistics.mean(lista_mejor)
    st_dev = statistics.pstdev(lista_mejor)

    print("Promedio mejor: ", prom)
    print("Desviación estanadar mejor: ", st_dev)