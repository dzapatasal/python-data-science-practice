# Source: citrus.py

## Acciones a realizar:

1. Cargar los datos. Para hacerlo, importa NumPy y utiliza la función loadtxt. Utiliza el enlace de la URL y el parámetro usecols para omitir la primera columna. Puedes usar **np.arange** para crear la secuencia de números que representan las columnas. Por último, también es necesario incluir el parámetro **skiprows=1** para que la primera línea de texto se omita al leer el archivo.

2. Calcular el coeficiente angular y lineal para la recta de las naranjas y para la recta de las toronjas. Utiliza la fórmula de mínimos cuadrados para encontrar cada uno.

3. Calcular el coeficiente angular utilizando la generación de números aleatorios. Supongamos que ya conoces el valor de b y que este es igual a 17.