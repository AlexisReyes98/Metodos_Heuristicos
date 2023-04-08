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

def bin_aleatorio():
    nombre_arch = "P01.txt"
    peso = []
    valor = []
    capacidad, num_articulos, peso, valor, solucion, mejor_peso, mejor_valor = leer_caso(nombre_arch)
    #print("capacidad: ", capacidad)
    #print("articulos: ", articulos)
    #print("peso: ", peso)
    #print("valor: ", valor)
    #print("solucion: ", solucion)
    #print("mejor_peso: ", mejor_peso)
    #print("mejor_valor: ", mejor_valor)

    max_iteraciones = 10000
    cont = 0
    res_peso = 1000
    res_valor = 0
    peso_aux = 0
    valor_aux = 0
    
    lista_solucion = []

    while cont < max_iteraciones:
        mi_lista = []
        #Generación de vectores binarios aleatorios de n bits.
        for i in range(num_articulos):
            mi_lista.append(random.randint(0,1))
        
        #print(mi_lista)
        for i in range(num_articulos):
            if mi_lista[i] == 1:
                peso_aux += peso[i]
                valor_aux += valor[i]
        if peso_aux < res_peso:
            res_peso = peso_aux
            res_valor = valor_aux
            lista_solucion = mi_lista
        cont = cont+1
        
    #print(cont)
    return lista_solucion, res_peso, res_valor

def cambio_mbit():
    nombre_arch = "P08.txt"
    capacidad, num_articulos, peso, valor, solucion, mejor_p, mejor_v = leer_caso(nombre_arch)
    #print("capacidad: ", capacidad)
    #print("articulos: ", num_articulos)
    #print("peso: ", peso)
    #print("valor: ", valor)
    #print("solucion: ", solucion)
    #print("mejor_peso: ", mejor_p)
    #print("mejor_valor: ", mejor_v)

    mi_lista = []
    #Generación de vectores binarios aleatorios de n bits.
    for i in range(num_articulos):
        mi_lista.append(random.randint(0,1))

    #print(mi_lista)

    repeticiones = 100
    iteraciones = 10000

    mejor_peso = 100000000
    mejor_valor = 0
    peso_rep = 100000000
    valor_rep = 0
    peso_ite = 0
    valor_ite = 0
    lista_aux = []
    lista_solucion = []

    # BUsqueda local iterada
    for i in range(repeticiones):
        # Busqueda local
        for j in range(iteraciones):
            # Vecindario
            num1 = random.randint(0, num_articulos-1)
            if mi_lista[num1] == 1:
                mi_lista[num1] = 0
            else:
                mi_lista[num1] = 1
            #print(num1)
            #print(mi_lista)
            for k in range(num_articulos):
                if mi_lista[k] == 1:
                    peso_ite += peso[k]
                    valor_ite += valor[k]
            
            if peso_ite < peso_rep:
                peso_rep = peso_ite
                valor_rep = valor_ite
                lista_aux  = mi_lista

        if peso_rep < mejor_peso:
            mejor_peso = peso_rep
            mejor_valor = valor_rep
            lista_solucion = lista_aux

    return lista_solucion, mejor_peso, mejor_valor

if __name__ == "__main__":
    solucion = []
    lista_mejor_peso = []
    lista_mejor_valor = []
    
    for i in range(30):
        solucion, result_peso, result_valor = cambio_mbit()
        print(result_peso, result_valor)
        lista_mejor_peso.append(result_peso)
        lista_mejor_valor.append(result_valor)
    
    prom_peso = statistics.mean(lista_mejor_peso)
    prom_valor = statistics.mean(lista_mejor_valor)
    st_dev_peso = statistics.pstdev(lista_mejor_peso)
    st_dev_valor = statistics.pstdev(lista_mejor_valor)

    print("Promedio peso: ", prom_peso)
    print("Promedio valor: ", prom_valor)
    print("Desviación estanadar peso: ", st_dev_peso)
    print("Desviación estanadar valor: ", st_dev_valor)

    #solucion, result_peso, result_valor = bin_aleatorio()
    #print("Solucion: ", solucion)        
    #print("Mejor Peso: ", result_peso)
    #print("Mejor Valor: ", result_valor)
