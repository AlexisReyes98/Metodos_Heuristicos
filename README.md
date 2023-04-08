UEA: Temas Selectos en Computación (Métodos Heurísticos para Optimización)

Metodología ágil usada: SCRUM.

Lenguaje usado: Python

Proyecto 1: Búsqueda local.

En este proyecto se trabajaron tres problemas basados en búsqueda.

-Problema de la mochila.

-Problema del viajero.

-Tres funciones de prueba de optimización: Six-hump camel, Ackley y Schwefel.

Las formas de representación de los datos en cada caso fueron: vectores binarios para el problema de la mochila y vectores de números reales en el resto de los casos.

Problema de la mochila.

Este problema recibe por entrada un archivo de texto que establece el peso máximo de la mochila, el valor óptimo y pesos de los artículos candidatos a incluirse en la mochila.

Problema del viajero.

Este problema recibe por entrada un archivo que contiene el número de ciudades y una matriz con los costos de desplazarse de una ciudad a otra. El objetivo es encontrar  el camino que permita recorrer todas las ciudades con el menor costo posible.

Funciones de prueba de optimización.

file:///home/alexis/Im%C3%A1genes/Six-hump%20camel.jpeg![imagen](https://user-images.githubusercontent.com/72325257/230697680-7694fd52-bb41-494f-b648-92e47121b783.png)

file:///home/alexis/Im%C3%A1genes/Ackley.png![imagen](https://user-images.githubusercontent.com/72325257/230697688-c82657cf-f50e-451b-864f-40485ac9ba70.png)

file:///home/alexis/Im%C3%A1genes/Schwefel.png![imagen](https://user-images.githubusercontent.com/72325257/230697693-48c088f2-d358-4930-810d-990f12c61eb4.png)

La finalidad de estas funciones es evaluar la calidad de la solución propuesta. Las funciones de Ackley y Schwefel presentan valles accidentados, lo que puede derivar en que el resultado no llegue a un óptimo global y se quede atrapado en un óptimo local. Por otro lado, la función Six-hump camel no presenta este problema, por lo que es más fácil que el resultado se encuentre muy cercano al óptimo global.

Proyecto 2: Recocido simulado.

En este proyecto se trabajaron tres problemas basados en búsqueda.

-Problema de la mochila.

-Problema del viajero.

-Tres funciones de prueba de optimización: Six-hump camel, Ackley y Schwefel.

Funciones de prueba de optimización.
Recordando lo visto en el proyecto 1, sabemos que funciones de Ackley y Schwefel presentan valles accidentados, lo que puede derivar en que el resultado no llegue a un óptimo global y se quede atrapado en un óptimo local. Por otro lado, la función Six-hump camel no presenta este problema, por lo que es más fácil que el resultado se encuentre muy cercano al óptimo global.
Para este proyecto se utilizó la técnica de recocido simulado para escapar de los óptimos locales en los que se pudiera llegar a caer. Con la implementación de este algoritmo se espera que los resultados sean mejores a comparación de los resultados obtenidos en el proyecto 1.

Recocido Simulado.

El recocido simulado es un método de búsqueda Montecarlo que toma su nombre de la metodología de calentamiento y enfriamiento del recocido del metal. El algoritmo simula un estado de temperaturas variables donde la temperatura de un estado influye en la probabilidad de toma de decisiones en cada paso. En la implementación de este solucionador, la temperatura de un estado se representa mediante el parámetro delta.

El algoritmo se ejecuta en varias iteraciones:

-Primero se parte de una solución inicial (en cada iteración se genera un vecino).

-Se genera un candidato para comparar con la solución inicial.

-Si la solución vecina (candidato) es peor, entonces se selecciona una probabilidad dada que depende de la temperatura actual (𝑇) y de cuanto se degrade la función objetivo (𝛿). Conforme avanza el algoritmo, la probabilidad decrece.

-Se utiliza com parámetro de control la temperatura (𝑇), para poder determinar la aceptación de soluciones peores.

-En cada nivel de temperatura, se explora un cierto número de soluciones.

-Cada vez que se ha explorado cierto número de soluciones por nivel de temperatura, se decrece la temperatura actual y se itera de nuevo.

Desarrollo:
Para cada problema en el algoritmo de recocido simulado como valor inicial del parámetro de control tomamos a la temperatura igual a la solución a evaluar * 0.4, el tiempo en dicha temperatura fue de 3 iteraciones y el criterio de terminación es que la temperatura fuera mayor o igual a 0.1.

Los valores de estos parámetros fueron escogidos mediante prueba y error.

Funciones de prueba de optimización:

Para las funciones de optimización los parámetros utilizados se describen a continuación:

Six-hump camel: Se utiliza sigma en 0.1 para el cálculo de la distribución normal en el resultado de la función, para lo demás usamos los valores por defecto de dicha función incluyendo las entradas de x1 y x2 en los intervalos siguientes: x1 ∈ (-3, 3) y x2 ∈ (-2, 2).

Ackley: Se utiliza sigma en 0.1 para el cálculo de la distribución normal en el resultado de la función, tomamos como entrada un arreglo de tamaño d = 10 y para lo demás usamos los valores por defecto de dicha función incluyendo el intervalo del arreglo de entrada x ∈ (-32.768, 32.768) y los valores de variables recomendados que fueron a = 20, b = 0.2 y c = 2π

Schwefel: Se utiliza sigma en 0.1 para el cálculo de la distribución normal en el resultado de la función, tomamos como entrada un arreglo de tamaño d = 10 y para lo demás usamos los valores por defecto de dicha función incluyendo el intervalo del arreglo de entrada x ∈ (-500, 500).

Problema de la mochila: Se usa un arreglo binario aleatorio de entrada y como vecindarios el cambio de un bit aleatorio en el arreglo. También consideramos la restricción de no exceder el peso al momento de hacer la evaluación de los artículos introducidos en la mochila.
Para descartar datos que excedan la capacidad de la mochila se utilizó penalización.

Problema del viajero: Se usa un arreglo de i hasta n, donde n es el número total de ciudades para recorrer y cómo vecindario permutaciones aleatorias de dicho arreglo.
