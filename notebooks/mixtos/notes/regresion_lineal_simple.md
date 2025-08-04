# Análisis de Regresión Lineal Simple

Este documento resume la fórmula y el procedimiento para calcular una regresión lineal simple, útil para predecir una variable dependiente (`y`) a partir de una independiente (`x`).

## Definición de variables

| Símbolo | Significado                        |
|---------|------------------------------------|
| $\alpha$ | Pendiente de la recta              |
| $\beta$  | Intersección (ordenada al origen)  |
| $n$      | Número de observaciones            |
| $y$      | Variable dependiente (ej: precio)  |
| $x$      | Variable independiente (ej: fecha) |

## Fórmulas

**Pendiente ($\alpha$):**
$$
\alpha = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2}
$$

**Intersección ($\beta$):**
$$
\beta = \frac{\sum y - \alpha \sum x}{n}
$$

**Ecuación de la recta:**
$$
y = \alpha x + \beta
$$

## Ejemplo numérico

Supón que tienes los siguientes datos:

| x (fecha) | y (precio) |
|-----------|------------|
|     1     |    100     |
|     2     |    110     |
|     3     |    115     |

Calcula los siguientes valores:

- $n = 3$
- $\sum x = 1 + 2 + 3 = 6$
- $\sum y = 100 + 110 + 115 = 325$
- $\sum xy = (1 \times 100) + (2 \times 110) + (3 \times 115) = 100 + 220 + 345 = 665$
- $\sum x^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$

Ahora, sustituimos en la fórmula de la pendiente:

$$
\alpha = \frac{3 \times 665 - 6 \times 325}{3 \times 14 - 6^2} = \frac{1995 - 1950}{42 - 36} = \frac{45}{6} = 7.5
$$

Para la intersección:

$$
\beta = \frac{325 - 7.5 \times 6}{3} = \frac{325 - 45}{3} = \frac{280}{3} \approx 93.33
$$

**Ecuación final:**

$$
y = 7.5x + 93.33
$$

## Referencias

- Aplicación práctica: [np_pd_apples.ipynb](../mixtos/np_pd_apples.ipynb)